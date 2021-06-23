import json
from difflib import get_close_matches

data=json.load(open("data.json"))

def translate(word):

    to_smaller=word.lower()

    if to_smaller in data:
       return data[to_smaller]
    elif to_smaller.title() in data:
        return data[to_smaller.title()]

    elif to_smaller.upper() in data:
        return data[to_smaller.upper()]

    elif len(get_close_matches(to_smaller,data.keys()))>0:
         match_word=input("Did you mean %s instead. Enter Y if yes else N ?" % str(get_close_matches(word,data.keys(),1)))
         if  match_word == "Y":
            return data[get_close_matches(word,data.keys())[0]]
         else:
             return "Enter a valid word"
    else:
        return "The word doesn't exist"


word=input("Enter a word : ")

output=translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
