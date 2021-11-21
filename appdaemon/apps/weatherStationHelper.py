import mqttapi as mqtt
import requests, lxml
from bs4 import BeautifulSoup

class WeatherStationHelper(mqtt.Mqtt):
    def initialize(self):
        self.listen_event(self.manageWeatherStation, "HA_MANAGE_WEATHERSTATION")

    def manageWeatherStation(self, event_name, data, kwargs):
        #web scraping..
        url = self.args['urlObserver']
        # Make a GET request to fetch the raw HTML content
        html_content = requests.get(url).text

        soup = BeautifulSoup(html_content, "lxml")

        data_scraped = soup.find_all("input", attrs={"disabled": "disabled"})
        
        for sensor in self.args["sensors"]:
            wsEntity = self.args["sensors"][sensor]["wsentity"]
            topic = self.args["sensors"][sensor]["topic"]

            input = soup.find("input", attrs={"name": wsEntity})
            value = input.get("value")
            if sensor == "battery":
                if value == "Normal":
                    value = 100
                else:
                    value = 0
            
            self.mqtt_publish(topic, value)