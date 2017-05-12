import media 

toy_story = media.Movie("Toy Story", 
							"A boy's toys come to life.",
							"https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg",
							"https://www.youtube.com/watch?v=KYz2wyBy3kc")							
print(toy_story.synopsis)							

avatar = media.Movie("Avatar",
						"A marine on an alien planet, eco-friendly.",
						"https://en.wikipedia.org/wiki/Avatar_(2009_film)#/media/File:Avatar-Teaser-Poster.jpg",
						"https://www.youtube.com/watch?v=zWKIWNJnlzI")
print(avatar.synopsis)		

avatar.show_trailer()	