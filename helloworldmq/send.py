import pika
username = 'test'
password = '123456'
credencial = pika.PlainCredentials(username=username, password=password)
connection = pika.BlockingConnection(pika.ConnectionParameters(host='172.18.1.57', port=5672, credentials=credencial))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
print("[x] Sent 'Hello World!")

connection.close()