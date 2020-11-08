from slackeventsapi import SlackEventAdapter
from slack import WebClient
import boto3
import time
from flask import Flask
from chirps import get_random_chirp, get_happen_chirp

ssm = boto3.client('ssm', region_name='us-west-2')
SLACK_SIGNING_SECRET = ssm.get_parameter(
    Name='/Shoresy/SlackSigningSecret', WithDecryption=True)['Parameter']['Value']
SLACK_ACCESS_TOKEN = ssm.get_parameter(
    Name='/Shoresy/SlackAccessToken', WithDecryption=True)['Parameter']['Value']

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello!"


slack_events_adapter = SlackEventAdapter(
    SLACK_SIGNING_SECRET, "/shoresy/slack/events", app)
slack_client = WebClient(token=SLACK_ACCESS_TOKEN)


@slack_events_adapter.on('app_mention')
def on_message(payload):
    user_target = payload['event']['user']

    target_profile = slack_client.users_info(user=user_target)
    if target_profile['user']['is_bot']:
        time.sleep(10)

    mention = f"<@{user_target}>"

    channel = payload['event']['channel']
    if 'happen' in str.lower(payload['event']['text']):
        slack_client.chat_postMessage(channel=channel, text=get_happen_chirp(),
                                      thread_ts=payload['event'].get('thread_ts', None))
    else:
        slack_client.chat_postMessage(
            channel=channel, text=get_random_chirp(mention),
            thread_ts=payload['event'].get('thread_ts', None))


if __name__ == "__main__":
    app.run()
