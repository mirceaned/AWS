# Building apps with AWS blocks

## The app
- Visibility as a service for Public Cloud
- web UI
- agents deployed on EC2 instances to be monitored, taps traffic
- agents deployed on the instance with monitoring tools
- centralized backend in Amazon managed by the company which developed the product
- Salt Stack - infrastructure as code

## Subsystem
- Users are creating projects which have permissions associated
- Automated tests cab fail and cleanup is not done - resources become orphan
- A cleanup system takes care of the leftovers

## Lego blocks (Services)
- Lambda
- IAM
- DynamoDB
- Cloudwatch
- Events and Triggers

## Some lessons

### Good
- simple deployment, no need to worry about provisioning servers
- reduces cost for maintaining infrastructure
- most of the time scales quickly and automatically

### Bad
- sometimes Amazon throttles resources if they think something malicious is going on
- any downtime for the cloud provider will impact directly the app
- app needs to be designed from the ground app with the assumption things will go wrong (timeout, network issues etc)
- lambda may be too slow for some operations, web app needs to be designed to be responsive
- execution time for lambdas limited by default to 5 mins

### So-so
- design with the assumption everything will fail, increases complexity

### Find out more
- explore AWS services, free tier: https://aws.amazon.com/free/
