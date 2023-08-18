from re import search

from .crawler import Crawler
from .interface import CrawlerInterface

class CrawlerAnimesOnline(Crawler, CrawlerInterface):
    def getLastEpisode(self, url: str) -> str:
        """ Função responsável por retornar o número do último episódio do 
        anime.

        Parameters
        -----------
        url: :class:`str`
            Url do site.
            
        Returns
        -----------
        lastEpisodeNumber: :class:`str`
        """

        soup = self.reqUrl(url)

        for episodes in soup.find_all('div', class_='episodiotitle'):
            lastEpisode = episodes.contents[0].contents[0]
            lastEpisodeNumber = search(r'\d', lastEpisode).group()

        return lastEpisodeNumber

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
    
if __name__ == "__main__":
    crawler = CrawlerAnimesOnline()

    print(crawler.getLastEpisode("https://animesonline.nz/animes/watashi-no-shiawase-na-kekkon/"))
    print(crawler.getLastEpisodeUrl("https://animesonline.nz/animes/watashi-no-shiawase-na-kekkon/"))