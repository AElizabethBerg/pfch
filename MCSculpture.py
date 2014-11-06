from bs4 import BeautifulSoup
import requests, csv

line = []
for i in range (10):
	payload = {"pg" : i}
	link = requests.get("http://metmuseum.org/collection/the-collection-online/search?what=Sculpture&ft=*&deptids=21&rpp=90&", params = payload)
	link_html = link.text
	with open ("MCSculpture.csv","w") as file:
		soup = BeautifulSoup(link_html)

		view_objects = soup.find_all("div", attrs={"class" : "list-view-object-info"})
		
		for j in range(len(view_objects)):
			
			artist_tag = view_objects[j].find_all("div", attrs= {"class" : "artist"})

			try:
				artist_line = artist_tag[0].text.replace(',', '/')+','
			except IndexError:
				artist_line = ' ,'

			try:
				origin_line = artist_tag[1].text.replace(',', '/')+','
			except IndexError:
				origin_line = ' ,'



			title_tag = view_objects[j].find_all("div", attrs= {"class" : "objtitle"})

			title_line = title_tag[0].text.replace(',', '/')+',' 



			info_tag = view_objects[j].find_all("div", attrs= {"class" : "objectinfo"})

			info_line0 = info_tag[0].text.replace(',', '/')+',' 

			try:
				info_line1 = info_tag[1].text.replace(',', '/')+','
			except IndexError:
				info_line1 = ' ,'

			try:
				info_line2 = info_tag[2].text.replace(',', '/')+','
			except IndexError:
				info_line2 = ' ,' 

			
			view_tag = view_objects[j].find_all("div", attrs= {"class" : "gallery"})

			view_line = view_tag[0].text +','  + '\n'


			line.append(artist_line)
			line.append(origin_line)
			line.append(title_line)
			line.append(info_line0)
			line.append(info_line1)
			line.append(info_line2)
			line.append(view_line)
			
		file.writelines(line)
			





