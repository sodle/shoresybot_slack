# Shoresy Chirp Bot for Slack

This bot posts chirps by the Letterkenny character Shoresy in Slack.
Based on [the equivalent Reddit bot by iwharris](https://github.com/iwharris/shoresy-bot).

## Triggers

- Bot responds with a random chirp whenever it's @mention'd
- Bot responds with a "three things are gonna happen" chirp to any @mention that asks "what's gonna happen?"

## Development Roadmap

- [x] ~~_Basic insult functionality_~~
- [ ] CICD pipeline
- [ ] Discord support
- [ ] [Bug] figger oot why Slack sends duplicate events sometimes, and how to dedup them
- [ ] [Potential feature] for chirps that originally mentioned both Reilly and Jonesy['s moms], the bot currently just picks "Reilly" or "Jonesy" at random for the other slot. It could maybe pick another member of the slack channel at random.

# Self-hosting / Development

## Requires

- Python 3.x
- Pipenv
- An AWS account (used to access SSM Parameter Store, a free service)
- A Slack account, with access to the Developer Portal
- A box with outbound HTTP access (tested on Linux)
- A webserver that does SSL termination and forwards HTTP requests to this app on port 3000 (I used an AWS Application Load Balancer)

## Setting up

1. Create an app in the Slack developer portal and enable the events API. Take note of the signing secret in this tab and the access token in the main tab.
2. In AWS, find the Systems Manager service and its "Parameter Store" tab. Create two new Parameters, with names `/Shoresy/SlackSigningSecret` and `/Shoresy/SlackAccessToken`, and type `SecureString`. Save the parameters with their respective values from step 1.
3. Configure your local machine or server to access AWS, with a role that enables it to call `ssm:GetParameter` on the parameter you created in step 2.
4. Clone this repo and cd into it.
5. `pipenv install`
6. `pipenv run start`
7. In the slack dev portal, set the event target url to `https://<your_webserver_hostname>/shoresy/slack/events`

The bot should now be running and ready to listen for requests. Add your slack bot to a channel and @mention it to test.
