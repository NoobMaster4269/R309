import random
from tkinter import *
from paho.mqtt import client as mqtt_client
from _thread import *
import time


date = time.strftime('%H:%M:%S', time.localtime())
broker = 'test.mosquitto.org'


# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'
        
    
fenetre = Tk()
fenetre.geometry("500x400")

frame = Frame(fenetre)
frame.pack(padx = 10, pady = 10)

label = Label(frame, text = "Nom du topic :")
label.grid(row = 0, column = 0, padx = 5)

topictk = Entry(frame)
topictk.grid(row = 1, column = 0, padx = 5)

label2 = Label(frame, text = "Port :")
label2.grid(row = 0, column = 1, padx = 5)

porttk = Entry(frame)
porttk.grid(row = 1, column = 1)

Boutonsubs = Button(frame, text ="S'abonner", command=lambda: start_new_thread(mqtt_thread, ()))
Boutonsubs.grid(row = 2, column = 0, padx = 5, pady = 5)

boutonquit = Button(frame, text = "quitter", command = fenetre.destroy)
boutonquit.grid(row = 0, column = 2, padx = 5)

text = Text(frame, width = 60, height = 5)
text.grid(row = 3, column = 0, columnspan = 3, padx = 5)



def mqtt_thread():
    global topic
    global port
    topic = topictk.get()
    port = porttk.get()
    port = int(porttk.get())
        

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


        frame2 = Frame(fenetre)
        frame2.pack(padx = 10, pady = 10)



        mes = Entry(frame2)
        mes.grid(row = 0, column = 0, padx = 5)

        def message():
            client.publish(topic, mes.get())
            mes.delete(0, END)
        
        Boutonsmsg = Button(frame2, text = "Envoyer msg", command = message)
        Boutonsmsg.grid(row = 1, column= 0, padx = 5, pady = 5)

        def decotopic():
            client.disconnect()
            porttk.delete(0, END)
            topictk.delete(0, END)

        Boutonsmsg = Button(frame, text = "Deconnexion du topic", command = decotopic)
        Boutonsmsg.grid(row = 1, column= 2, padx = 5, pady = 5)

        def enregisterlog():
            f = open("Log.txt", "w")
            f.write(text.get("1.0", "end"))

        Boutonsmsg = Button(frame, text = "Enregister", command = enregisterlog)
        Boutonsmsg.grid(row = 4, column= 0, padx = 5, pady = 5)

    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()
        

    

def run():
    fenetre.mainloop()
    fenetre.update()
  

if __name__ == '__main__':
    run()
