org_token = ['share','opening','product','about','ceo']
hr_token = ['hr','clc']

def recoganize(tkn):
	hr_count=0
	org_count=0
	for t in tkn :
		if t in org_token:
			org_count+=1
		if t in hr_token:
			hr_count+=1
	if hr_count ==0 and org_count==0:
		return 'HI'
	elif hr_count > org_count :
		return 'HR'
	else :
		return 'ORG'
