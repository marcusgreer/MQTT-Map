import subprocess
import os
import time
import pexpect
import paho.mqtt.client as mqtt
import sys
import struct

btID = 'E0:41:9E:C5:08:B7'

print('start')
child = pexpect.spawn('gatttool -I')

print('connecting to ')
print(btID)
child.sendline('connect {0}'.format(btID))
child.expect('Connection successful', timeout=20)
print('connected!')

child.sendline('char-read-hnd 0x0034')
child.expect('Characteristic value/descriptor: ', timeout=10)
child.expect('\r\n', timeout=10)
#child.sendline('disconnect')
print('data: ')
print(child.before)

message = child.before

#print(message)

bytes = int.from_bytes(message, byteorder='big', signed = True)

print(type(message))
xCoord = message[12:23]
yCoord = message[24:35]
zCoord = message[36:47]
print('X: ')
print(xCoord)
print('Y: ')
print(yCoord)
print('Z: ')
print(zCoord)

realX = int.from_bytes(xCoord, byteorder='big', signed = True)
print('real x: ')
print(realX)
realY = int.from_bytes(yCoord, byteorder='big', signed = True)
print('real y: ')
print(realY)
realZ = int.from_bytes(zCoord, byteorder='big', signed = True)
print('real z: ')
print(realZ)

#print(type(realX))

# auth = {'username':"afevtheu", 'password':"rdr2nR0R7W4e"}
#publish.single("example","X: " + str(realX), hostname="m16.cloudmqtt.com", port=13945, auth=auth)
#publish.single(realY, auth=auth, hostname="m16.cloudmqtt.com", port=13945)
#publish.single(realZ, auth=auth, hostname="m16.cloudmqtt.com", port=13945)

#quit()
client = mqtt.Client(client_id="RPi")
client.connect("169.254.140.49", port=1883)


client.publish("topics/positions", "34")
client.disconnect()
