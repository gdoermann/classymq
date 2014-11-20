#!/usr/bin/env python
from twisted.internet.defer import inlineCallbacks
from uuid import uuid1
from classymq.tests import base
from twisted.internet import reactor, defer
from classymq.api import consumer, producer, common

__author__ = 'gdoermann'

class BaseTestMessage(common.AMQPAPIRequest):
    pass

class TestMessageType1(BaseTestMessage):
    pass

class TestMessageType2(BaseTestMessage):
    pass

class TestAPIExchange(common.AMQPAPIExchange):
    KEY = "test-amqpapi"


class TestAMQPAPIQueue(common.AMQPAPIQueue):
    KEY = "test-amqpapi-%(prefix)s-%(uuid)s"


class TestAPIConsumer(consumer.AMQPAPIConsumer):
    EXCHANGE = TestAPIExchange
    QUEUE = TestAMQPAPIQueue
    MESSAGE_CLASS = BaseTestMessage

class TestAPIProducer(producer.AMQPAPIProducer):
    CONSUMER = TestAPIConsumer


class ApiTest(base.ClassyTestCase):

    @inlineCallbacks
    def test_connection(self):
        defer_until_received = defer.Deferred()
        def message_received(msg):
            raise msg

        yield self.defer_until_connected
        consumer = TestAPIConsumer(uuid=str(uuid1()), prefix='tester')
        consumer.processor.register(message_received)
        self.connection.read(consumer)

        producer = TestAPIProducer(self.connection)
        msg = TestMessageType1(message='hello world')
        producer.push(msg)
        yield defer_until_received

        raise Exception('Reactor is not running!')

