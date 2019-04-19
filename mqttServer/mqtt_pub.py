import paho.mqtt.publish as publish
import time

auth = {'username':"afevtheu", 'password':"rdr2nR0R7W4e"}

for i in range(5):
    publish.single("Positions", "X Position:  " + str(5*1 + 1), auth=auth, hostname="m16.cloudmqtt.com", port=13945)
    print("msg %d sent", i)
    time.sleep(10)


