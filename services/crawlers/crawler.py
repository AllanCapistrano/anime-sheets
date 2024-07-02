import requests
from bs4 import BeautifulSoup

from ..webpage import get_webpage

# ------------------------------ Constants ----------------------------------- #
DIRECTORY_PATH = "web"
TIMEOUT        = 45
# ---------------------------------------------------------------------------- #

class Crawler:
    """Classe base para os crawlers
    """

    def req_url(self, url: str) -> BeautifulSoup:
        """Função responsável por buscar as Urls.

        Args:
            url (str): Url do site.

        Returns:
            BeautifulSoup
        """

        req  = requests.get(url=url, timeout=TIMEOUT)
        soup = BeautifulSoup(req.text, 'lxml')

        return soup

    def req_webpage(self, url: str, webpage_name: str = "index.html") -> BeautifulSoup:
        """Função responsável por buscar as Urls e fazer download das páginas.

        Args:
            url (str): Url do site.
            webpage_name (str, optional): Nome do arquivo. Por padrão é "index.html".

        Returns:
            BeautifulSoup
        """

        webpage_name = f"{DIRECTORY_PATH}/{webpage_name}"

        get_webpage(url=url)

        file = open(webpage_name, encoding="utf8")
        soup = BeautifulSoup(file, 'html.parser')
        file.close()

        return soup
