import urllib

def read_text():
	quotes = open("C:\Users\Chronos Quantums\Desktop\projects of sorts\Practise\Python\movie_quotes.txt")
	contents = quotes.read()
	#print(contents)
	quotes.close()
	check_profanity(contents)

def check_profanity(text):
	connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text)
	output = connection.read()
	print(output)
	connection.close()
	
	
read_text()
