import os
import time
import processing
from slackclient import SlackClient

#BOT_ID = os.environ.get("BOT_ID")
SLACK_BOT_TOKEN = 'xoxp-111990615873-113353817607-124861784162-730df6118c6ae605c9a4e064ac843a92'
# constants

#AT_BOT = "<@" + BOT_ID + ">"
EXAMPLE_COMMAND = "do"

# instantiate Slack Client
slack_client = SlackClient('SLACK_BOT_TOKEN')


def handle_command(command, channel):
    response = processing.handle_input(command)
    slack_client.rtm_send_message(channel, response)


def parse_slack_output(slack_rtm_output):
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and 'reply_to' not in output:
                return output['text'].lower(), output['channel']
    return None, None


if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1
    if slack_client.rtm_connect():
        print("StarterBot connected and running!")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
