import os
from slackclient import SlackClient
import time
from yahoo_finance import Share as sh
import random
import nltk
#from nltk.tokenize import word_tokenize
#import remove_stop_words as RM
#import redirect as RE
import aiml as AI
import sqlite3
slack_client = SlackClient("xoxp-111990615873-113353817607-130303875302-9e20c3253753286fbed9a64820e7c9cc")


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
			BOT_NAME = user['name']


def connect() :
    try:
        con = sqlite3.connect('DB\slackbot.db')
        c = con.cursor()
    except :
        print('DB Connection ERROR : ')

    return con,c

def fetch(sql) :
    res =''
    try :
        con, c = connect()
        c.execute(sql)
        res = c.fetchall()
        con.commit()
    except:
        print("Fetch ERROR: ")
    finally:
        con.close()
    return res

def add(sent) :
    try:
        con,c = connect()
        c.execute('''CREATE TABLE IF NOT EXISTS question (Ques text)''')
        sql = "INSERT INTO question (Ques) VALUES ('"+sent+"')"
        c.execute(sql)
#       c.execute('''select * from answered''')
#       print(c.fetchall())
        con.commit()
        con.close()
    except :
        print ("DB ERROR : ")
    finally:
        con.close()
# constants
AT_BOT = "<@" + BOT_ID + ">"
EXAMPLE_COMMAND = "do"


def handle_command(res, channel):
	if len(res) == 0:
		res = "I dont have information right now"
	slack_client.api_call("chat.postMessage", channel=channel,text=res, as_user=True)


def parse_slack_output(slack_rtm_output):
	output_list = slack_rtm_output
	if output_list and len(output_list) > 0:	
		for output in output_list:
			#print(output)
			if output.has_key('text') and output.has_key('user') and output['user'] != BOT_ID:
				return output['text'], \
					   output['channel']
	return None, None

if __name__ == "__main__":	
	READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
	print("READ_WEBSOCKET_DELAY : ", READ_WEBSOCKET_DELAY)
	if slack_client.rtm_connect():
		print("StarterBot connected and running!")
		mybot = AI.Kernel()
		#os.chdir('AIML')
		# If there is a brain file named standard.brn, Kernel() will initialize using bootstrap() method
		if os.path.isfile("Slackstandard.brn"):
			mybot.bootstrap(brainFile="Slackstandard.brn")
		else:
			# If there is not brain file, load all AIML files and save a new brain
			mybot.bootstrap(learnFiles="startup.xml", commands="init")
			mybot.saveBrain("Slackstandard.brn")
		while True:
			command, channel = parse_slack_output(slack_client.rtm_read())
			if command and channel:
				result = mybot.respond(command)
				if "FINANCEAPI" in result:
					result = result.replace("FINANCEAPI", "")
					y = sh(result)
					result = 'Teradata today\'s Share value is ' + y.get_price()
				elif "DB" in result:
					res = result.replace("DB", "")
					#print res
					xres = fetch(res)
					result = xres
				elif "ADDTODB:" in result:
					result = result.replace("ADDTODB:","")
					add(command)
				if len(result)==0:
					result = "I dont have information right now"
					add(command)
				handle_command(result, channel)
			time.sleep(READ_WEBSOCKET_DELAY)
	else:
		print("Connection failed. Invalid Slack token or bot ID?")
