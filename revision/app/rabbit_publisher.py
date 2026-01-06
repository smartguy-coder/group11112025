

import config
import datetime
import ssl
import pika

ssl_context = ssl.create_default_context()

connection_params = pika.ConnectionParameters(
    host=config.RMQ_HOST,
    port=config.RMQ_PORT,
    virtual_host=config.RMQ_VIRTUAL_HOST,
    credentials=pika.PlainCredentials(username=config.RMQ_USER, password=config.RMQ_PASSWORD),
    ssl_options=pika.SSLOptions(context=ssl_context),
)


def get_connection() -> pika.BlockingConnection:
    return pika.BlockingConnection(parameters=connection_params)


def produce_message(channel: pika.adapters.blocking_connection.BlockingChannel):
    QUEUE = 'weather'
    channel.queue_declare(queue=QUEUE)

    message = 'hello kitty )))) {item}'
    for item in range(20):
        body = message.format(item=item)
        channel.basic_publish(
            exchange='',
            routing_key=QUEUE,
            body=body
        )
        print(body)


def main():
    with get_connection() as connection:
        with connection.channel() as channel:
            produce_message(channel)


if __name__ == "__main__":
    main()
