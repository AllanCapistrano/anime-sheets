from .crawler import Crawler
from .interface import CrawlerInterface

class CrawlerAnimesHouseAndAnimesGratis(Crawler, CrawlerInterface):
    """Crawler responsável pelos sites animeshouse e animesgratis.
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

        for episodes in soup.find_all('div', class_='numerando'):
            lastEpisode = episodes.contents[0]

        return lastEpisode.split('- ')[1]

    def getLastEpisodeUrl(self, url: str) -> str:
        """Função responsável por retornar a url do último episódio do anime.

        Args:
            url (str): Url do site.

        Returns:
            str
        """

        soup = self.req_url(url)

        for episodes in soup.find_all('div', class_='episodiotitle'):
            episodeUrl = episodes.find('a')

        return episodeUrl.attrs['href']
