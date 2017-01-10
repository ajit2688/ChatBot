import random

import identify as ID
import remove_stop_words as RM
from DB import ADDtoDB as DB
from HR import hr
from ORG import org

greetinn_token = open('tokens/Greet.txt').read()

def redirect(sent) :
	result = ''
	tokens = RM.imp_word(sent)
	type = ID.recoganize(tokens)
	if type == 'ORG':
		result = org.parse_request(tokens)
	elif type == 'HR':
		result = hr.parse_request(tokens)
	elif type == 'HI' :
		print (tokens)
		for i in tokens:
			if i.lower() in greetinn_token :
				result =  random.choice(greetinn_token)+'!!! How can I help you ?'
	else :
		result = 'this Question can\'t be answered, we will update the Answer.'
		'''Add the Question into db table'''
		DB.add(sent)

	return result

