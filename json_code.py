import json
f= open("templates//data.json","r")
s= f.read()
data=json.loads(s)

u_name="abhinav9001@kg.com"
print(data[u_name]["name"])