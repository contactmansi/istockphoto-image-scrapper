# import os
# import urllib3
# import urllib3.request
# from bs4 import BeautifulSoup
# from tqdm import tqdm
#
# os.mkdir('image')
#
# i = 0
# for page in range(1, 20):
# 	url = f'https://www.istockphoto.com/photos/gold-bullion?page={page}&phrase=gold%20bullion&sort=mostpopular'
#
# 	response = http.request('GET', url)
# 	soup = BeautifulSoup(response.data, 'html.parser')
# 	image_links = soup.find_all('img', attrs={'class': 'gallery-asset__thumb gallery-mosaic-asset__thumb'})
# 	response.release_conn()
# 	print('page: ', page)
# 	for link in tqdm(image_links):
# 		im_url = link.get('src')
# 		r = http.request('GET', im_url, preload_content=False)
# 		with open(os.path.join('image', f'{i}.jpg'), 'wb') as out:
# 			while True:
# 				data = r.read(256)
# 				if not data:
# 					break
# 				out.write(data)
# 		i += 1
# 		r.release_conn()


from scrapper import Scrapper
from istockphoto import IStockSearch


if __name__ == '__main__':
    istock_se = IStockSearch()
    istock_se.set_search_param(search_query='lion')
    scrap = Scrapper(search_engine=istock_se, total_image=100)
    scrap.download()
