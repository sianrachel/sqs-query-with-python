# Python SQS Query Script (Part 2/2) 🧚‍♀️

A python script that fetches and displays items from an SQS queue.

## Requirements 🍄

### Python 🐛

| Name | Version |
|------|---------|
| [Python3](https://www.python.org/about/gettingstarted/) | >= 3.8 |
| [Pip3](https://pypi.org/project/pip/) | >= 3.48 |
| [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html) | >= 1.16 |
| [Pytest](https://docs.pytest.org/en/7.1.x/) | >= 3.48 |
| [Moto](https://pypi.org/project/moto/) | >= 3.1.17 |

`Requirements.txt` generated with:

```
pip3 freeze > requirements.txt
```

Installing requirements:

```
pip3 install -r requirements.txt
```

### AWS 🐝

- A working AWS account with Admin access that you have previously created SQS queues on using [this repo](https://github.com/sianrachel/terraform-sqs-queues), if you don't have access, please request
- [AWSCLI](https://aws.amazon.com/cli/) installed

## Listing queues 🐿️

We created our SQS queues using the config from

To call all queues created previously and get all queue names:

```
aws sqs list-queues
```

## Running as a script 🦋

Target the main file sqs_queues and specify a queue name (listing in previous step) to receive the queue url:

This is an example cmd, but you can use any queue name you have created:

```
python3 -m sqs_queues 'non-prod-test-queue-100'
```

## Running Tests 🐌

Running tests with clean verbose output:

```
pytest --no-header -vv
```
