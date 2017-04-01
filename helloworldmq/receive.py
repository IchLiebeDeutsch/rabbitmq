import pika
username = 'test'
password = '123456'
credencial = pika.PlainCredentials(username=username, password=password)
connection = pika.BlockingConnection(pika.ConnectionParameters(host='172.18.1.57', port=5672, credentials=credencial))
channel = connection.channel()

channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print("[x] Received %r" % body)

channel.basic_consume(callback, queue='hello', no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
