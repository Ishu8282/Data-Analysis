import json
from difflib import get_close_matches


data = json.load(open("data.json"))
word = input("enter the word:")

def defi(w):
    w = w.lower()
    if w in data:
        x=data[w]
        print(i for i in x)

    elif len(get_close_matches(w, data.keys()))> 0:
        strn=get_close_matches(w,data.keys())[0]
        ans = input("did you mean {}:".format(strn) )
        if ans == "yes":
            print(data[strn])
        else:
            print("double check the word")

      
    else:
        print("the data doesn't exit")
        
   
defi(word)   
    
    