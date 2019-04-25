import time
import paho.mqtt.client as paho
broker="169.254.15.227"
#define callback
def on_message(client, userdata, message):
    time.sleep(1)
    print("received message =",str(message.payload.decode("utf-8")))

client= paho.Client(client_id="raspberry pi")
#create client object client1.on_publish = on_publish
#assign function to callback client1.connect(broker,port)
#establish connection client1.publish("house/bulb1","on")
######Bind function to callback
client.on_message=on_message
#####
print("connecting to broker ",broker)
client.connect(broker, port=1883)#connect
client.loop_start() #start loop to process received messages
print("subscribing ")
client.subscribe("topics/positions")#subscribe
time.sleep(2)
print("publishing ")
client.publish("topics/positions","on")#publish
time.sleep(4)
client.disconnect() #disconnect
client.loop_stop() #stop loop
