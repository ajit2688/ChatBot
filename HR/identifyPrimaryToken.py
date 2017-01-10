
primary_tokens = open('../tokens/HRPrimaryToken.txt').read()
def Ptoken(tokens):
    ptk = ''
    for i in tokens:
        if i in primary_tokens :
           ptk = i
    return ptk

