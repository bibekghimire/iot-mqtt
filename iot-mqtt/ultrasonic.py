from gpiozero import DistanceSensor
from gpiozero.pins.lgpio import LGPIOFactory
from time import sleep

import paho.mqtt.client as mqtt
import time
import psutil

## mqtt publisher
client = mqtt.Client()
client.connect("bibek.local", 1883, 60)


sensor = DistanceSensor(
    echo=4,
    trigger=14,
    pin_factory=LGPIOFactory()
)

while True:
    
    distance_cm = sensor.distance * 100
    message=f"distance: {distance_cm}"
    client.publish("ultrasonic/1",distance_cm)
    print(f"Distance: {distance_cm:.2f} cm")
    sleep(1)