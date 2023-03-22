
import random

key=[
"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",
"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"
    ]
def apikey(N=None):

    if N==None:
        return key[random.randint(0,len(key)-1)]
    elif N>len(key):
        return key[random.randint(0,len(key)-1)]
    elif N==0:
        return key[0]
    else:
        return key[N-1]
        
