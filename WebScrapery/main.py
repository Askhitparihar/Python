from bs4 import BeautifulSoup
import requests

search = raw_input("Enter Search Term: ")
params = {"q": search}
r = requests.get("https://www.bing.com/search", params=params)

soup = BeautifulSoup(r.text, "html.parser")
results = soup.find("ol", {"id": "b_results"})
links = results.findAll("li", {"class": "b_algo"})

for item in links:
    itemText = item.find("a").text
    itemHref = item.find("a").attrs["href"]

    if itemText and itemHref:
        print(itemText)
        print(itemHref)
        #print("Summary: " + str(item.find("a").parent.parent.find("p").text))


        #children = item.find("h2")
        #print("Next sibling of H2: " + str(children.next_sibling))



