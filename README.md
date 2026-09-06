# iot-mqtt
for mqtt protocol, working with mosquitto service. 

RPI PINS (26 PIN)

# Raspberry Pi 26-Pin GPIO Pinout

| Physical Pin | BCM GPIO | Function / Signal | Physical Pin | Function / Signal | BCM GPIO |
|:------------:|:--------:|-------------------|:------------:|-------------------|:--------:|
| 1 | — | 3.3V Power | 2 | 5V Power | — |
| 3 | GPIO 2 | SDA (I2C) | 4 | 5V Power | — |
| 5 | GPIO 3 | SCL (I2C) | 6 | Ground (GND) | — |
| 7 | GPIO 4 | GPIO / GPCLK0 | 8 | UART TXD | GPIO 14 |
| 9 | — | Ground (GND) | 10 | UART RXD | GPIO 15 |
| 11 | GPIO 17 | GPIO | 12 | PWM0 / GPIO | GPIO 18 |
| 13 | GPIO 27 | GPIO | 14 | Ground (GND) | — |
| 15 | GPIO 22 | GPIO | 16 | GPIO | GPIO 23 |
| 17 | — | 3.3V Power | 18 | GPIO | GPIO 24 |
| 19 | GPIO 10 | MOSI (SPI) | 20 | Ground (GND) | — |
| 21 | GPIO 9 | MISO (SPI) | 22 | GPIO | GPIO 25 |
| 23 | GPIO 11 | SCLK (SPI) | 24 | SPI CE0 | GPIO 8 |
| 25 | — | Ground (GND) | 26 | SPI CE1 | GPIO 7 |

## visual representation 


| Left Pin Name | Left Pin (#) | Pin Layout | Right Pin (#) | Right Pin Name |
| :--- | :---: | :---: | :---: | :--- |
| **3.3V** | 1 | ● ● | 2 | **5V** |
| **GPIO2 / SDA** | 3 | ● ● | 4 | **5V** |
| **GPIO3 / SCL** | 5 | ● ● | 6 | **GND** |
| **GPIO4** | 7 | ● ● | 8 | **GPIO14 / TXD** |
| **GND** | 9 | ● ● | 10 | **GPIO15 / RXD** |
| **GPIO17** | 11 | ● ● | 12 | **GPIO18 / PWM** |
| **GPIO27** | 13 | ● ● | 14 | **GND** |
| **GPIO22** | 15 | ● ● | 16 | **GPIO23** |
| **3.3V** | 17 | ● ● | 18 | **GPIO24** |
| **GPIO10 / MOSI** | 19 | ● ● | 20 | **GND** |
| **GPIO9 / MISO** | 21 | ● ● | 22 | **GPIO25** |
| **GPIO11 / SCLK** | 23 | ● ● | 24 | **GPIO8 / CE0** |
| **GND** | 25 | ● ● | 26 | **GPIO7 / CE1** |

### simple program

Here is a simple Python program to read temperature and humidity from a DHT22 sensor using Raspberry Pi GPIO.