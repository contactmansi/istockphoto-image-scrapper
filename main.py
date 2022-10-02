import sys
import argparse

from scrapper import Scrapper
from istockphoto import IStockSearch

# python3 main.py --search-engine istockphoto  --total-images 10000

def parser():
    pars = argparse.ArgumentParser(description='Stock image scrap tool')
    pars.add_argument('--search-engine', type=str, default='istockphoto')
    pars.add_argument('--search-query', type=str, nargs='+') # removed search-query from required field
    pars.add_argument('--total-images', type=int, required=True)
    arg = pars.parse_args()
    if arg.search_query:
        arg.search_query = " ".join(arg.search_query)
    return arg

if __name__ == '__main__':
    arg = parser()
    search_engine = IStockSearch()
    search_engine.set_search_param(search_query=arg.search_query)
    scrap = Scrapper(search_engine=search_engine, total_image=arg.total_images)
    scrap.download()
    sys.exit(0)
