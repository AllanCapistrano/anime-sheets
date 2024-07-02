from deprecated import deprecated

from .crawler import Crawler
from .interface import CrawlerInterface

@deprecated("Esta classe não é mais compatível com o site goyabu")
class CrawlerGoyabuOld(Crawler, CrawlerInterface):
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

        soup = self.req_url(url)

        anime_info   = soup.find("div", class_="anime-episode")
        episode      = anime_info.find("h3")
        episode_info = episode.contents[0].split(" ")

        for episode_number in episode_info:
            if (episode_number.isnumeric()):
                return episode_number

    def get_last_episode_url(self, url: str) -> str:
        """Função responsável por retornar a url do último episódio do anime.

        Args:
            url (str): Url do site.

        Returns:
            str
        """

        soup             = self.req_url(url)
        anime_info       = soup.find("div", class_="anime-episode")
        episode          = anime_info.find("a")
        last_episode_url = episode.attrs["href"]

        return last_episode_url

    @deprecated()
    def get_last_episodeOld(self, url: str) -> str:
        """Função responsável por retornar o número do último episódio do anime.

        Args:
            url (str): Url do site.

        Returns:
            str
        """

        soup = self.req_url(url)

        for anime_info in soup.find_all("div", class_="anime-episode"):
            for episodes in anime_info.find_all("h3"):
                episode_info = episodes.contents[0].split(" ")

        for episode_number in episode_info:
            if (episode_number.isnumeric()):
                return episode_number

    def get_last_episode_urlOld(self, url: str) -> str:
        """Função responsável por retornar a url do último episódio do anime.

        Args:
            url (str): Url do site.

        Returns:
            str
        """

        soup = self.req_url(url)

        for anime_info in soup.find_all("div", class_="anime-episode"):
            for episodes in anime_info.find_all("a"):
                last_episode_url = episodes.attrs["href"]

        return last_episode_url
