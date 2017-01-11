import json
import jsonschema
 
schema = open("schema1.json").read()
print schema
 
data = open("data.json").read()
print data
 
try:
    jsonschema.validate(json.loads(data), json.loads(schema))
except jsonschema.ValidationError as e:
    print e.message
except jsonschema.SchemaError as e:
    print e
