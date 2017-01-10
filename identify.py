org_token = open('ORGtoken.txt').read()
hr_token = open('HRtoken.txt').read()
greet_token = open('Greet.txt').read()
def recoganize(tkn):
	result = 'UNKNOWNTOKEN'
	hr_count=0
	org_count=0
	greet_count = 0
	for t in tkn :
		if t in org_token:
			org_count+=1
		if t in hr_token:
			hr_count+=1
		if t in greet_token :
			greet_count+=1
	if hr_count ==0 and org_count==0:
		if greet_count != 0 :
			result='HI'
	elif hr_count > org_count :
		result= 'HR'
	else :
		result= 'ORG'
	return result
