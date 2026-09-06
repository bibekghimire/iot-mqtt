import paho.mqtt.client as mqtt

# Called when connection succeeds
def on_connect(client, userdata, flags, rc):
    print("Connected to broker")

    # Subscribe to topic
    client.subscribe("test/topic")

# Called when message is received
def on_message(client, userdata, msg):
    print(f"Received: {msg.payload.decode()}")

# Create client
client = mqtt.Client()

# Attach callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to broker
client.connect("192.168.1.68", 1883, 60)

# Infinite loop waiting for messages
client.loop_forever()