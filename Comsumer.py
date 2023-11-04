import random
from tkinter import *
from paho.mqtt import client as mqtt_client
from _thread import *
import time
from tkinter import ttk

#  test.mosquitto.org  

date = time.strftime('%H:%M:%S', time.localtime())
clients = []
  
fenetre = Tk()
fenetre.geometry("600x400")

tabControl = ttk.Notebook(fenetre)

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

label3 = Label(frame, text = "Broker :")
label3.grid(row = 0, column = 2, padx = 5)

brokertk = Entry(frame)
brokertk.grid(row = 1, column = 2, padx = 5)

Boutonsubs = Button(frame, text ="S'abonner", command=lambda: start_new_thread(mqtt_thread, ()))
Boutonsubs.grid(row = 2, column = 1, padx = 5, pady = 5)

boutonquit = Button(frame, text = "quitter", command = fenetre.destroy)
boutonquit.grid(row = 1, column = 3, padx = 10)



def mqtt_thread():
    global topic, port 
    topic = topictk.get()
    broker = brokertk.get()
    port = porttk.get()
    port = int(porttk.get())
    # generate client ID with pub prefix randomly
    client_id = f'python-mqtt-{random.randint(0, 100)}'

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

        tab1 = ttk.Frame(tabControl)
        tabControl.add(tab1, text = topic)
        tabControl.pack(expand = 1, fill ="both")

        label4 = Label(frame, text = "Envoyer un message :")
        label4.grid(row = 3, column = 1, pady = 5)

        label5 = Label(frame, text = "Topic du message:")
        label5.grid(row = 3, column = 0, pady = 5)

        mes = Entry(frame)
        mes.grid(row = 4, column = 1, padx = 5)

        topicmes = Entry(frame)
        topicmes.grid(row = 4, column = 0, padx = 5)

   
        def message():
            client.publish(topicmes.get(), mes.get())
            mes.delete(0, END)

        Boutonsmsg = Button(frame, text = "Envoyer", command = message)
        Boutonsmsg.grid(row = 4, column= 2, padx = 5, pady = 5)

        text = Text(tab1, width = 70, height = 7)
        text.grid(row = 3, column = 0, columnspan = 4, padx = 5, pady = 5)

        def enregisterlog():
            f = open("Log.txt", "a")
            f.write(text.get("1.0", "end"))

        Boutonsenreg = Button(tab1, text = "Enregister", command = enregisterlog)
        Boutonsenreg.grid(row = 4, column= 0, padx = 5, pady = 5)

    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()
    clients.append(client)

  
    

def run():
    fenetre.mainloop()
    fenetre.update()
  

if __name__ == '__main__':
    run()
