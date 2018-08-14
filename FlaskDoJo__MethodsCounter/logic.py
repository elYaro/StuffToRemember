import json
# saving variable counter in data.txt file (will create file if data.txt does not exists
# input: dictionary
# saving as a string
def file_write(counter):
    file = open('./FlaskDoJo__MethodsCounter/data.txt','w')
    file.write(str(counter))
    file.close()


# reading data.txt file and getting the couter saved data
# recives: str
# returns: dict
def file_read():
    file = open('./FlaskDoJo__MethodsCounter/data.txt','r')
    str_data = file.read()
    str_data = str_data.replace("'", "\"")
    counter = data_converter(str_data)
    file.close()
    return counter


# json converter of str into dict
# input: string
# returns: json object --> dict
def data_converter(str_data):
    counter = json.loads(str_data)
    return counter

