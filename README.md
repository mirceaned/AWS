# Building apps with AWS

## Overview
- Cloud providers offer building blocks for a variety of needs
- various degrees of cloud integration, for legacy apps or cloud native ones 

## A cloud native app
- Visibility as a service for public cloud
- web app hosted in S3
- agents on EC2 instances to tap traffic
- agents on EC2 instance with monitoring tools
- centralized backend in Amazon Cloud
- Salt Stack - for infrastructure

## Subsystem
- Users are creating projects which have permissions associated
- Automated tests can fail and cleanup is not done - resources become orphan
- A cleanup system to take care of the leftovers

## Building blocks (Services)
- Lambda
- API Gateway
- IAM
- DynamoDB
- Cloudwatch Logs and Events

## Some lessons

### Good
- simple deployment, with serverlss no need to worry about provisioning
- can reduce cost for infrastructure
- most of the time scales quickly and automatically

### Bad
- sometimes Amazon throttles resources if they think something malicious is going on
- any downtime for the cloud provider will directly impact the app
- lambda may be too slow for time critical operations, caller (e.g. web app) needs to be designed to be responsive. cold start.
- execution time for lambdas limited to 5 mins by Amazon
- debugging for Amazon lambdas is difficult

### So-so
- design with the assumption everything will fail (timeouts, network issues etc), increases complexity

### Find out more
- explore AWS services, try the free tier and the labs: 

https://aws.amazon.com/free/

https://aws.amazon.com/training/self-paced-labs/

- competition: Microsoft Azure, Google Cloud
