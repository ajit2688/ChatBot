import remove_stop_words as RM
import identify as ID
import org
import hr
import random
import ADDtoDB as DB

greetinn_token = open('Greet.txt').read()

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

