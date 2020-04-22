import json

data = json.load(open("data.json"))

word = input("Enter word: ")

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    else:
        return "The word doesn't exist. Please double check it."



print(translate(word))
