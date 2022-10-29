text =str(input("what is the message to cypher" ))

def key_generator():
    key = str(input("what key would you loke to use" ))
    if len(key) == len(text):
        return(key)
    else :
        for i in range (len(text)-len(key)):
             key.append(key[i % len(key)])
    return("" . join(key))

def encription(text,key):
    
