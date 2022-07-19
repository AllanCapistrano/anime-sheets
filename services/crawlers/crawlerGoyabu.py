import re

from services.crawlers.crawler import Crawler
from services.crawlers.interface.crawlerInterface import CrawlerInterface

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
        lastEpisode        = animeInfo.contents[0].split(" ")[1]
        lastEpisodeNumeric = re.sub('[^.0-9]', '', lastEpisode)

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