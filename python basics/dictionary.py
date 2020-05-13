import json
from spellchecker import SpellChecker

sp = SpellChecker()


data = json.load(open("data.json"))
word = input("enter the word:")

print(sp)
def defi(w):
    w = w.lower()
    if w in data:
        print(data[w])

    else:
        msp = sp.correction(w)
        if(msp != w):
            print("did you mean the word: {}".format(msp))
        else:
            print("the data doesn't exit")
        
   
defi(word)   
    
    