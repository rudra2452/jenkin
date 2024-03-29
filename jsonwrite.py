import json
#data={'name': "Prem Prakash", 'aim': "learning python"}

#with open("write.json","w") as writestjson:
    #json.dump(data,writestjson)
    #print(writestjson)
with open("write.json","r") as writestjson:
    data=json.load(writestjson)
data["aim"] = "DevOps"

with open("write.json","w") as writestjson:
    json.dump(data, writestjson)
    print(writestjson)
    
    