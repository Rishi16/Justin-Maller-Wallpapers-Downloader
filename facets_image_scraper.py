'''
	usage of python requests and beautifulsoup
	<3 Justin Maller
'''

import os
import requests
import urllib
from bs4 import BeautifulSoup


def get_images():
	# TODO:
	# DO THE TRADITIONAL WAY'
	# NOT ALL OF THEM ARE WALLPAPERS
	for i in range(1, 331)[22:23]:
		url = 'http://www.facets.la/2013/' + str(i) + '/wallpaper/'
		print(url)
		src = requests.get(url)
		soup = BeautifulSoup(src.text, 'html.parser')
		img = soup.findAll('img')[2]
		print(img)



if __name__ == '__main__':
	#folder_path = input('Enter a path to store these wallpapers:\n')
	#os.makedirs(folder_path, exist_ok=True)

	get_images()