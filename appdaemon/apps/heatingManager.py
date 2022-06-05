import hassapi as hass

class HeatingManager(hass.Hass):

    def initialize(self):
        self.listen_event(self.manageHeating, "HA_MANAGE_HEATER")

    def manageHeating(self, event_name, data, kwargs):
        
        event = data.get('event')
        self.log("Event name: %s", event)