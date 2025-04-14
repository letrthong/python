import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare an exchange
channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

# Declare a queue
queue_name = channel.queue_declare(queue='', exclusive=True).method.queue

# Bind the queue to the exchange with a routing key
severity = 'info'
channel.queue_bind(exchange='direct_logs', queue=queue_name, routing_key=severity)

print(' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(f" [x] Received {body}")

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
channel.start_consuming()
