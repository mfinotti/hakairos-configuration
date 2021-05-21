import sqlite3
import json
from datetime import datetime
import paho.mqtt.publish as publish


logfile                 = open("metrics-entity.log","a+")

start_timestamp         = datetime.now()

logfile.write("\n#### Started entityMetrics script at "+str(start_timestamp))

mqtt_host               = "localhost"

authParams              = {}
authParams['username']  = "mqtt_kairos"
authParams['password']  = "kairos!"

metricsName             = "ENTITY_METRICS_COLLECTION"
metricsTopic            = "metrics/entities"
con                     = sqlite3.connect('home-assistant_v2.db')
cur                     = con.cursor()

cur.execute('SELECT CAST(state AS INTEGER) FROM states WHERE state != "unknown" AND entity_id = "input_number.metrics_frequency" ORDER BY last_updated DESC LIMIT 1')
frequency               = cur.fetchone()[0]

queryFrequencyString    = "-"+str(frequency)+" hour"
cur.execute('SELECT * FROM states WHERE entity_id = "group.entity_metrics" ORDER BY last_updated DESC LIMIT 1')

for row in cur.fetchall():
    try:
    
        entities = json.loads(row[4])
        logfile.write("\nfound ["+ str(len(entities['entity_id'])) +"] entities in group.entity_metrics")
        message                     = {}
        message['id']               = metricsName
        metrics                     = []
        for entity in entities['entity_id']:
            cur.execute("SELECT CAST(AVG(state) AS INTEGER), attributes FROM states WHERE state != 'unknown' AND entity_id = '"+ entity +"' AND last_updated >= DATETIME('now', '"+queryFrequencyString+"')")
            rowData                 = cur.fetchone()
            if None != rowData and None != rowData[0]:
                avg                     = rowData[0]
                attributes              = json.loads(rowData[1])
                avgModel                = {}
                avgModel['entity_id']   = entity
                avgModel['state']       = avg
                avgModel['type']        = attributes["device_class"] if "device_class" in attributes else "value"

                metrics.append(avgModel)

        logfile.write("\nMetrics collected: "+ str(metrics))
        message['data'] = metrics
        publish.single(metricsTopic, str(message), hostname=mqtt_host, auth=authParams)
    
    except Exception as e:
        logfile.write("Error: "+e)    


end_timestamp = datetime.now()
logfile.write("\n#### Ended entityMetrics script at "+str(end_timestamp))

con.close()
logfile.close()
