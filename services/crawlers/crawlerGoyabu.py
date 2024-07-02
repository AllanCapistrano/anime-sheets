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

        soup               = self.req_url(url)
        animeInfo          = soup.find("div", class_="chaps-infs")
        lastEpisode        = animeInfo.contents[0].split(" ")
        index              = len(lastEpisode) - 2
        lastEpisodeNumeric = sub('[^.0-9]', '', lastEpisode[index])

        return lastEpisodeNumeric

    def get_last_episode_url(self, url: str) -> str:
        """Função responsável por retornar a url do último episódio do anime.

        Args:
            url (str): Url do site.

        Returns:
            str
        """

        soup = self.req_url(url)

        animeInfo      = soup.find("div", class_="row")
        animeLink      = animeInfo.find("a")
        lastEpisodeUrl = animeLink.attrs["href"]

        return lastEpisodeUrl
