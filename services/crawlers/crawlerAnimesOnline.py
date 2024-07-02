from re import search

from .crawler import Crawler
from .interface import CrawlerInterface

class CrawlerAnimesOnline(Crawler, CrawlerInterface):
    """Crawler responsável pelo site animesonline.
    """

    def get_last_episode(self, url: str) -> str:
        """Função responsável por retornar o número do último episódio do 
        anime.

        Args:
            url (str): Url do site.

        Returns:
            str
        """

        soup = self.req_webpage(url=url)

        for episodes in soup.find_all('div', class_='episodiotitle'):
            lastEpisode = episodes.contents[0].contents[0]
            lastEpisodeNumber = search(r'\d+', lastEpisode).group()

        return lastEpisodeNumber

    def get_last_episode_url(self, url: str) -> str:
        """Função responsável por retornar a url do último episódio do anime.

        Args:
            url (str): Url do site.

        Returns:
            str
        """
        
        soup = self.req_webpage(url=url)

        for episodes in soup.find_all('div', class_='episodiotitle'):
            episodeUrl = episodes.find('a')

        return episodeUrl.attrs['href']
