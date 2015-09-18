
import time
import RPi.GPIO as g
import paho.mqtt.client as mqtt

def on_connect(client, userdata, rc):
        print('connected with result_code: ' + str(rc))
        client.subscribe('jmh/0')

def on_message(client,userdata,msg):
        print 'topic: ', msg.topic+'\nMessage:'+str(msg.payload)
        g.setwarnings(False)
        g.setmode(g.BOARD)
        g.setup(15,g.OUT)
        if str(msg.payload)=='on':
                print 'on ' + (time.strftime("%d/%m/%Y %H:%M:%S"))
                g.output(15,True)
        if str(msg.payload)=='off':
                print 'off ' + (time.strftime("%d/%m/%Y %H:%M:%S"))
                g.output(15,False)


client=mqtt.Client()
client.on_connect=on_connect
client.on_message=on_message
client.connect('test.mosquitto.org',1883,60)
client.loop_forever()
import RPi.GPIO as g
import paho.mqtt.client as mqtt

def on_connect(client, userdata, rc):
        print('connected with result_code: ' + str(rc))
        client.subscribe('jmh/0')

def on_message(client,userdata,msg):
        print 'topic: ', msg.topic+'\nMessage:'+str(msg.payload)
        g.setwarnings(False)
        g.setmode(g.BOARD)
        g.setup(15,g.OUT)
        g.output(15,True)

client=mqtt.Client()
client.on_connect=on_connect
client.on_message=on_message
client.connect('test.mosquitto.org',1883,60)
client.loop_forever()
