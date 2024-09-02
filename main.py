import json

with open('./dictionary.json', 'r') as file:
    data = json.load(file)
while True:
    word = input('enter word:')
    if word in data:
        print(word,' def:' ,data[word]['meaning'])
    else:
        break
        print('word not in dictionary')