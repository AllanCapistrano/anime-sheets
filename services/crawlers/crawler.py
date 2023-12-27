import requests
from bs4 import BeautifulSoup

from ..webpage import getWebPage, deleteWebpage

# ------------------------------ Constants ----------------------------------- #
DIRECTORY_PATH = "web"
# ---------------------------------------------------------------------------- #

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
    
    def reqWebpage(self, url: str, webpage_name: str = "index.html") -> BeautifulSoup:
        """ Função responsável por buscar as Urls e fazer download das páginas.

        Parameters
        -----------
        url: :class:`str`
            Url do site.
        webpage_name: :class:`str`
            Nome do arquivo. Por padrão é `index.html`.

        Returns
        -----------
        soup: :class:`BeautifulSoup`
        """
        
        webpage_name = f"{DIRECTORY_PATH}/{webpage_name}"
        
        getWebPage(url=url)

        file = open(webpage_name)
        soup = BeautifulSoup(file, 'html.parser')
        file.close

        deleteWebpage()

        return soup