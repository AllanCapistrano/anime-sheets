from re import sub

from .crawler import Crawler
from .interface import CrawlerInterface

class CrawlerGoyabu(Crawler, CrawlerInterface):
    """Crawler responsável pela antiga versão do site goyabu.
    """

    def get_last_episode(self, url: str) -> str:
        """Função responsável por retornar o número do último episódio do
        anime.

        Args:
            url (str): Url do site.

        Returns:
            str
        """

        soup                 = self.req_url(url)
        anime_info           = soup.find("div", class_="chaps-infs")
        last_episode         = anime_info.contents[0].split(" ")
        index                = len(last_episode) - 2
        last_episode_numeric = sub('[^.0-9]', '', last_episode[index])

        return last_episode_numeric

    def get_last_episode_url(self, url: str) -> str:
        """Função responsável por retornar a url do último episódio do anime.

        Args:
            url (str): Url do site.

        Returns:
            str
        """

        soup = self.req_url(url)

        anime_info       = soup.find("div", class_="row")
        animeLink        = anime_info.find("a")
        last_episode_url = animeLink.attrs["href"]

        return last_episode_url
