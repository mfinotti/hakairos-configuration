import hassapi as hass
import asyncio

class GreenhouseWindowsPositionManager(hass.Hass):
    def initialize(self):
        self.listen_event(self.manageWindows, "HA_MANAGE_WINDOWS")

    def manageWindows(self, event_name, data, kwargs):    
        event               = data.get('event')
        entitiesToFind      = data.get('entities')
        toPosition          = data.get('toPosition', None)
        positionIncrease    = data.get('positionIncrease', None)
        positionDecrease    = data.get('positionDecrease', None)    
        openCloseTime       = data.get('openCloseTime', None)

        self.log("event data collected: %s", data)
        
        entities = []
        
        for entity in entitiesToFind:
            if "group." in entity:
                #fetch group entities
                entityState = self.get_state(entity, attribute="entity_id")
                #searching into attributes..
                for entityAttribute in entityState:
                    if "group." in entityAttribute:
                        entitiesAttributeState = self.get_state(entityAttribute, attribute="entity_id")
                        for e in entitiesAttributeState:
                            entities.append(self.buildEntityDocumentByEntityName(e, toPosition, positionIncrease, positionDecrease))
                    else:
                        entities.append(self.buildEntityDocumentByEntityName(entityAttribute, toPosition, positionIncrease, positionDecrease))
            else:
                entities.append(self.buildEntityDocumentByEntityName(entity, toPosition, positionIncrease, positionDecrease))

        for entity in entities:
            if "group." not in entity['entity']:
                self.windowsTakeAWhile(entity['entity'], entity['topicCommand'], entity['state'], entity['toPosition'], openCloseTime) 



    def windowsTakeAWhile(self, entity, topic, windowCurrentPosition: int, windowTargetPosition: int, openCloseTime: int) :
        command = None
        
        windowCurrentPosition = int(windowCurrentPosition)
        windowTargetPosition = int(windowTargetPosition)

        #checking if the target position is equals the current position
        if windowCurrentPosition == windowTargetPosition:
            return windowCurrentPosition

        #checking if the target position is 0 or 100 
        if windowTargetPosition == 100 or windowTargetPosition == 0:
            tDelta = openCloseTime
        else: 
            pDelta = windowCurrentPosition - windowTargetPosition
            if pDelta > 0:
                #SALI 
                tDelta = openCloseTime * (pDelta/100)
            else:
                #SCENDI (DA VERIFICARE) 
                pDelta *= -1
                tDelta = openCloseTime * (pDelta/100)
                

            if windowCurrentPosition > windowTargetPosition:
                command = "close"
            else:
                command = "open"

        #windows first command
        self.fire_event("APPDAEMON_MQTT_PUBLISH", topic=topic, command=command)
        #await asyncio.sleep(tDelta)
        #windows second command (stop)
        self.create_task(asyncio.sleep(tDelta), callback=self.callbackStopEvent, topic=topic, command="stop", entity=entity, newPosition=windowTargetPosition, oldPosition=windowCurrentPosition )
        #self.fire_event("APPDAEMON_MQTT_PUBLISH", topic=topic, command="stop")

        # message = "current position: {} was: {} alter: {} seconds".format(windowTargetPosition, windowCurrentPosition, tDelta)
        # mqttClient.publish(topic, message) 


    def callbackStopEvent(self, kwargs):
        self.fire_event("APPDAEMON_MQTT_PUBLISH", topic=kwargs['topic'], command=kwargs['command'])
        self.set_state(kwargs['entity'], state=kwargs['newPosition'])
        
        self.log("Entity [%s] moved to a new position: %d, was: %d", kwargs['entity'], kwargs['newPosition'], kwargs['oldPosition'])
    
    def buildEntityDocumentByEntityName(self, entityName, toPosition, positionIncrease, positionDecrease):
        state           = self.get_state(entityName)
        topicCommand    = self.get_state(entityName, attribute="command_topic")
        entityToUpdate  = self.get_state(entityName, attribute="entityStateToUpdate")

        document = {}
        document['entity']          = entityToUpdate if entityToUpdate != None else entityName
        document['state']           = state
        document['topicCommand']    = topicCommand

        #future position calc
        if toPosition != None and toPosition != "":
            document['toPosition'] = toPosition
        elif positionIncrease != None and "" != positionIncrease:
            futurePosition = int(state) + int(positionIncrease)
            document['toPosition'] = futurePosition if futurePosition <= 100 else 100
        elif positionDecrease != None:
            futurePosition = int(state) - int(positionDecrease)
            document['toPosition'] = futurePosition if futurePosition >= 0 else 0

        return document