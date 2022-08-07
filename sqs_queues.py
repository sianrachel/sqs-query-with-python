import boto3

class SqsQueues:
    def __init__(self):
        self.client = boto3.client("sqs", "eu-west-1")

    def get_queue_url(self, name):
        try:
            return self.client.get_queue_url(QueueName=name)['QueueUrl']
        except BaseException as err:
            print("One or more queues provided do not exist. Please try again.")