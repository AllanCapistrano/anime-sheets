import requests
from bs4 import BeautifulSoup

class Crawler:
    def reqUrl(self, url: str) -> BeautifulSoup:
        """ Função responsável por buscar as Urls.

        Parameters
        -----------
        url: :class:`str`
            Url do site.

        Returns
        -----------
        soup: :class:`BeautifulSoup`
        """

        req  = requests.get(url)
        soup = BeautifulSoup(req.text, 'lxml')

        return soup