import webbrowser

class Movie():
	def __init__(self, t, s, piu, tyu):
		self.title = t
		self.synopsis = s
		self.poster_img_url = piu
		self.trailer_youtube_url = tyu
		
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)