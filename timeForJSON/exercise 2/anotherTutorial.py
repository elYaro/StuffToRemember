# based on tutorial: https://www.youtube.com/watch?v=9N6a-VLBa2I

import json


# for this exercise we create here the data_string variable containing string looking like json object
data_string = '''
    {
	    "people": 
        [
        {
			"name": "Jarek",
			"location": "Poland",
			"age": 42,
			"sex": "male",
            "happy" : true,
            "pets" : null
		},
		{
			"name": "Adam",
			"location": "Swiss",
			"age": 40,
			"sex": "male",
            "happy" : false,
            "pets" : null
		},
		{
			"name": "Kate",
			"location": "UK",
			"age": 30,
			"sex": "female",
            "happy" : false,
            "pets" : true
		}
	    ]
    }
'''
# lets check the type, length and content ...see...it is a string, length 468.
print("1.data.\n type: {}  ---- length : {} ---- sample: {} \n".format(type(data_string), len(data_string), data_string[13]))


# now lets convert this string json into python object....see....it is a Python dictionaty now, length 1. 
data_loads = json.loads(data_string)  # json.loads method convetrs json object into Python dictionary, changes false >> False, true >> True, null >> None, arrey >> list, object >> dirctionary, etc.
print("2.data_loads.\n type: {}  ---- length : {} ---- sample: {} \n".format(type(data_loads), len(data_loads), data_loads))

# lest check the data inside this dictionary
print("2.1.data_loads['person'].\n type: {}  ---- length : {} ---- sample: {} \n".format(type(data_loads["people"]), len(data_loads["people"]), data_loads["people"]))


#  ok , so sow lets use dumps method to convert it into json object...see....it becomes the string again in a json format
data_dumps = json.dumps(data_loads, indent=2)
print("3.data_dumps.\n type: {}  ---- length : {} ---- sample: {} \n".format(type(data_dumps), len(data_dumps), data_dumps))

# we can easyly iterate on the python object after usung json.loads method

for person in data_loads["people"]:
    print(person["name"])

# we cen delete a specific data, specific key...example key: "happy"
for person in data_loads["people"]:
    del person["happy"]
    print(person)


# ------------------------------------------------------------------------------------------------

# ok, so now lets do simmilar but usung data from the json file (lets look at the data.json file)

with open('data.json') as file:
    # data_from_file = file.read() #it is a string now
    #  in order to have easier to work with type ... like dictionary we can use json.load method:
    data_from_file_load = json.load(file)
    print(type(data_from_file_load), data_from_file_load) # now it is a python dictionary

    # so lets save this data to the another file, but before lets delete soma data (for example: 'sex')
    for item in data_from_file_load['people']:
        del item["sex"]
    
    with open('new_file.json', 'w') as f:
        json.dump(data_from_file_load, f, indent=2)
