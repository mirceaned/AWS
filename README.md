# AWS Building Blocks for apps

## Lego blocks
Services
- Lambda
- IAM
- DynamoDB
- Cloudwatch
- Events and Triggers

## Pros
- simplifies deployment
- reduces cost for maintaining infrastructure
- most of the time easily scalable

## Cons
- sometimes Amazon throttles resources if they think something malicious is going on
- any downtime for the cloud provider will impact the app
- app needs to be designed from the ground app with the assumption things will go wrong - e.g. requests may fail so retry mechanism is needed
- lambda may be too slow for some operations, web app needs to be designed to be responsive
