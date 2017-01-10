from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize as WT
stop = set(stopwords.words('english'))
stop.update(["bot","ajitbot"])
stop.remove('about')
#sentence = 'tell me about teradata'

def imp_word (sentence):
	if len(sentence) > 0:
		tokens = WT(sentence)
		imptext = []
		for s in tokens:
			if (s not in stop) and (not s.isdigit()):
				imptext.append(s.lower())
		return (imptext)
	return None
	
#print (imp_word(sentence))