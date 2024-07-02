from deprecated import deprecated

from .crawler import Crawler
from .interface import CrawlerInterface

@deprecated("Esta classe não é mais compatível com o site goyabu")
class CrawlerGoyabuOld(Crawler, CrawlerInterface):
    """Crawler responsável pela antiga versão do site goyabu.
    """

    def getLastEpisode(self, url: str) -> str:
        """Função responsável por retornar o número do último episódio do
        anime.

        Args:
            url (str): Url do site.

        Returns:
            str
        """

        soup = self.req_url(url)

        animeInfo = soup.find("div", class_="anime-episode")
        episode = animeInfo.find("h3")
        episodeInfo = episode.contents[0].split(" ")

        for episodeNumber in episodeInfo:
            if(episodeNumber.isnumeric()):
                return episodeNumber

    def getLastEpisodeUrl(self, url: str) -> str:
        """Função responsável por retornar a url do último episódio do anime.

        Args:
            url (str): Url do site.

        Returns:
            str
        """

        soup = self.req_url(url)
        animeInfo = soup.find("div", class_="anime-episode")
        episode = animeInfo.find("a")
        lastEpisodeUrl = episode.attrs["href"]

        return lastEpisodeUrl

    @deprecated()
    def getLastEpisodeOld(self, url: str) -> str:
        """Função responsável por retornar o número do último episódio do anime.

        Args:
            url (str): Url do site.

        Returns:
            str
        """

        soup = self.req_url(url)

        for animeInfo in soup.find_all("div", class_="anime-episode"):
            for episodes in animeInfo.find_all("h3"):
                episodeInfo = episodes.contents[0].split(" ")

        for episodeNumber in episodeInfo:
            if(episodeNumber.isnumeric()):
                return episodeNumber

    def getLastEpisodeUrlOld(self, url: str) -> str:
        """Função responsável por retornar a url do último episódio do anime.

        Args:
            url (str): Url do site.

        Returns:
            str
        """

        soup = self.req_url(url)

        for animeInfo in soup.find_all("div", class_="anime-episode"):
            for episodes in animeInfo.find_all("a"):
                lastEpisodeUrl = episodes.attrs["href"]

        return lastEpisodeUrl
