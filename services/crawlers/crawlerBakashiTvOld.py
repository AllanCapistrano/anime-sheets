from re import search

from .crawler import Crawler
from .interface import CrawlerInterface

# ------------------------------ Constants ----------------------------------- #
ANCHOR_POSITION = 2
EPISODE_CLASS   = "epnumber"
# ---------------------------------------------------------------------------- #

class CrawlerBakashiTvOld(Crawler, CrawlerInterface):
    """Crawler responsável pela antiga versão do site bakashi.
    """

    def getLastEpisode(self, url: str) -> str:
        """Função responsável por retornar o número do último episódio do 
        anime.

        Args:
            url (str): Url do site.

        Returns:
            str
        """

        soup = self.req_webpage(url=url)

        episodes                   = soup.find_all('div', class_=EPISODE_CLASS)
        lastEpisode                = episodes[-1].contents[0]
        lastEpisodeNumberSanitized = search(r'\d+', lastEpisode).group()

        return lastEpisodeNumberSanitized

    def getLastEpisodeUrl(self, url: str) -> str:
        """Função responsável por retornar a url do último episódio do anime.

        Args:
            url (str): Url do site.

        Returns:
            str
        """

        soup = self.req_webpage(url=url)

        episodes            = soup.find_all('div', class_=EPISODE_CLASS)
        lastEpisodeListItem = episodes[-1].parent
        lastEpisodeAnchor   = lastEpisodeListItem.contents[ANCHOR_POSITION]
        lastEpisodeUrl      = lastEpisodeAnchor.attrs["href"]

        return lastEpisodeUrl
