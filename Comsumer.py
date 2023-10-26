import random
from tkinter import *
from paho.mqtt import client as mqtt_client
from _thread import *
import time


date = time.strftime('%H:%M:%S', time.localtime())
broker = 'test.mosquitto.org'
port = 1883

# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'
        
    
fenetre = Tk()
fenetre.geometry("400x400")

topictk = Entry(fenetre)
topictk.pack()


Boutonsubs = Button(fenetre, text ="S'abonner", command=lambda: start_new_thread(mqtt_thread, ()))
Boutonsubs.pack()

boutonquit = Button(fenetre, text = "quitter", command = fenetre.destroy)
boutonquit.pack()

#msg = Entry(fenetre)
#msg.pack()


text = Text(fenetre, width = 400, height = 150)
text.pack()

#Boutonsmsg = Button(fenetre, text = "Envoyer msg", command = Message)
#Boutonsmsg.pack()   
#def Message():
 #   client.publish(msg.get())
  #  text.insert(INSERT, msg.topic + " " + "|" + " " + date + " " + "|" + " "  + msg.get() + "\n")
    

def mqtt_thread():
    global topic
    topic = topictk.get()
    topictk.delete(0, END)


    def connect_mqtt() -> mqtt_client:
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("Connecté au Broker MQTT !")
            else:
                print("Connexion échouée, code %d\n", rc)

        client = mqtt_client.Client(client_id)
        client.on_connect = on_connect
        client.connect(broker, port)
        return client


    def subscribe(client: mqtt_client):
        def on_message(client, userdata, msg):
            s = str(msg.payload.decode("utf-8"))
            print(f"Reçoi `{s}` du topic  `{msg.topic}`")
            text.insert(INSERT, msg.topic + " " + "|" + " " + date + " " + "|" + " "  + s + "\n")


        client.subscribe(topic)
        client.on_message = on_message

    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()
        

def run():
    fenetre.mainloop()
  

if __name__ == '__main__':
    run()
