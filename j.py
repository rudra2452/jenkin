import json

# Reading data from a JSON file
with open("posts.json", "r") as file:
    x = file.read()
    finaldata = json.loads(x)
    print(finaldata)
    
    


