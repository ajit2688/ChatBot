import identifyPrimaryToken as id

def process(Ptkn,Stkn):
    a=''

def parse_request(tokens):
    result = ''
    All_token = set(tokens)
    primary_token = id.Ptoken(tokens);
    secondary_token = All_token.remove(primary_token)
    if len(primary_token) ==0 :
        result = 'I am not clear with your Question can you please be sepecific'
    else :
        result = process(primary_token,secondary_token)
    return result

