'''
	simple yet functional scraper to get wallpapers from facets.la
	<3 Justin Maller
'''

import os
import requests
import urllib
from bs4 import BeautifulSoup


def get_images():
	page_src = requests.get('http://www.facets.la/wallpapers/')
	page_soup = BeautifulSoup(page_src.text, 'html.parser')
	for image_link in page_soup.findAll('div', {'class', 'thumb-image'}):
		image_url = image_link.find('a').get('href')
		image_url_src = requests.get(image_url)
		image_url_soup = BeautifulSoup(image_url_src.text, 'html.parser')
		img = image_url_soup.find('div', id='facet-wallpaper').find('img').get('src')
		title = image_url_soup.find('div', {'class', 'size15'}).find('strong').text
		urllib.request.urlretrieve(img, folder_path + '/' + title + '.jpg')
		print('Finished downloading ' + title)


if __name__ == '__main__':
	folder_path = input('Enter a path to store these wallpapers:\n')
	os.makedirs(folder_path, exist_ok=True)

	get_images()