import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import time



client = mqtt.Client(client_id="Pi")
client.connect("169.254.140.49", port=1883)

msg = "34"
for i in range(5):
    client.publish("topics/positions","34")
    print("Message sent")
    time.sleep(1)
