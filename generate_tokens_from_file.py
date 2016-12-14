from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize as WT#
stop = set(stopwords.words('english'))
stop.update(['(',')','?',':','&'])
f = open("Questions.txt","r")
imptext = []
sentence = f.read()
if len(sentence) > 0:
    tokens = WT(sentence)
    for s in tokens:
        if s.lower() not in stop:
            imptext.append(s)
s = set(imptext)
f1= open("token.txt","w")
for i in s:
    f1.write(i+", ")
print (set(imptext))