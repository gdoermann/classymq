from classymq.api import consumer
from djitch.amqp.lib.uuid import UUIDProducer, SyncUUIDProducer

class AMQPAPIProducer(UUIDProducer):
    CONSUMER = consumer.AMQPAPIConsumer

class SyncAMQPAPIProducer(SyncUUIDProducer):
    CONSUMER = consumer.AMQPAPIConsumer