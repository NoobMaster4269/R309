import random
import time
from _thread import * 
from paho.mqtt import client as mqtt_client






# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'

def mqtt_thread():
    def connect_mqtt():
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("Connected to MQTT Broker!")
            else:
                print("Failed to connect, return code %d\n", rc)

        client = mqtt_client.Client(client_id)
        client.on_connect = on_connect
        client.connect(broker, port)
        return client


    def publish(client, topic):
        while True:
            time.sleep(1)
    
            msg = input('')
            result = client.publish(topic, msg)
            # result: [0, 1]
            status = result.rc
            if status == mqtt_client.MQTT_ERR_SUCCESS:
                print(f"Send `{msg}` to topic `{topic}`")
                client.publish(msg)
            else:
                print(f"Failed to send message to topic {topic}")

    topic = input('Nom du topic:')
    port = int(input('Numero du port : '))
    broker = input('Broker :')
    client = connect_mqtt()
    client.loop_start()
    publish(client, topic)

start_new_thread(mqtt_thread, ())


if __name__ == '__main__':
    while True:
        pass
