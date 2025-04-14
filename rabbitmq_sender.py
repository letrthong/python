# 
# sudo apt-get install rabbitmq-server
# pip install pika

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare an exchange
channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

# Send a message with a routing key
severity = 'info'
message = 'This is an info message.'
channel.basic_publish(exchange='direct_logs', routing_key=severity, body=message)
print(f" [x] Sent {severity}: {message}")

connection.close()
