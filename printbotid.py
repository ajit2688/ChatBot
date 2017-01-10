import os
from slackclient import SlackClient
import time
#from yahoo_finance import Share as sh
import random
import nltk
#from nltk.tokenize import word_tokenize
#import remove_stop_words as RM
import redirect as RE





slack_client = SlackClient("xoxp-111990615873-113353817607-124861784162-730df6118c6ae605c9a4e064ac843a92")


BOT_NAME = "ajitbot"
BOT_ID =''
api_call = slack_client.api_call("users.list")
if api_call.get('ok'):
	users = api_call.get('members')
	for user in users:
###		print(user.get('name'))
		if 'name' in user and user.get('name') == BOT_NAME:
			print("Bot ID for '" + user['name'] + "' is " + user.get('id'))
			BOT_ID = user.get('id')
		

# constants
AT_BOT = "<@" + BOT_ID + ">"
EXAMPLE_COMMAND = "do"


def handle_command(res, channel):
	if len(res) == 0:
		res = "invalid Request"
	slack_client.api_call("chat.postMessage", channel=channel,text=res, as_user=True)


def parse_slack_output(slack_rtm_output):
	output_list = slack_rtm_output
	if output_list and len(output_list) > 0:	
		for output in output_list:
			print(output)
			if output.has_key('text') and output.has_key('user') and output['user'] != BOT_ID:
				return output['text'], \
					   output['channel']
	return None, None

def handle_command_paresing(text1, channel) :
#	token = RM.imp_word(command)
	result = RE.redirect(text1)
	print(result)
	handle_command(result, channel)				

	
if __name__ == "__main__":	
	READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
	print("READ_WEBSOCKET_DELAY : ", READ_WEBSOCKET_DELAY)
	if slack_client.rtm_connect():
		print("StarterBot connected and running!")
		while True:
			command, channel = parse_slack_output(slack_client.rtm_read())
			if command and channel:
				handle_command_paresing(command, channel)		
			time.sleep(READ_WEBSOCKET_DELAY)
	else:
		print("Connection failed. Invalid Slack token or bot ID?")
