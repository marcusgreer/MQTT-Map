import paho.mqtt.subscribe as subscribe
import paho.mqtt.client as mqtt

auth = {'username':"afevtheu", 'password':"rdr2nR0R7W4e"}

client = mqtt.Client(client_id="DraNard")
client.username_pw_set("afevtheu", "rdr2nR0R7W4e")
client.connect()


callback()

msg = subscribe.simple("Positions", hostname="m16.cloudmqtt.com", auth=auth, port=13945)
print("%s %s" % (msg.topic, msg.payload))