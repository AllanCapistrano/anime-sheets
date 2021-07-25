import requests
from bs4 import BeautifulSoup

class CrawlerGoyabu:
    def __reqUrl__(self, url: str) -> BeautifulSoup:
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

    def getLastEpisode(self, url: str) -> str:
        """ Função responsável por retornar o número do último episódio do anime.

        Parameters
        -----------

        url: :class:`str`
            Url do site.
            
        Returns
        -----------
        episodeNumber: :class:`str`
        """

        soup = self.__reqUrl__(url)

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

        soup = self.__reqUrl__(url)

        for animeInfo in soup.find_all("div", class_="anime-episode"):
            for episodes in animeInfo.find_all("a"):
                lastEpisodeUrl = episodes.attrs["href"]
                
        return lastEpisodeUrl