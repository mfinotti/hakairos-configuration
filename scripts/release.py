import sys
import paho.mqtt.publish as publish

auth_data               = {}
auth_data["username"]   = "mqtt_kairos"
auth_data["password"]   = "kairos!"

sw      = sys.argv[1]
version = sys.argv[2]
publish.single("kairostech/"+sw+"/version", version, hostname="localhost", port=1884, auth=auth_data, retain=True)