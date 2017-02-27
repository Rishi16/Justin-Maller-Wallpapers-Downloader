'''
	usage of python requests and beautifulsoup
	<3 Justin Maller
'''

import os
import requests
import urllib
from bs4 import BeautifulSoup


def get_projects():
	# creates a list of all projects
	src = requests.get('http://justinmaller.com/')
	soup = BeautifulSoup(src.text, 'html.parser')
	for link in soup.findAll('a', {'class', 'image'}):
		projects.append(link.get('href'))


def get_images():
	# to download each image
	for project_name in projects:
		project_title = project_name[9:-1]							# name for the folder
		url = 'http://justinmaller.com' + project_name
		project_src = requests.get(url)
		# is inside individual project page
		project_soup = BeautifulSoup(project_src.text, 'html.parser')
		for image_link in project_soup.findAll('a', text='Download Wallpaper'):
			# is inside the individual image's link
			image_url = image_link.get('href')
			image_src = requests.get(image_url)
			# is inside individual image's 'download wallpaper' page
			image_soup = BeautifulSoup(image_src.text, 'html.parser')

			image_title = image_soup.find('h1').text
			folder_name = folder_path + '/' + project_title
			image_name = folder_path + '/' + project_title + '/' + image_title + '.jpg'
			os.makedirs(folder_name, exist_ok=True)

			image = image_soup.findAll('img')[9].get('src')			# the actual image

			get_image(image, image_name, image_title, project_title, image_soup)


def get_image(image, image_name, image_title, project_title, image_soup):
	# do not try this at home
	# create folder if it doesn't exist
	if (os.path.exists(image_name)):
		print('image ' + image_name + ' already exists')
	else:
		try:
			# temporary hack
			urllib.request.urlretrieve(image, image_name)
			# confirmation message
			print('Finished downloading ' + image_title + ' from ' + project_title)
		except:
			if (image != image_soup.findAll('img')[8].get('src')):
				try:
					image = image_soup.findAll('img')[8].get('src')
					get_image(image, image_name, image_title, project_title, image_soup)
				except:
					pass
				else:
					try:
						image = image_soup.findAll('img')[10].get('src')
						get_image(image, image_name, image_title, project_title, image_soup)
					except:
						pass
						# please dont do this to yourself


if __name__ == '__main__':
	folder_path = input('Enter a path to store these wallpapers:\n')
	os.makedirs(folder_path, exist_ok=True)

	projects = []
	get_projects()
	get_images()