import random
from tkinter import *
from paho.mqtt import client as mqtt_client
from _thread import *


broker = 'test.mosquitto.org'
port = 1883

# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'
        
    

fenetre = Tk()
fenetre.geometry("400x400")

topic = Entry(fenetre)
topic.pack()

def mqtt_thread():
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
            
            label = Label(fenetre, text = s)
            label.pack()

            print(f"Received `{s}` from `{msg.topic}` topic")
        
        client.subscribe(topic)
        client.on_message = on_message

    boutonquit = Button(fenetre, text = "quitter", command = fenetre.destroy)
    boutonquit.pack()

    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()
    
start_new_thread(mqtt_thread, ())
 



Boutonsubs = Button(fenetre, text="Subscribe", command=lambda: start_new_thread(mqtt_thread, ()))
Boutonsubs.pack()
    
def run():
    fenetre.mainloop()
  

if __name__ == '__main__':
    run()
