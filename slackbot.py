from slackeventsapi import SlackEventAdapter
from slack import WebClient
import boto3
import time
import logging
import sys
import json
import threading
from flask import Flask
from chirps import get_random_chirp, get_happen_chirp

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(stream=sys.stdout))

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

def send_message(channel: str, text: str, thread_ts: str = None, delay_sec: int = 0):
    time.sleep(delay_sec)
    slack_client.chat_postMessage(channel=channel, text=text, thread_ts=thread_ts)


@slack_events_adapter.on('app_mention')
def on_message(payload):
    logger.info(json.dumps(payload))

    user_target = payload['event']['user']

    target_profile = slack_client.users_info(user=user_target)
    logger.info(target_profile)

    mention = f"<@{user_target}>"

    channel = payload['event']['channel']
    if 'happen' in str.lower(payload['event']['text']):
        chirp = get_happen_chirp()
    else:
        chirp = get_random_chirp(mention)

    send_thread = threading.Thread(target=send_message, kwargs={
        'channel': channel,
        'text': chirp,
        'thread_ts': payload['event'].get('thread_ts', None),
        'delay_sec': 300 if target_profile['user']['is_bot'] else 0
    })
    send_thread.run()


if __name__ == "__main__":
    app.run()
