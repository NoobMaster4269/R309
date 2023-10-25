import random
from tkinter import *
from paho.mqtt import client as mqtt_client
from _thread import *

broker = 'test.mosquitto.org'
port = 1883
default_topic = "/Apex"
client_id = f'python-mqtt-{random.randint(0, 100)}'

fenetre = Tk()
fenetre.geometry("400x400")

def mqtt_thread(subscribed_topic):
    def connect_mqtt() -> mqtt_client:
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("Connected to MQTT Broker!")
            else:
                print("Failed to connect, return code %d\n", rc)

        client = mqtt_client.Client(client_id)
        client.on_connect = on_connect
        client.connect(broker, port)
        return client

    def subscribe(client: mqtt_client):
        def on_message(client, userdata, msg):
            s = str(msg.payload.decode("utf-8"))
            label = Label(fenetre, text=s)
            label.pack()
            print(f"Received `{s}` from `{msg.topic}` topic")

        client.subscribe(subscribed_topic)
        client.on_message = on_message

    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()

# Champ de texte pour saisir le topic
topic_entry = Entry(fenetre)
topic_entry.insert(0, default_topic)
topic_entry.pack()

# Bouton pour s'abonner au topic spécifié
subscribe_button = Button(fenetre, text="Subscribe", command=lambda: start_new_thread(mqtt_thread, (topic_entry.get(),)))
subscribe_button.pack()

def run():
    fenetre.mainloop()

if __name__ == '__main__':
    run()