from gpiozero import DistanceSensor
from gpiozero.pins.lgpio import LGPIOFactory
from time import sleep

sensor = DistanceSensor(
    echo=4,
    trigger=14,
    pin_factory=LGPIOFactory()
)

while True:
    distance_cm = sensor.distance * 100
    print(f"Distance: {distance_cm:.2f} cm")
    sleep(1)