import requests
from bs4 import BeautifulSoup

class Crawler:

  #Função para buscar o site pela URL
  def reqUrl(self, url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'lxml')

    return soup

  #Função que retorna o número da última temporada lançada.
  def getLastSeason(self, url):
    soup = self.reqUrl(url)
    list_seasons_html = soup.find_all('span', class_='se-t')
    numSeasons = len(list_seasons_html)
    lastSeason = int(list_seasons_html[numSeasons - 1].contents[0])

    return lastSeason


  #Funçaõ que retorna o número do último episódio lançado.
  def getLastEpisode(self, url):
    soup = self.reqUrl(url)
    list_episodes_html = soup.find_all('div', class_='numerando')

    for episode in list_episodes_html:
      lastEpisode = episode.contents[0]

    lastEpisode = lastEpisode.split('-')

    return lastEpisode[1]

  #Funçaõ que retorna o link do último episódio lançado.
  def getLastEpisodeLink(self, url):
    soup = self.reqUrl(url)
    list_links_html = soup.find_all('div', class_='episodiotitle')

    for link_html in list_links_html:
      lastEpisodeLink_html = link_html.find('a')

    return lastEpisodeLink_html.attrs['href']