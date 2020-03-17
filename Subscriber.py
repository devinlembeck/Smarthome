import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe


class Subscribe:
    def __init__(self, topic, ip_address):
        self.ip = ip_address
        self.topic = topic
        self.client = None

    def client_setup(self):
        self.client = mqtt.Client()
        self.client.on_message = self.on_message
        self.client.on_connect = self.on_connect

        self.client.connect(self.ip)

        self.client.loop_forever()

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code" + str(rc))

        self.client.subscribe(self.topic)

    def on_message(self, client, userdata, msg):
        print(msg.topic + " " + str(msg.payload))

    def get_single_message(self):
        msg = subscribe.simple(self.topic, hostname=self.ip)
        return msg.payload


