import hassapi as hass
import asyncio
import datetime

WEATHER_RAINING                         = "WE_RAINING"
WEATHER_NOT_RAINING                     = "WE_NOT_RAINING"
WEATHER_WIND_NONE                       = "WE_WIND_INTENSITY_NONE"
WEATHER_WIND_MODERATE                   = "WE_WIND_INTENSITY_MODERATE"
WEATHER_WIND_STRONG                     = "WE_WIND_INTENSITY_HIGH"
WEATHER_WIND_DOWNWIND_KEY               = "downwind"
WEATHER_WIND_UPWIND_KEY                 = "upwind"
WEATHER_WIND_MODERATE_KEY               = "moderate"
WEATHER_WIND_STRONG_KEY                 = "strong"
WINDOW_TOP_TYPE_KEY                     = "window_top"
WINDOW_LOW_TYPE_KEY                     = "window_low"

WINDOW_CLOSED_POSITION                  = 0
WINDOW_OPEN_POSITION                    = 100

WINDOW_ACTIVE_KEY                       = "_active"
WINDOW_TOPIC_KEY                        = "_topic"
WINDOW_NAME_KEY                         = "_name"
WINDOW_POSITION_KEY                     = "_position"
WINDOW_TYPE_KEY                         = "_type"
WINDOW_ORIENTATION_KEY                  = "_orientation"

SYSTEM_WINDOWS_RECALIBRATION_ENTITY     = "input_boolean.system_windows_recalibration_inprogress"

class WindowEntity():
    isActive                            : bool
    id                                  : str
    topic                               : str
    name                                : str
    currentPosition                     : int
    entityToUpdate                      : str
    windowType                          : str
    windowOrientation                   : str

    def __init__(self, isActive, id, name, topic, currentPosition, entityToUpdate, windowType, windowOrientation
    ) -> None: 
        self.isActive           = isActive
        self.id                 = id
        self.name               = name
        self.topic              = topic
        self.currentPosition    = currentPosition
        self.entityToUpdate     = entityToUpdate
        self.windowType         = windowType
        self.windowOrientation  = windowOrientation

    # @property
    def isActive(self):
        return self.isActive

    # @property
    def id(self):
        return self.id
    
    # @property
    def name(self):
        return self.name
    
    # @property
    def topic(self):
        return self.topic

    # @property
    def currentPosition(self):
        return self.currentPosition
    
    # @property
    def windowType(self):
        return self.windowType

    # @property
    def entityToUpdate(self):
        return self.entityToUpdate

    # @property
    def windowOrientation(self):
        return self.windowOrientation

    def __str__(self) -> str:
        activeVal = str(self.isActive)
        return ("isActive:"+ activeVal 
            +", id:"+self.id
            +", name:"+self.name
            +", topic:"+self.topic
            +", currentPosition:"+str(self.currentPosition)
            +", entityToUpdate:"+str(self.entityToUpdate)
            +", windowType:"+self.windowType
            +", windowOrientation:"+self.windowOrientation
        )


class PeriodConfiguration():
    isActive                            : bool
    startPeriod                         : datetime 
    endPeriod                           : datetime
    targetTemperature                   : float
    windowLowMaxOpen                    : int
    windowTopMaxOpen                    : int

    windowTopMaxOpenDownwindModerate    : int
    windowLowMaxOpenDownwindModerate    : int
    windowTopMaxOpenDownwindHigh        : int 
    windowLowMaxOpenDownwindHigh        : int
    windowTopMaxOpenUpwindModerate      : int
    windowTopMaxOpenUpwindHigh          : int
    


    def __init__(self, isActive, startPeriod, targetTemperature, windowLowMaxOpen, windowTopMaxOpen,
        windowTopMaxOpenDownwindModerate    : int = 0,
        windowLowMaxOpenDownwindModerate    : int = 0,
        windowTopMaxOpenDownwindHigh        : int = 0,
        windowLowMaxOpenDownwindHigh        : int = 0,
        windowTopMaxOpenUpwindModerate      : int = 0,
        windowTopMaxOpenUpwindHigh          : int = 0,
        
    ) -> None:
        self.isActive               = isActive
        self.startPeriod            = datetime.datetime.strptime(startPeriod, "%H:%M:%S").time() 
        self.targetTemperature      = targetTemperature
        self.windowLowMaxOpen       = windowLowMaxOpen
        self.windowTopMaxOpen       = windowTopMaxOpen
        
        self.windowTopMaxOpenDownwindModerate   = windowTopMaxOpenDownwindModerate
        self.windowLowMaxOpenDownwindModerate   = windowLowMaxOpenDownwindModerate
        self.windowTopMaxOpenDownwindHigh       = windowTopMaxOpenDownwindHigh
        self.windowLowMaxOpenDownwindHigh       = windowLowMaxOpenDownwindHigh
        self.windowTopMaxOpenUpwindModerate     = windowTopMaxOpenUpwindModerate
        self.windowTopMaxOpenUpwindHigh         = windowTopMaxOpenUpwindHigh


    # @property
    def isActive(self):
        return self.isActive

    # @property
    def startPeriod(self):
        return self.startPeriod
    
    # @property
    def endPeriod(self):
        return self.endPeriod

    # @property
    def targetTemperature(self):
        return self.targetTemperature
    
    # @property
    def windowLowMaxOpen(self):
        return self.windowLowMaxOpen
    
    # @property
    def windowTopMaxOpen(self):
        return self.windowTopMaxOpen

    # @property
    def windowTopMaxOpenDownwindModerate(self):
        return self.windowTopMaxOpenDownwindModerate

    # @property
    def windowLowMaxOpenDownwindModerate(self):
        return self.windowLowMaxOpenDownwindModerate

    # @property
    def windowTopMaxOpenDownwindHigh(self):
        return self.windowTopMaxOpenDownwindHigh

    # @property
    def windowLowMaxOpenDownwindHigh(self):
        return self.windowLowMaxOpenDownwindHigh

    # @property
    def windowTopMaxOpenUpwindModerate(self):
        return self.windowTopMaxOpenUpwindModerate
    
    # @property
    def windowTopMaxOpenUpwindHigh(self):
        return self.windowTopMaxOpenUpwindHigh

    # @endPeriod.setter
    def setEndPeriod(self, value):
        self.endPeriod = value

    def __str__(self) -> str:
        activeVal = str(self.isActive)
        stringPeriod1 = str(self.startPeriod)
        stringPeriod2 = str(self.endPeriod)
        return ("isActive:"+ activeVal 
            +", startPeriod:"+stringPeriod1
            +", endPeriod:"+stringPeriod2
            +", targetTemperature:"+self.targetTemperature
            +", windowLowMaxOpen:"+self.windowLowMaxOpen
            +", windowTopMaxOpen:"+self.windowTopMaxOpen
            +", windowTopMaxOpenDownwindModerate:"+str(self.windowTopMaxOpenDownwindModerate)
            +", windowLowMaxOpenDownwindModerate:"+str(self.windowLowMaxOpenDownwindModerate)
            +", windowTopMaxOpenDownwindHigh:"+str(self.windowTopMaxOpenDownwindHigh)
            +", windowLowMaxOpenDownwindHigh:"+str(self.windowLowMaxOpenDownwindHigh)
            +", windowTopMaxOpenUpwindModerate:"+str(self.windowTopMaxOpenUpwindModerate)
            +", windowTopMaxOpenUpwindHigh:"+str(self.windowTopMaxOpenUpwindHigh)
        )

class GreenhouseWindowsPositionManager(hass.Hass):

    def initialize(self):
        self.listen_event(self.manageWindows, "HA_MANAGE_WINDOWS3")

    def manageWindows(self, event_name, data, kwargs):    
        
        event   = data.get('event')
        
        isRecalibrationInProgress: bool = False
        if self.get_state(SYSTEM_WINDOWS_RECALIBRATION_ENTITY) == "on":
            isRecalibrationInProgress = True

        if isRecalibrationInProgress:
            if event == "windows_s7_recalibration" or event == "windows_s8_recalibration":
                self.log("There is already one running process for windows recalibration Event: %s", event, level="WARNING")
                return
            
        self.create_task(asyncio.sleep(1), callback=self.manageWindowsProcess, data=data )

        

    def manageWindowsProcess(self, kwargs):
        data                            = kwargs['data']
        event                           = data.get('event')

        if self.get_state(SYSTEM_WINDOWS_RECALIBRATION_ENTITY) == "on": 
            self.log("Windows recalibration in progress.. Event: %s will be delayed for 30 seconds...", event)
            self.create_task(asyncio.sleep(30), callback=self.manageWindowsProcess, data=data )
            return 

        groupPeriodActive               = data.get('periodActive')
        groupPeriod                     = data.get('period', None)
        groupPeriodTemperature          = data.get('periodTemperature', None)
        groupPeriodWindowTopMaxOpen     = data.get('periodWindowTopMaxOpen', None) 
        groupPeriodWindowLowMaxOpen     = data.get('periodWindowLowMaxOpen', None)
        valueToCheck                    = data.get('valueToCheck', None)
        entities                        = data.get('entities', None)
        openCloseTime                   = data.get('openCloseTime', None)
        windowsMinStep                  = data.get('windowsMinStep', 5)
        temperatureTrend                = data.get('temperatureTrend')

        groupPeriodWindWindowTopMaxOpen = data.get('periodWindWindowTopMaxOpen', None)
        groupPeriodWindWindowLowMaxOpen = data.get('periodWindWindowLowMaxOpen', None)

        rainSensor                      = data.get('rainingSensor', False)
        windSensor                      = data.get('windSensor', False)
        windDirectionSensor             = data.get('windDirectionSensor', False)
        structure_orientation           = data.get('structure_orientation', None)

        self.log("event data collected: %s", data)

        #reset periods
        periods = []
        windows = []
        #rebuild periods
        self.buildPeriods(periods, 
            groupPeriodActive               = groupPeriodActive, 
            groupPeriod                     = groupPeriod, 
            groupPeriodTemperature          = groupPeriodTemperature, 
            groupPeriodWindowTopMaxOpen     = groupPeriodWindowTopMaxOpen, 
            groupPeriodWindowLowMaxOpen     = groupPeriodWindowLowMaxOpen,
            groupPeriodWindWindowTopMaxOpen = groupPeriodWindWindowTopMaxOpen,
            groupPeriodWindWindowLowMaxOpen = groupPeriodWindWindowLowMaxOpen)

        now = datetime.datetime.now().time()
        currentPeriod = None
        for period in periods:
            self.log("period configuration: %s", period, level="DEBUG")
            #finding the current period
            if period.isActive and self.time_in_range(period.startPeriod, period.endPeriod, now) :
                currentPeriod = period

        if currentPeriod:
            self.log("current period detected: %s", currentPeriod)
            #rebuild windows entities
            windows = self.buildWindows(entities)
        else:
            self.log("Period not found. skipping...", level="WARNING")
            return

        if len(windows) == 0:
            self.log("None windows found for this event. skipping..", level="WARNING")
            return

        if event == "windows_check":
            self.manageWindowsByTemperature(currentPeriod, 
                valueToCheck, 
                temperatureTrend, 
                windows, 
                windowsMinStep, 
                openCloseTime,
                rainSensor,
                windSensor,
                windDirectionSensor,
                structure_orientation)
        
        if event == "raining":
            self.manageWindowsByRain(currentPeriod,
                windows,
                openCloseTime)

        if event == "wind":
            self.manageWindowsByWind(currentPeriod,
                windows,
                openCloseTime,
                rainSensor,
                windSensor,
                windDirectionSensor,
                structure_orientation)

        if event == "windows_s7_recalibration" or event == "windows_s8_recalibration":
            self.manageWindowsRecalibrationEvent(currentPeriod,
                windows,
                openCloseTime)

    def manageWindowsByWind(self,
        currentPeriod : PeriodConfiguration, 
        windowsEntity, 
        openCloseTime,
        rainSensor,
        windSensor,
        windDirectionSensor,
        structure_orientation
    ):

        upwindSource    = structure_orientation['upwind']
        downwindSource  = structure_orientation['downwind']
        self.log("Structure exposure to Upwind: %s, Downwind: %s", upwindSource, downwindSource)

        for entity in windowsEntity:
            entity : WindowEntity
            
            if rainSensor == WEATHER_RAINING and self.isWindowTopType(entity):
                self.log("skipping current top window %s on wind event due rain", entity.name)
                continue

            toPosition = None
            isOnUpwindDownwind = self._checkIsOnUpwindDownwind(entity, windSensor, windDirectionSensor, upwindSource, downwindSource)
            if isOnUpwindDownwind and self.isWindowTopType(entity):
                if isOnUpwindDownwind == WEATHER_WIND_DOWNWIND_KEY:
                    #downwind
                    if windSensor == WEATHER_WIND_MODERATE:
                        toPosition = currentPeriod.windowTopMaxOpenDownwindModerate
                    else:
                        toPosition = currentPeriod.windowTopMaxOpenDownwindHigh
                else:
                    #upwind
                    if windSensor == WEATHER_WIND_MODERATE:
                        toPosition = currentPeriod.windowTopMaxOpenUpwindModerate
                    else:
                        toPosition = currentPeriod.windowTopMaxOpenUpwindHigh
            elif isOnUpwindDownwind and not self.isWindowTopType(entity):
                if isOnUpwindDownwind == WEATHER_WIND_DOWNWIND_KEY:
                     #downwind
                    #windows low are excluded from upwinds because the greenhouse has four sides and the opposite side of this works like as a shield for this window.
                    if windSensor == WEATHER_WIND_MODERATE:
                        toPosition =  currentPeriod.windowLowMaxOpenDownwindModerate
                    else:
                        toPosition = currentPeriod.windowLowMaxOpenDownwindHigh
               
            
            if toPosition:    
                if self.isWindowTopType(entity):
                    self.windowsTakeAWhile(entity.entityToUpdate, entity.topic, entity.currentPosition, int(float(toPosition)), self._getWindowTopOpenCloseTime(openCloseTime))
                else:
                    self.windowsTakeAWhile(entity.entityToUpdate, entity.topic, entity.currentPosition, int(float(toPosition)), self._getWindowLowOpenCloseTime(openCloseTime))

    def manageWindowsRecalibrationEvent(self,
        currentPeriod : PeriodConfiguration, 
        windowsEntity, 
        openCloseTime
    ):
        self.set_state(SYSTEM_WINDOWS_RECALIBRATION_ENTITY, state="on")
        self.log("WINDOWS RECALIBRATION PROCESS STARTED")
        for entity in windowsEntity:
            entity : WindowEntity
            toPosition = WINDOW_CLOSED_POSITION
            self.windowsTakeAWhile(entity.entityToUpdate, entity.topic, entity.currentPosition, toPosition, self._getWindowTopOpenCloseTime(openCloseTime))
        
        self.create_task(asyncio.sleep(30), callback=self.callbackWindowsCalibrationEvent, windowsEntity=windowsEntity )
        

    def callbackWindowsCalibrationEvent(self, kwargs):
        windowsEntity = kwargs['windowsEntity']
        self.log("WINDOWS CALIBRATION IN PROGRESS. Checking if the windows is on reset position (0)")
        isAllWindowsClosed : bool = False
        for entity in windowsEntity:
            entity : WindowEntity
            if int(float(self.get_state(entity.entityToUpdate))) > 0:
                break
            isAllWindowsClosed = True
            if isAllWindowsClosed:
                self.set_state(SYSTEM_WINDOWS_RECALIBRATION_ENTITY, state="off")
                break
       
        if not isAllWindowsClosed:
            self.create_task(asyncio.sleep(30), callback=self.callbackWindowsCalibrationEvent, windowsEntity=windowsEntity )
            return

        self.log("All windows is on reset position. Windows recalibration process ended.")
        self.log("WINDOWS CALIBRATION COMPLETE")

    def manageWindowsByRain(self,
        currentPeriod : PeriodConfiguration, 
        windowsEntity, 
        openCloseTime
    ):
        for entity in windowsEntity:
            entity : WindowEntity
            #close all windows top
            if self.isWindowTopType(entity):
                toPosition = WINDOW_CLOSED_POSITION
                self.windowsTakeAWhile(entity.entityToUpdate, entity.topic, entity.currentPosition, toPosition, self._getWindowTopOpenCloseTime(openCloseTime))
           

    def manageWindowsByTemperature(self, 
        currentPeriod : PeriodConfiguration, 
        currentTemperature, 
        temperatureTrend, 
        windowsEntity,
        windowsMinStep, 
        openCloseTime,
        rainSensor,
        windSensor,
        windDirectionSensor,
        structure_orientation):
        
        windowLowOpenCloseTime  = self._getWindowLowOpenCloseTime(openCloseTime)
        windowTopOpenCloseTime  = self._getWindowTopOpenCloseTime(openCloseTime)
        upwindSource            = structure_orientation['upwind']
        downwindSource          = structure_orientation['downwind']
        toPosition              = None

        #checking the target temperature
        targetTemperature = float(currentPeriod.targetTemperature)
        
        if "unknown" == currentTemperature:
            self.log("UNKNOWN value for current temperature. Skipping windows position managing..", level="WARNING")
            return
            
        temperatureComparison = "ABOVE" if float(currentTemperature) > targetTemperature else "BELOW"
        self.log("current temperature: %s it's %s the target temperature %s", currentTemperature, temperatureComparison, targetTemperature)
        self.log("temperature trend is: %s", temperatureTrend)


        for window in windowsEntity:
            window : WindowEntity

            self.log("window: %s", window)
            if rainSensor == WEATHER_RAINING and self.isWindowTopType(window):
                self.log("window name %s skipped due rain presence", window.name)
                continue

            isOnUpwindDownwind = self._checkIsOnUpwindDownwind(window, windSensor, windDirectionSensor, upwindSource, downwindSource)
            if isOnUpwindDownwind:
                self.log("window name %s with orientation: %s skipped due wind presence direction: %s and intensity: %s. The window is on: %s ", window.name, window.windowOrientation, windDirectionSensor, windSensor, isOnUpwindDownwind)
                continue

            if targetTemperature-currentTemperature < -1: #TODO METTERE UNA TOLLERANZA CONFIGURABILE
                
                # more than one degree above the temperature target at this point i need to check the trend for a deeper examination
                # CASE 1 trend = BALANCED -> continue to open
                # CASE 2 trend = FALLING -> nothing to do, check again in the next iteration 
                # CASE 3 trend = RISING -> very bad, we are far from setpoing
                if temperatureTrend == "BALANCED":
                    toPosition = self.calculateWindowFuturePosition(windowEntity=window, currentPeriod=currentPeriod, needToOpen=True, windowsMinStep=windowsMinStep)

                elif temperatureTrend == "FALLING":
                    continue #good job kairos!! 

                elif temperatureTrend == "RISING":
                    toPosition = self.calculateWindowFuturePosition(windowEntity=window, currentPeriod=currentPeriod, needToOpen=True, windowsMinStep=windowsMinStep)
                
            elif targetTemperature-currentTemperature > 1: #TODO METTERE UNA TOLLERANZA CONFIGURABILE          
                
                # more than one degree below the temperature target, checking the trend for a decision..
                # CASE 1 trend = BALANCED -> continue to close
                # CASE 2 trend = FALLING -> very bad, the temperature are every minute more far from the setpoint
                # CASE 3 trend = RISING ->  nothing to do, check again in the next iteration  
                if temperatureTrend == "BALANCED":
                    toPosition = self.calculateWindowFuturePosition(windowEntity=window, currentPeriod=currentPeriod, needToOpen=False, windowsMinStep=windowsMinStep)

                elif temperatureTrend == "FALLING":
                    toPosition = self.calculateWindowFuturePosition(windowEntity=window, currentPeriod=currentPeriod, needToOpen=False, windowsMinStep=windowsMinStep)  

                elif temperatureTrend == "RISING":
                    continue #good job kairos!! 

            else:
                self.log("Nothing to do, the temperature is OK.")
                continue        

            openCloseTime = None
            if self.isWindowTopType(window):
                openCloseTime = windowTopOpenCloseTime
            else:
                openCloseTime = windowLowOpenCloseTime

            self.windowsTakeAWhile(window.entityToUpdate, window.topic, window.currentPosition, toPosition, openCloseTime)


    def buildWindows(self, windowsConf):

        windows     = []
        entityKeys  = []
        self._getEntitiesInGroup(windowsConf, entityKeys)

        for key in entityKeys:
            #1 check if the current windows is enabled
            keyComposed = key+WINDOW_ACTIVE_KEY
            keyComposed = keyComposed.replace("input_text", "input_boolean")
            state = self.get_state(keyComposed)
            if "on" == state or True == state:
                try:
                    #2 getting all window date by his own keys
                    #2.1 getting name
                    keyComposed = key+WINDOW_NAME_KEY
                    name = self.get_state(keyComposed)
                    #2.2 getting id
                    id = key
                    #2.3 getting topic
                    keyComposed = key+WINDOW_TOPIC_KEY
                    topic = self.get_state(keyComposed)
                    #2.4 getting current position
                    keyComposed = key+WINDOW_POSITION_KEY
                    entityToUpdate = keyComposed.replace("input_text", "input_number")
                    position = self.get_state(entityToUpdate)
                    #2.5 getting orientation
                    keyComposed = key+WINDOW_ORIENTATION_KEY
                    keyComposed = keyComposed.replace("input_text", "input_select")
                    orientation = self.get_state(keyComposed)
                    #2.6 getting window type
                    keyComposed = key+WINDOW_TYPE_KEY
                    keyComposed = keyComposed.replace("input_text", "input_select")
                    type = self.get_state(keyComposed)

                    windowEntity = WindowEntity(True, id, name, topic, position, entityToUpdate, type, orientation)
                    self.log("window entity: %s", windowEntity, level="DEBUG")
                    windows.append(windowEntity)
                except Exception as e:
                    self.log("Error occourred: %s", e)
                    continue
            else: 
                self.log("window id: %s skipped. It is disabled! value: %s ", keyComposed, state)


        return windows


    def buildPeriods(self, periods, groupPeriodActive, groupPeriod, groupPeriodTemperature, groupPeriodWindowTopMaxOpen, groupPeriodWindowLowMaxOpen, groupPeriodWindWindowTopMaxOpen, groupPeriodWindWindowLowMaxOpen):
        index: int = 0
        
        windWindowTopMaxOpen    = {}
        windWindowLowMaxOpen    = {}
        self._extractWindSettingsFromParameters(groupPeriodWindWindowTopMaxOpen, windWindowTopMaxOpen)
        self._extractWindSettingsFromParameters(groupPeriodWindWindowLowMaxOpen, windWindowLowMaxOpen)

        if groupPeriodWindWindowLowMaxOpen:
            if WEATHER_WIND_DOWNWIND_KEY in groupPeriodWindWindowLowMaxOpen:
                if WEATHER_WIND_MODERATE_KEY in groupPeriodWindWindowLowMaxOpen[WEATHER_WIND_DOWNWIND_KEY]:
                    entitiesInGroup = self.get_state(groupPeriodWindWindowLowMaxOpen[WEATHER_WIND_DOWNWIND_KEY][WEATHER_WIND_MODERATE_KEY], attribute="entity_id")
                    for entity in entitiesInGroup:
                        state = self.get_state(entity)

        entitiesInPeriodActiveGroup = self.get_state(groupPeriodActive, attribute="entity_id")
        for entityName in entitiesInPeriodActiveGroup:
            state = self.get_state(entityName)
            if state == "on" or state == True:
                currentIsActive = True
            else:
                continue
                currentIsActive = False

            #getting period value
            currentPeriod = self.get_state(self.get_state(groupPeriod, attribute="entity_id")[index])
 
            #getting period temperature
            currentPeriodTemperature = self.get_state(self.get_state(groupPeriodTemperature, attribute="entity_id")[index])
            #getting period window Top MAX open position
            currentPeriodWindowTopMaxOpen = self.get_state(self.get_state(groupPeriodWindowTopMaxOpen, attribute="entity_id")[index])

            #getting period window Low MAX open position
            currentPeriodWindowLowMaxOpen = self.get_state(self.get_state(groupPeriodWindowLowMaxOpen, attribute="entity_id")[index])

            periodWindowTopDownwindModerateMaxOpen      = None
            periodWindowLowDownwindModerateMaxOpen      = None
            periodWindowTopDownwindStrongMaxOpen        = None
            periodWindowLowDownwindStrongMaxOpen        = None
            periodWindowTopUpwindModerateMaxOpen        = None
            periodWindowLowUpwindModerateMaxOpen        = None
            periodWindowTopUpwindStrongMaxOpen          = None
            periodWindowLowUpwindStrongMaxOpen          = None

            #windows top
            if WEATHER_WIND_DOWNWIND_KEY in windWindowTopMaxOpen:
                if WEATHER_WIND_MODERATE_KEY in windWindowTopMaxOpen[WEATHER_WIND_DOWNWIND_KEY]:
                    periodWindowTopDownwindModerateMaxOpen = windWindowTopMaxOpen[WEATHER_WIND_DOWNWIND_KEY][WEATHER_WIND_MODERATE_KEY][index]
            if WEATHER_WIND_DOWNWIND_KEY in windWindowTopMaxOpen:
                if WEATHER_WIND_STRONG_KEY in windWindowTopMaxOpen[WEATHER_WIND_DOWNWIND_KEY]:
                    periodWindowTopDownwindStrongMaxOpen = windWindowTopMaxOpen[WEATHER_WIND_DOWNWIND_KEY][WEATHER_WIND_STRONG_KEY][index]    
            if WEATHER_WIND_UPWIND_KEY in windWindowTopMaxOpen:
                if WEATHER_WIND_MODERATE_KEY in windWindowTopMaxOpen[WEATHER_WIND_UPWIND_KEY]:
                    periodWindowTopUpwindModerateMaxOpen = windWindowTopMaxOpen[WEATHER_WIND_UPWIND_KEY][WEATHER_WIND_MODERATE_KEY][index]
            if WEATHER_WIND_UPWIND_KEY in windWindowTopMaxOpen:
                if WEATHER_WIND_STRONG_KEY in windWindowTopMaxOpen[WEATHER_WIND_DOWNWIND_KEY]:
                    periodWindowTopUpwindStrongMaxOpen = windWindowTopMaxOpen[WEATHER_WIND_UPWIND_KEY][WEATHER_WIND_STRONG_KEY][index]

            #windows low
            if WEATHER_WIND_DOWNWIND_KEY in windWindowLowMaxOpen:
                if WEATHER_WIND_MODERATE_KEY in windWindowLowMaxOpen[WEATHER_WIND_DOWNWIND_KEY]:
                    periodWindowLowDownwindModerateMaxOpen = windWindowLowMaxOpen[WEATHER_WIND_DOWNWIND_KEY][WEATHER_WIND_MODERATE_KEY][index]
            if WEATHER_WIND_DOWNWIND_KEY in windWindowLowMaxOpen:
                if WEATHER_WIND_STRONG_KEY in windWindowLowMaxOpen[WEATHER_WIND_DOWNWIND_KEY]:
                    periodWindowLowDownwindStrongMaxOpen = windWindowLowMaxOpen[WEATHER_WIND_DOWNWIND_KEY][WEATHER_WIND_STRONG_KEY][index]    

            period = PeriodConfiguration(
                        isActive=currentIsActive, 
                        startPeriod=currentPeriod,
                        targetTemperature=currentPeriodTemperature,
                        windowLowMaxOpen=currentPeriodWindowLowMaxOpen,
                        windowTopMaxOpen=currentPeriodWindowTopMaxOpen,
                        windowTopMaxOpenDownwindModerate=periodWindowTopDownwindModerateMaxOpen,
                        windowTopMaxOpenDownwindHigh=periodWindowTopDownwindStrongMaxOpen,
                        windowTopMaxOpenUpwindModerate=periodWindowTopUpwindModerateMaxOpen,
                        windowTopMaxOpenUpwindHigh=periodWindowTopUpwindStrongMaxOpen,
                        windowLowMaxOpenDownwindModerate=periodWindowLowDownwindModerateMaxOpen,
                        windowLowMaxOpenDownwindHigh=periodWindowLowDownwindStrongMaxOpen
                        )
                    
            periods.append(period)

            index = index+1
        
        ##closig last end period with the period value of the first
        index = 0
        firstStartPeriod = None
        if len(periods) == 1:
            firstStartPeriod = periods[0].startPeriod
            testDate = datetime.datetime(2021, 12, 18, firstStartPeriod.hour, firstStartPeriod.minute, 0)
            endPeriod =  (testDate - datetime.timedelta(seconds=1)).time()
            periods[0].setEndPeriod(endPeriod)
        else: 
            for p in periods:
                if index == 0:
                    firstStartPeriod = p.startPeriod
                    index = index+1
                    continue
                else:
                    periods[index-1].setEndPeriod(p.startPeriod)
                index = index+1

            periods[len(periods)-1].setEndPeriod(firstStartPeriod)


    def _checkIsOnUpwindDownwind(self, windowEntity : WindowEntity, windSensor, windDirection, structureUpwind, structureDownwind):

        if windSensor == WEATHER_WIND_NONE:
            return None

        windowOrientation   = windowEntity.windowOrientation

        if self.isWindowTopType(windowEntity):
            if windDirection == self._calcBackwardOrientation(structureDownwind):
                #downwind
                return WEATHER_WIND_DOWNWIND_KEY
            elif windDirection == self._calcBackwardOrientation(structureUpwind):
                return WEATHER_WIND_UPWIND_KEY
        else:
            if self._calcBackwardOrientation(windDirection)  == windowOrientation:
                return WEATHER_WIND_DOWNWIND_KEY

        return None


    def _extractWindSettingsFromParameters(self, groupEntity, windWindowMaxOpen):

        groupKey1 = None
        groupKey2 = None

        for k1 in groupEntity.keys():
            groupKey1 = k1
            if groupKey1 not in windWindowMaxOpen:
                windWindowMaxOpen[groupKey1] = {}
                 
            for k2 in groupEntity[groupKey1].keys():
                groupKey2 = k2
                windWindowMaxOpen[groupKey1][groupKey2] = self._getGroupEntityState(groupEntity=groupEntity, groupKey1=groupKey1, groupKey2=groupKey2)
            
            groupKey1 = None
            groupKey2 = None

    
    def _getEntitiesInGroup(self, groupEntity, entityArray):
        groupEntity = self.get_state(groupEntity, attribute="entity_id")
        for entity in groupEntity:
            if "group." in entity:
                #fetch group entities
                entityState = self.get_state(entity, attribute="entity_id")
                #searching into attributes..
                for entityAttribute in entityState:
                    if "group." in entityAttribute:
                        entitiesAttributeState = self.get_state(entityAttribute, attribute="entity_id")
                        for e in entitiesAttributeState:
                            entityArray.append(e)
                    else:
                        entityArray.append(entityAttribute)
            else:
                entityArray.append(entity)
    
    
    def _getGroupEntityState(self, groupEntity, groupKey1, groupKey2 = None):
        
        entityStateArray = []
        if groupKey2:
            entitiesInGroup = self.get_state(groupEntity[groupKey1][groupKey2], attribute="entity_id")
            if None == entitiesInGroup:
                self.log("entity not found. entity: %s", groupEntity[groupKey1][groupKey2], level="ERROR")
            else: 
                for entity in entitiesInGroup:
                    state = self.get_state(entity)
                    entityStateArray.append(state)
        else:
            entitiesInGroup = self.get_state(groupEntity[groupKey1], attribute="entity_id")
            if None == entitiesInGroup:
                self.log("Entity not found. entity: %s", groupEntity[groupKey1], level="ERROR")
            else:
                for entity in entitiesInGroup:
                    state = self.get_state(entity)
                    entityStateArray.append(state)
        
        return entityStateArray


    def windowsTakeAWhile(self, entity, topic, windowCurrentPosition: int, windowTargetPosition: int, openCloseTime: int) :
        command = None
        
        windowCurrentPosition = int(float(windowCurrentPosition))
        windowTargetPosition = int(float(windowTargetPosition))

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
        #windows second command (stop)
        self.create_task(asyncio.sleep(tDelta), callback=self.callbackStopEvent, topic=topic, command="stop", entity=entity, newPosition=windowTargetPosition, oldPosition=windowCurrentPosition, startTime=datetime.datetime.now().time(), tDelta=tDelta )


    def callbackStopEvent(self, kwargs):
        self.fire_event("APPDAEMON_MQTT_PUBLISH", topic=kwargs['topic'], command=kwargs['command'])
        self.set_state(kwargs['entity'], state=kwargs['newPosition'])
        
        self.log("Entity [%s] moved to a new position: %d, was: %d start time: [%s], stop time: [%s], alter [%s] seconds", kwargs['entity'], kwargs['newPosition'], kwargs['oldPosition'], kwargs['startTime'], datetime.datetime.now().time(), kwargs['tDelta'])
    

    def buildEntityDocumentByEntityName(self, entityName, toPosition, positionIncrease, positionDecrease):

        state               = self.get_state(entityName)
        topicCommand        = self.get_state(entityName, attribute="command_topic")
        entityToUpdate      = self.get_state(entityName, attribute="entityStateToUpdate")
        windowType          = self.get_state(entityName, attribute="window_type")
        windowOrientation   = self.get_state(entityName, attribute="orientation")
        
        document = {}
        document['name']            = entityName
        document['entity']          = entityToUpdate if entityToUpdate != None else entityName
        document['state']           = state
        document['topicCommand']    = topicCommand
        document['type']            = windowType
        document['orientation']     = windowOrientation

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


    def  calculateWindowFuturePosition(self, windowEntity : WindowEntity, currentPeriod: PeriodConfiguration, needToOpen, windowsMinStep ):
        self.log("Calculating current position for window: %s", windowEntity.name)

        windowCurrentPosition : int = int(float(windowEntity.currentPosition))
        windowTopMinStep : int      = int(self._getWindowTopOpenCloseTime(windowsMinStep))
        windowLowMinStep : int      = int(self._getWindowLowOpenCloseTime(windowsMinStep))
        toPosition                  = None

        if needToOpen:
            if self.isWindowTopType(windowEntity) == False:
                positionRest = float(currentPeriod.windowLowMaxOpen) - windowCurrentPosition
                if windowCurrentPosition+windowLowMinStep <= float(currentPeriod.windowLowMaxOpen):
                    toPosition = windowCurrentPosition+windowLowMinStep
                elif  positionRest < windowLowMinStep and positionRest > 0:
                    toPosition = windowCurrentPosition + positionRest
                else:
                    toPosition = windowCurrentPosition
            elif self.isWindowTopType(windowEntity):
                positionRest = float(currentPeriod.windowTopMaxOpen) - windowCurrentPosition
                if windowCurrentPosition + windowTopMinStep <= float(currentPeriod.windowTopMaxOpen):
                    toPosition = windowCurrentPosition+windowLowMinStep
                elif  positionRest < windowTopMinStep and positionRest > 0:
                    toPosition = windowCurrentPosition + positionRest
                else:
                    toPosition = windowCurrentPosition
        else:
            if self.isWindowTopType(windowEntity) == False:
                toPosition = windowCurrentPosition-(windowLowMinStep*1.5)
            elif self.isWindowTopType(windowEntity):
                toPosition = windowCurrentPosition-(windowTopMinStep*1.5)

        if toPosition < 0:
            toPosition = 0
        elif toPosition > 100: 
            toPosition = 100

        if toPosition == windowCurrentPosition:
            self.log("window %s is on max period position: [%d], nothing to do..", windowEntity.name, toPosition)
        else:    
            self.log("windowd current position %d, future position calculated: %d", windowCurrentPosition, toPosition)
        
        return toPosition


    def isWindowTopType(self, windowEntity: WindowEntity):
        windowType = windowEntity.windowType
        if windowType == WINDOW_TOP_TYPE_KEY:
            return True
        else:
            return False


    def _getWindowTopOpenCloseTime(self, openCloseTime):
        if WINDOW_TOP_TYPE_KEY in openCloseTime:
            return openCloseTime[WINDOW_TOP_TYPE_KEY]
        else:
            self.log("OpenClose parameter missing key value for %s. Returning 0 value", WINDOW_TOP_TYPE_KEY, level="ERROR")
            return 0
    

    def _getWindowLowOpenCloseTime(self, openCloseTime):
        if WINDOW_LOW_TYPE_KEY in openCloseTime:
            return openCloseTime[WINDOW_LOW_TYPE_KEY]
        else:
            self.log("OpenClose parameter missing key value for %s. Returning 0 value", WINDOW_LOW_TYPE_KEY, level="ERROR")
            return 0

    
    def _calcBackwardOrientation(self, orientation):
        compass = {
            "Nord"      : 0,
            "Nord Est"  : 45,
            "Est"       : 90,
            "Sud Est"   : 135,
            "Sud"       : 180,
            "Sud Ovest" : 225,
            "Ovest"     : 270,
            "Nord Ovest": 315, 
        }

        calcDownwind = compass[orientation] +180

        if calcDownwind > 360:
            calcDownwind = calcDownwind-360
        elif calcDownwind == 360:
            calcDownwind = 0

        for key, val in compass.items():
            if val == calcDownwind:
                return key
        
        self.log("Downwind not calculated. Please check the orientation value.. ordientation: %s", orientation, level="ERROR")
        
        return None

   
    def time_in_range(self, start, end, x):
        """Return true if x is in the range [start, end]"""
        if start <= end:
            return start <= x <= end
        else:
            return start <= x or x <= end