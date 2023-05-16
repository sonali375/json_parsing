# Python program to read json file
import json

# Opening JSON file
f = open('input.json', "r")

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
sonali_list = []
for i in data['parametersList']:
    my_dict = {
        "parameterName": i['parameterName'],
        "min": i['min'],
        "max": i['max'],
        "avg": i['avg']

    }

    sonali_list.append(my_dict)
my_list = json.dumps(sonali_list)
# dumps helps to convert it into json format so it will return a string
print(my_list)

with open("input.json", "w") as file1:
    file1.write(my_list)
print(sonali_list)

# Closing file
f.close()
