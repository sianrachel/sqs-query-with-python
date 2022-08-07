import boto3
import json
import pprint

pp = pprint.PrettyPrinter(indent=4)

class SqsQueues:
    def __init__(self):
        self.client = boto3.client("sqs", "eu-west-1")

    def get_queue_url(self, name):
        try:
            return self.client.get_queue_url(QueueName=name)['QueueUrl']
        except BaseException as err:
            print("One or more queues provided do not exist. Please try again.")

    def get_queue_message_count(self,target_url):
        attrs = 'ApproximateNumberOfMessages'
        count = self.client.get_queue_attributes(QueueUrl=target_url, AttributeNames=[attrs])['Attributes'].get(attrs)
        return int(count)

    def get_queues_message_totals(self,queues):
        response = []
        for queue in queues:
            url = self.get_queue_url(queue)
            dlq = url + '-dlq'
            standard_count = self.get_queue_message_count(url)
            dead_letter_count = self.get_queue_message_count(dlq)
            response.append({'standard_queue_url': url,
                            'dead_letter_queue_url': dlq,
                            'standard_queue_message_count': standard_count,
                            'dead_letter_queue_message_count': dead_letter_count
                            })
        pp.pprint(response)
        return response
        
if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        instance = SqsQueues()
        instance.get_queues_message_totals(sys.argv[1:])
    else:
        print('Please specify at least one queue name!')