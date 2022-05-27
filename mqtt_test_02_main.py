import paho.mqtt.client as mqtt
import json
import time
import os
import random
import threading
import datetime
import sys
sys.path.append("..")
# from . import mqtt_test_01_main as a

# a.mqttdemo01.mqttclientdemo()

class mqttdemo02():
    def mqttclient_local(self):
        # HOST = "192.9.230.253"
        # HOST="192.9.230.27"
        HOST="127.0.0.1"
        PORT = 1883
        client_id = "1083421xxxx"                       # 没有就不写，此处部分内容用xxx代替原内容，下同

        HOST="192.9.250.94"
        PORT = 2031
        client_id = "10834216636"                       # 没有就不写，此处部分内容用xxx代替原内容，下同

        HOST2="10.1.48.34"
        PORT2 = 1883
        client_id2 = "10834218848"                       # 没有就不写，此处部分内容用xxx代替原内容，下同

        def on_connect(client, userdata, flags, rc):
            print("local")
            print("Connected with result code "+str(rc))
            #client.subscribe("testmq")         # 订阅消息，字符串内容为订阅主题名字


        def on_message(client, userdata, msg):
            print("主题:"+msg.topic+" 消息:"+str(msg.payload.decode('utf-8')))


        def on_subscribe(client, userdata, mid, granted_qos):
            print("On Subscribed: qos = %d" % granted_qos)


        def on_disconnect(client, userdata, rc):
            if rc != 0:
                print("Unexpected disconnection %s" % rc)

        def on_connect2(client, userdata, flags, rc):
            print("internet")
            print("Connected with result code "+str(rc))
            client.subscribe("MYMQTT",qos=0)         # 订阅消息，字符串内容为订阅主题名字


        def on_message2(client, userdata, msg):
            print("主题:"+msg.topic+" 消息:"+str(msg.payload.decode('utf-8')))
            strtrans_pass01=str(msg.payload.decode('utf-8'))
            strtrans_pass02=strtrans_pass01.split("'",6)
            strtrans_pass03=strtrans_pass02[3].split("`",7)
            timeset=time.time()
            #timesetstr=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timeset))
            data_msg={"shebei_num":"004-166","time":strtrans_pass02[5],"time2":timeset,"data":{"SP1_speed":strtrans_pass03[0],"SP1_load":strtrans_pass03[1],"X10_load":strtrans_pass03[2],"Y10_load":strtrans_pass03[3],"Z10_load":strtrans_pass03[4],"B_load":strtrans_pass03[5],"B_speed":strtrans_pass03[6]}}
            param_msg=json.dumps(data_msg)
            #client1.publish("smec/send",payload=param_msg,qos=0)
            #client1.publish("smec/send2", payload=param_msg, qos=0)

        def on_subscribe2(client, userdata, mid, granted_qos):
            print("On Subscribed: qos = %d" % granted_qos)


        def on_disconnect2(client, userdata, rc):
            if rc != 0:
                print("Unexpected disconnection %s" % rc)



        data = {
            "type":2,
            "timestamp": time.time(),
            "messageId":"9fcda359-89f5-4933-xxxx",  #最后四位xxxx
            "command":"/recommend",
            "data":{
                "openId":"xxxx",
                "appId":"xxxx",
                "recommendType":"temRecommend"
            }
        }
        param = json.dumps(data)
        client1 = mqtt.Client(client_id)
        client2 = mqtt.Client(client_id2)
        #client1.username_pw_set("xxxx", "xxxx")
        client1.username_pw_set("smectest", "test")
        client2.username_pw_set("Linus", "abcde.12345")
        client1.on_connect = on_connect
        client1.on_message = on_message
        client1.on_subscribe = on_subscribe
        client1.on_disconnect = on_disconnect
        client2.on_connect = on_connect2
        client2.on_message = on_message2
        client2.on_subscribe = on_subscribe2
        client2.on_disconnect = on_disconnect2
        client1.connect(HOST, PORT, 60)
        client2.connect(HOST2, PORT2, 60)
        #client1.publish("smec/send", payload=param, qos=0)     # 发送消息
        client1.loop_start()
        client2.loop_start()



def run1(obj):
    t1=threading.Thread(daemon=True,target=mqttdemo02.mqttclient_local(obj))
    t1.start()
    print("t1start")

def run2(obj):
    t2=threading.Thread(daemon=True,target=mqttdemo02.mqttclient_hezi(obj))
    t2.start()
    print("t2start")

if __name__ == '__main__':
    a=time.time()
    print(str(a))
    objnew=mqttdemo02
    # objnew2=mqttdemo01
    file=open("D:\\python test\\SCADAtest01\\输出存放\\DZ18004185T6\\0_控制.txt","r")
    panduan=file.read()
    #run2(objnew2)
    run1(objnew)
    while panduan!="0":
        print("start:"+str(datetime.datetime.now()))
        # run2(objnew2)
        panduan=file.read()
        time.sleep(600)
    file.close()
    print("finish")