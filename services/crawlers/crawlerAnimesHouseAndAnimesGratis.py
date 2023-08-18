from services.crawlers.crawler import Crawler
from services.crawlers.interface.crawlerInterface import CrawlerInterface

class CrawlerAnimesHouseAndAnimesGratis(Crawler, CrawlerInterface):
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

        for episodes in soup.find_all('div', class_='numerando'):
            lastEpisode = episodes.contents[0]

        return lastEpisode.split('- ')[1]

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

        for episodes in soup.find_all('div', class_='episodiotitle'):
            episodeUrl = episodes.find('a')

        return episodeUrl.attrs['href']