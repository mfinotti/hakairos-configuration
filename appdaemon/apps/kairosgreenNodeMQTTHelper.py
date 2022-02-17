import hassapi as hass

class KairosgreenNodeMQTTHelper(hass.Hass):

    def initialize(self):
        self.listen_event(self.onMessage, "APPDAEMON_KGNODE_MQTT_INTERNAL_MESSAGE")

    def onMessage(self, event_name, data, kwargs):
        #getting nodes configuration 
        nodeConfiguration = self.args["node"]
        
        payload = data['payload']
        self.log("incoming message for kairosgreen node: %s, message: %s ", payload['node'], payload)
        
        #getting current node
        node = nodeConfiguration[payload["node"]]
        if node:
            #updating kairosgreen node and gateway information
            self.set_state("binary_sensor."+payload["node"], state="on", attributes={"measurement_timestamp": payload["timestamp"]})
            self.set_state("binary_sensor."+payload['gateway'], state="on", attributes={"lastseem_timestamp": payload["timestamp"]})
            #getting configuration keys for data payload extraction
            for key in node.keys():
                payloadValue = payload[key]
                targetEntity = node[key]
                if payloadValue and targetEntity:
                    self.log("Setting state for entity: %s and value %s", targetEntity, payloadValue, level="DEBUG")        
                    self.set_state(targetEntity, state=payloadValue)

