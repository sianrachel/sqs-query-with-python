import boto3
import pytest
import os
from moto import mock_sqs
from sqs_queues import SqsQueues as Queues

REGION='eu-west-1'
BASE_URL = 'https://eu-west-1.queue.amazonaws.com/123456789012/'
TEST_QUEUE_1 = 'test-queue-1'
TEST_QUEUE_2 = 'test-queue-2'
TEST_MESSAGE_1 = 'This is your first test message'
TEST_MESSAGE_2 = 'This is your second test message'

@pytest.fixture(scope='function')
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ['AWS_ACCESS_KEY_ID'] = 'mock_access_key_id'
    os.environ['AWS_SECRET_ACCESS_KEY'] = 'mock_secret_access_key'

@pytest.fixture(scope='function')
def sqs_client(aws_credentials):
    with mock_sqs():
        yield boto3.client('sqs', region_name=REGION)

def test_get_queue_url(sqs_client):
    instance = Queues()
    sqs_client.create_queue(QueueName=TEST_QUEUE_1)
    response = instance.get_queue_url(TEST_QUEUE_1)
    assert TEST_QUEUE_1 in response
    assert TEST_QUEUE_2 not in response

def test_get_queue_message_count(sqs_client):
    instance = Queues()
    sqs_client.create_queue(QueueName=TEST_QUEUE_2)
    sqs_client.send_message(QueueUrl = BASE_URL + TEST_QUEUE_2, MessageBody = TEST_MESSAGE_2)
    count = instance.get_queue_message_count(BASE_URL + TEST_QUEUE_2)
    assert count == 1