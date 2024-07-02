from re import search

from .crawler import Crawler
from .interface import CrawlerInterface

# ------------------------------ Constants ----------------------------------- #
EPISODE_CLASS   = "episodiotitle"
# ---------------------------------------------------------------------------- #

class CrawlerBakashiTv(Crawler, CrawlerInterface):
    def getLastEpisode(self, url: str) -> str:
        """ Função responsável por retornar o número do último episódio do 
        anime.

        Parameters
        -----------
        url: :class:`str`
            Url do site.
            
        Returns
        -----------
        episodeNumber: :class:`str`
        """

        soup = self.req_webpage(url=url)

        episodes                   = soup.find_all('div', class_=EPISODE_CLASS)
        lastEpisodeAnchor          = episodes[-1].contents[0]
        lastEpisodeNumber          = lastEpisodeAnchor.contents[0]
        lastEpisodeNumberSanitized = search(r'\d+', lastEpisodeNumber).group()

        return lastEpisodeNumberSanitized

    def getLastEpisodeUrl(self, url: str) -> str:
        """ Função responsável por retornar a url do último episódio do anime.

        Parameters
        -----------
        url: :class:`str`
            Url do site.
            
        Returns
        -----------
        lastEpisodeUrl: :class:`str`
        """

        soup = self.req_webpage(url=url)

        episodes          = soup.find_all('div', class_=EPISODE_CLASS)
        lastEpisodeAnchor = episodes[-1].contents[0]
        lastEpisodeUrl    = lastEpisodeAnchor.attrs["href"]

        return lastEpisodeUrl