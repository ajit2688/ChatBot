import remove_stop_words as RM
import identify as ID
import org
import hr
import random

greetinn_token = ['hi','hello','whats up','ola']

def redirect(sent) :
	result = ''
	tokens = RM.imp_word(sent)
	type = ID.recoganize(tokens)
	if type == 'ORG':
		result = org.parse_request(tokens)
	elif type == 'HR':
		result = ''
	else :
		print (tokens)
		for i in tokens:
			if i.lower() in greetinn_token :
				result =  random.choice(greetinn_token)+'!!! How can I help you ?'
	return result
	
	
	

