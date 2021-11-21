import sqlite3
import json
from datetime import datetime
import paho.mqtt.publish as publish

from requests import get


logfile                 = open("metrics-system.log","a+")

start_timestamp         = datetime.now()

logfile.write("\n#### Started systemMetrics script at "+str(start_timestamp))

mqtt_host               = "localhost"

authParams              = {}
authParams['username']  = "mqtt_kairos"
authParams['password']  = "kairos!"

metricsName             = "SYSTEM_METRICS_COLLECTION"
metricsTopic            = "metrics/system"

message                 = {}
message['id']           = metricsName
metrics                 = []

### PUBLIC IP 
ip = get('https://api.ipify.org').text

model                   = {}
model['entity_id']      = "system.ip"
model['state']          = ip

#add to message metric's
metrics.append(model)
message['data'] = metrics

logfile.write("\nMetrics collected: "+ str(metrics))
publish.single(metricsTopic, str(message), hostname=mqtt_host, auth=authParams)


end_timestamp = datetime.now()
logfile.write("\n#### Ended systemMetrics script at "+str(end_timestamp))

logfile.close()
