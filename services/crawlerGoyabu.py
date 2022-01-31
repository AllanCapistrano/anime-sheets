from services.crawler import Crawler
from services.crawlerInterface import CrawlerInterface

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

        soup = self.reqUrl(url)

        for animeInfo in soup.find_all("div", class_="anime-episode"):
            for episodes in animeInfo.find_all("h3"):
                episodeInfo = episodes.contents[0].split(" ")

        for episodeNumber in episodeInfo:
            if(episodeNumber.isnumeric()):
                return episodeNumber

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

        for animeInfo in soup.find_all("div", class_="anime-episode"):
            for episodes in animeInfo.find_all("a"):
                lastEpisodeUrl = episodes.attrs["href"]
                
        return lastEpisodeUrl