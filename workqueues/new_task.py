import sys
import pika
username = 'test'
password = '123456'
message = ' '.join(sys.argv[1:]) or 'Hello World!'
credencial = pika.PlainCredentials(username=username, password=password)
connection = pika.BlockingConnection(pika.ConnectionParameters(host='172.18.1.57', port=5672, credentials=credencial))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

channel.basic_publish(exchange='', routing_key='task_queue', body=message, properties=pika.BasicProperties(delivery_mode=2))

print("[x] Sent %r" % message)

connection.close()