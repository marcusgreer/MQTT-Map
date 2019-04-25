import paho.mqtt.subscribe as subscribe
import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)

#auth = {'username':"afevtheu", 'password':"rdr2nR0R7W4e"}

client = mqtt.Client(client_id="DraNard")
#client.username_pw_set("afevtheu", "rdr2nR0R7W4e")
client.on_message=on_message #attach function to callback
client.connect("localhost", port=1883)
client.subscribe("topics/positions")
client.loop_start()
time.sleep(60)
client.loop_stop()
