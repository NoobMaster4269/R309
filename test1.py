import random
import time
from _thread import *
from paho.mqtt import client as mqtt_client

broker = 'test.mosquitto.org'
port = 1883
client_id = f'python-mqtt-{random.randint(0, 1000)}'

def mqtt_thread():
    def connect_mqtt() -> mqtt_client:
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("Connected to MQTT Broker!")
            else:
                print(f"Failed to connect, return code {rc}")

        client = mqtt_client.Client(client_id)
        client.on_connect = on_connect
        client.connect(broker, port)
        return client

    def publish(client, topic):
        while True:
            time.sleep(1)
            msg = input('')
            result = client.publish(topic, msg)
            status = result.rc
            if status == mqtt_client.MQTT_ERR_SUCCESS:
                print(f"Send `{msg}` to topic `{topic}`")
            else:
                print(f"Failed to send message to topic {topic}")

    client = connect_mqtt()
    client.loop_start()

    # Demander le topic auquel publier
    topic = input('Enter the topic to publish to: ')

    publish(client, topic)

start_new_thread(mqtt_thread, ())

if __name__ == '__main__':
    while True:
        pass
