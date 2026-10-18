import json

json_string ='''
  {
    "student":[
    {
      "name":"tim",
      "age":18
      },
      {
      "name":"fred",
      "age":20
      }       
    ]
  }
'''

data = json.loads(json_string)
data['passed'] = True

new_json = json.dumps(data, indent = 4)

print(new_json)