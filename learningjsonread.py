import json
file=open("jsonread_write","r")
x=file.read()
filedata=json.loads(x)
print("filedata")