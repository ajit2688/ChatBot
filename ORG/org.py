from yahoo_finance import Share as sh


org_token = ['share','opening','product','about','ceo']

def parse_request(tokens):
	result =''
	tokens.sort()
	word =""
	for i in tokens:
		word+=i
	if word == 'shareteradata' or word == 'shareteradatavalue' or word =='priceshareteradata':
		y = sh('TDC')
		result = 'Teradata today\'s Share value is '+ y.get_price()
	elif word == 'openshare' or word == 'openpriceshare':
		y = sh('TDC')
		result = 'Teradata today\'s Share value is '+ y.get_price()+' today opening price: '+y.get_open()
	return result	
	