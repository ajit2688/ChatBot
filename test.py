'''
read = open('Greet.txt').read()

#print (read[read.find('Policy CMP601'):])
txt = read.split(',')
print(read)
print(txt)
'''

from slackclient import SlackClient
import time
# from yahoo_finance import Share as sh
import random
import nltk
# from nltk.tokenize import word_tokenize
# import remove_stop_words as RM
import redirect as RE
'''
slack_client = SlackClient("xoxp-111990615873-113353817607-124861784162-730df6118c6ae605c9a4e064ac843a92")

BOT_NAME = "ajitbot"
BOT_ID = ''
print ('!!!!!connection created!!!!!')
api_call = slack_client.api_call("users.list")
if api_call.get('ok'):
    users = api_call.get('members')
    for user in users:
        print (user)
'''
#U39U907J4
'''u'text': u'hey wahsu how you doing', u'ts': u'1484032710.000006', u'user': u'U39U907J4', u'team': u'T39V4J3RP', u'type': u'message', u'channel': u'D3BAETTBR'}'''
hr_token = open('HRtoken.txt').read()
t = 'hr'

print (hr_token)
print (hr_token.index(t))
if t in hr_token :
    print ('yes')