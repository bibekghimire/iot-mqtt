import paho.mqtt.client as mqtt
import time
import psutil

import board
import adafruit_dht

#DHT 22 initialization
dht_device1 = adafruit_dht.DHT22(board.D4)


def read_tmp_hum(dht_device):
    try:
        temperature = dht_device.temperature
        humidity = dht_device.humidity
        return (temperature, humidity)
    except RuntimeError as error:
        # DHT sensors occasionally return temporary errors
        print(f"Reading error: {error}")
        return 0.0,0.0


# Create MQTT client object
client = mqtt.Client()

# Connect to broker
client.connect("192.168.1.68", 1883, 60)

while True:
    # Publish message
    tmp, hum = read_tmp_hum(dht_device1)    
    message = f", GUMIT!!! published : \n Temperature{tmp} \n humidity: {hum} \n"
    client.publish("gumit/dht/1/temp", tmp)
    client.publish("gumit/dht/1/humidity", hum)

    print(f"Published: {message}")
    # temps = psutil.sensors_temperatures()
    time.sleep(2)
