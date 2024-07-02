from abc import ABC, abstractmethod

class CrawlerInterface(ABC):
    """Interface para os crawlers
    """

    @abstractmethod
    def getLastEpisode(self, url: str) -> str:
        """Função responsável por retornar o número do último episódio do
        anime.

        Args:
            url (str): Url do site.

        Returns:
            str
        """

    @abstractmethod
    def getLastEpisodeUrl(self, url: str) -> str:
        """Função responsável por retornar a url do último episódio do anime.

        Args:
            url (str): Url do site.

        Returns:
            str
        """
