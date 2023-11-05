import random
import time
from paho.mqtt import client as mqtt_client

topic = input('Nom du topic:')
port = int(input('Numero du port : '))
broker = input('Broker :')

# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
#Creer une connexion MQTT
def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connecté au Broker MQTT!")
        else:
            print("Connexion échouée, code de retour%d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish(client, topic):
    while True:
        time.sleep(1)
        msg = input(f'{topic}>')
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result.rc
        #Verifie si code de retour est égale à 0
        if status == mqtt_client.MQTT_ERR_SUCCESS:
            print(f"Envoie du `{msg}` au topic `{topic}` du client {client_id}")
            client.publish(msg)
        else:
            print(f"Echec de l'envoie du message au topic {topic}")


#Appelle les fonctions
def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client, topic)

#
if __name__ == '__main__':
        run()