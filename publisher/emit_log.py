import pika
import sys

username = 'test'
password = '123456'
credencial = pika.PlainCredentials(username=username, password=password)
connection = pika.BlockingConnection(pika.ConnectionParameters(host='172.18.1.57', port=5672, credentials=credencial))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = ''.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='logs', routing_key='', body=message)

print('[x] Sent %r' % message)
connection.close()