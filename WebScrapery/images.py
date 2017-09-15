from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os

def StartSearch():
    search = raw_input("Enter Search Term: ")
    params = {"q": search}
    dirName = search.replace(" ", "_").lower()

    if not os.path.isdir(dirName):
        os.makedirs[dirName]

    r = requests.get("http://www.bing.com/images/search", params=params)

    soup = BeautifulSoup(r.text, "html.parser")
    links = soup.findAll("a", {"class": "thumb"})

    for item in links:
        try:
            imgObj = requests.get(item.attrs["href"])
            print("Getting " + str(item.attrs["href"]))
            title = item.attrs["href"].split("/")[-1]
            try:
                img = Image.open(BytesIO(imgObj.content))
                img.save("./" + dirName + title + img.format)
            except:
                print("Could not save image.")
        except:
            print("Could not request image.")

    StartSearch()
StartSearch()