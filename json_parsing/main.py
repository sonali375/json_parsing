# Python program to read json file
import json

# Opening JSON file
file = open('input.json', "r")

# returns JSON object as a dictionary
data = json.load(file)

# Iterating through the json
# list
sonali_list = []
for item in data['parametersList']:
    my_dict = {
        "parameterName": item['parameterName'],
        "min": item['min'],
        "max": item['max'],
        "avg": item['avg']

    }

    sonali_list.append(my_dict)
my_list = json.dumps(sonali_list)
# dumps helps to convert it into json format so it will return a string
print(my_list)

with open("output.json", "w") as file1:
    file1.write(my_list)
print(sonali_list)

# for each_keys in data:
#     # print(each_keys)
#     # print(json_data[each_keys])
#     if isinstance(data[each_keys], list):
#         print(each_keys)
#         print(type(data[each_keys]))
#         print()
#         for each_items in data[each_keys]:
#             print(each_items)

# Closing file
file.close()
