import os
from shutil import rmtree
import urllib3
import urllib3.request
from bs4 import BeautifulSoup
from tqdm import tqdm

from istockphoto import IStockSearch


class Scrapper:
	def __init__(self, search_engine: IStockSearch, total_image=1000):
		self.search_engine = search_engine
		self.total_image = total_image
		self.save_path = self.search_engine.engine_name + '_' + '_'.join(search_engine.search_query.split())

		if os.path.exists(self.save_path):
			rmtree(self.save_path, ignore_errors=True)
		os.mkdir(self.save_path)

		self.pool_man = urllib3.PoolManager()
		self.downloaded_im = 0
		self.parser_type = 'html.parser'
		self.response = None
		self.links = None

		self.pbar = tqdm(total=self.total_image, unit='image')

	def url_request(self, page):
		self.response = self.pool_man.request('GET', self.search_engine.create_search_url(page))
		self.links = self.__bs4_parser()
		self.response.release_conn()

	def __bs4_parser(self):
		soup = BeautifulSoup(self.response.data, self.parser_type)
		return soup.find_all(self.search_engine.attr_name, attrs=self.search_engine.attr_dict)

	def image_url_to_file(self):
		for link in self.links:
			im_url = link.get('src')
			im_request = self.pool_man.request('GET', im_url, preload_content=False)
			with open(os.path.join(self.save_path, f'{self.downloaded_im+1:04}.jpg'), 'wb') as out:
				while True:
					data = im_request.read(256)
					if not data:
						break
					out.write(data)
			self.downloaded_im += 1
			self.pbar.update(1)
			if self.downloaded_im == self.total_image:
				break
			im_request.release_conn()

	def download(self):
		self.print_scrap_conf()
		print('Starting!')
		page = 1
		while self.downloaded_im < self.total_image:
			self.pbar.set_description(f"Downloading page: {page} ")
			try:
				self.url_request(page)
				self.image_url_to_file()
				page += 1
			except Exception as e:
				page += 1
				print('Fail on page', e)
		self.pbar.close()
		self.check_download_count()

	def check_download_count(self):
		p = os.listdir(self.save_path)
		print('\nChecking local files!')
		if len(p) == self.total_image:
			print(f'Scrap successful! {self.downloaded_im}/{self.total_image}')
		else:
			print(f'Scrap failed! {self.downloaded_im}/{self.total_image}')

	def print_scrap_conf(self):
		print(f'\nSearch engine: \t\t\t\t{self.search_engine}')
		print(f'Search engine sort method: \t{self.search_engine.sort_type}')
		print(f'Total image request: \t\t{self.total_image}')
		print(f'Save path: \t\t\t\t\t{self.save_path}\n')
