import sys
import argparse

from scrapper import Scrapper
from istockphoto import IStockSearch


def parser():
    pars = argparse.ArgumentParser(description='Stock image scrap tool')
    pars.add_argument('--search-engine', type=str, default='istockphoto')
    pars.add_argument('--search-query', type=str, nargs='+', required=True)
    pars.add_argument('--total-images', type=int, required=True)
    arg = pars.parse_args()
    arg.search_query = " ".join(arg.search_query)
    return arg


if __name__ == '__main__':
    arg = parser()

    if arg.search_engine == 'istockphoto':
        search_engine = IStockSearch()
    else:
        search_engine = IStockSearch()
    # TODO: Will be fixed when new engines added

    search_engine.set_search_param(search_query=arg.search_query)
    scrap = Scrapper(search_engine=search_engine, total_image=arg.total_images)
    scrap.download()
    sys.exit(0)
