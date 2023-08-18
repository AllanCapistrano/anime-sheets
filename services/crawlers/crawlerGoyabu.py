import re

from .crawler import Crawler
from .interface import CrawlerInterface

class CrawlerGoyabu(Crawler, CrawlerInterface):

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

        soup               = self.reqUrl(url)
        animeInfo          = soup.find("div", class_="chaps-infs")
        lastEpisode        = animeInfo.contents[0].split(" ")
        index              = len(lastEpisode) - 2
        lastEpisodeNumeric = re.sub('[^.0-9]', '', lastEpisode[index])

        return lastEpisodeNumeric

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

        soup = self.reqUrl(url)

        animeInfo      = soup.find("div", class_="row")
        animeLink      = animeInfo.find("a")
        lastEpisodeUrl = animeLink.attrs["href"]

        return lastEpisodeUrl