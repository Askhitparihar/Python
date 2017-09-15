import requests

myData = {"name": "Joseph", "email": "none@none.com"}
r = requests.post("http://www.w3schools.com/php/welcome.php", data=myData)

f = open("myFile.html", "w+")
f.write(r.text)