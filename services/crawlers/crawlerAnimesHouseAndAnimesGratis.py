from .crawler import Crawler
from .interface import CrawlerInterface

class CrawlerAnimesHouseAndAnimesGratis(Crawler, CrawlerInterface):
    """Crawler responsável pelos sites animeshouse e animesgratis.
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

        for episodes in soup.find_all('div', class_='numerando'):
            last_episode = episodes.contents[0]

        return last_episode.split('- ')[1]

    def get_last_episode_url(self, url: str) -> str:
        """Função responsável por retornar a url do último episódio do anime.

        Args:
            url (str): Url do site.

        Returns:
            str
        """

        soup = self.req_url(url)

        for episodes in soup.find_all('div', class_='episodiotitle'):
            episode_url = episodes.find('a')

        return episode_url.attrs['href']
