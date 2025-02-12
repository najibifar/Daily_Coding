import json
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])

# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print(y)

