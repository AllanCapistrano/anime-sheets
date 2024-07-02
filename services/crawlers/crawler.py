import requests
from bs4 import BeautifulSoup

from ..webpage import getWebpage

# ------------------------------ Constants ----------------------------------- #
DIRECTORY_PATH = "web"
TIMEOUT        = 45
# ---------------------------------------------------------------------------- #

class Crawler:
    def req_url(self, url: str) -> BeautifulSoup:
        """ Função responsável por buscar as Urls.

        Parameters
        -----------
        url: :class:`str`
            Url do site.

        Returns
        -----------
        soup: :class:`BeautifulSoup`
        """

        req  = requests.get(url=url, timeout=TIMEOUT)
        soup = BeautifulSoup(req.text, 'lxml')

        return soup

    def req_webpage(self, url: str, webpage_name: str = "index.html") -> BeautifulSoup:
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

        getWebpage(url=url)

        file = open(webpage_name, encoding="utf8")
        soup = BeautifulSoup(file, 'html.parser')
        file.close()

        return soup
