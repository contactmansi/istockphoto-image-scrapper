import urllib.parse


class IStockSearch:
    def __init__(self):
        self.__main_url = 'https://www.istockphoto.com/photos'

        self.__total_sort_types = ['best', 'newest', 'mostpopular']
        self.__safe_strings = ":/?-&="
        self.__search_query = None
        self.__sort_type = None
        self.__search_url = None
        self.__selected_page = None

        self.__attr_name = 'img'
        self.__image_extension = 'jpg'
        self.__attr_dict = {'class': 'gallery-asset__thumb gallery-mosaic-asset__thumb'}

    def __str__(self):
        return "iStock Photo - https://www.istockphoto.com/"

    def set_search_param(self, search_query: str, sort_type='mostpopular'):
        assert sort_type in self.__total_sort_types
        self.__search_query = search_query
        self.__sort_type = sort_type

    def create_search_url(self, page):
        self.__selected_page = page
        self.__search_url = "{}/{}?page{}&phrase={}&sort={}".format(
            self.__main_url,
            '-'.join(self.__search_query.split()),
            self.__selected_page,
            self.__search_query,
            self.__sort_type)
        quoted = urllib.parse.quote(self.__search_url, safe=self.__safe_strings)
        return quoted

    @property
    def main_url(self):
        return self.__main_url

    @property
    def search_query(self):
        return self.__search_query

    @property
    def sort_type(self):
        return self.__sort_type

    @property
    def search_url(self):
        return self.__search_url

    @property
    def attr_name(self):
        return self.__attr_name

    @property
    def attr_dict(self):
        return self.__attr_dict

    @property
    def image_extension(self):
        return self.__image_extension

    @property
    def selected_page(self):
        return self.__selected_page


if __name__ == '__main__':
    search_engine = IStockSearch()
    search_engine.set_search_param(search_query='horse field')
    search_engine.create_search_url(page=20)
    print(search_engine.selected_page)
