import simplejson as json
import os

if os.path.isfile("./ages.jason") and os.stat("ages.json").st_size != 0:
    old_file = open("./ages.json", "r+")
    data = json.loads(old_file.read())
    print("Current age is" + str(data["age"]) + "-- adding a year.")
    data["age"] = data["age"] + 1
    print("New age is " + data["age"])
else:
    old_file = open("./ages.json", "w+")
    data = {"name": "Joseph", "age": 26}
    print("No file found, setting default age to " + str(data["age"]))

old_file.seek(0)
old_file.write(json.dumps(data))