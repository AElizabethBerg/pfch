from bs4 import BeautifulSoup

import requests

import json

frick_paintings = []

number = 1

url = "view/objects/asimages/152"
next_link = True

while next_link != None:
	url = 'http://collections.frick.org/' + url
	painting_page = requests.get(url)

	if painting_page.status_code != 200:	
		print ("There was an error with", url)

	page_html = painting_page.text
	soup = BeautifulSoup(page_html)

	full_title = soup.find_all("a", attrs = {"class" : "titleLink"})

	for title in full_title:

		full_artist = soup.find_all("span", attrs = {"class" : "imageArtist"})
		
		for artist in full_artist:

			next_link = soup.find("a",text="Next")

			if next_link != None:
				url = next_link['href']

		dictionary = { "number" : number, "title" : title.text, "artist" : artist.text }
		number = number + 1

		frick_paintings.append(dictionary)


with open('scraped_artworks.json', 'w') as f:
	f.write(json.dumps(frick_paintings,indent=4))


