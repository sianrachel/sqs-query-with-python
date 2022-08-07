# Python SQS Query Script 🧚‍♀️

A python script that fetches and displays items from an SQS queue.

## Requirements 🍄

### Python 🐛

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

## Running Tests 🐌

Running tests with clean verbose output:

```
pytest --no-header -vv
```
