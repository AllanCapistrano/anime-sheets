import requests
from bs4 import BeautifulSoup

class CrawlerAnimesHouseAndAnimesOnline:
  def reqUrl(self, url: str) -> BeautifulSoup:
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