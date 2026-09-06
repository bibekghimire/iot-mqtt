import paho.mqtt.client as mqtt
import time
import psutil


# Create MQTT client object
client = mqtt.Client()

# Connect to broker
client.connect("192.168.1.68", 1883, 60)

count = 1

while True:
    message = f"Hello MQTT {count}"

    # Publish message
    client.publish("test/topic", message)

    print(f"Published: {message}")
    # temps = psutil.sensors_temperatures()
    # print(f"Temperature: {temps}")
    count += 1

    time.sleep(2)
