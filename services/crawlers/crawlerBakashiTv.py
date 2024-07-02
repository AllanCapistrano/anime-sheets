from re import search

from .crawler import Crawler
from .interface import CrawlerInterface

# ------------------------------ Constants ----------------------------------- #
EPISODE_CLASS   = "episodiotitle"
# ---------------------------------------------------------------------------- #

class CrawlerBakashiTv(Crawler, CrawlerInterface):
    """Crawler responsável pelo site bakashi.
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

        episodes                      = soup.find_all('div', class_=EPISODE_CLASS)
        last_episode_anchor           = episodes[-1].contents[0]
        last_episode_number           = last_episode_anchor.contents[0]
        last_episode_number_sanitized = search(r'\d+', last_episode_number).group()

        return last_episode_number_sanitized

    def get_last_episode_url(self, url: str) -> str:
        """Função responsável por retornar a url do último episódio do anime.

        Args:
            url (str): Url do site.

        Returns:
            str
        """

        soup = self.req_webpage(url=url)

        episodes            = soup.find_all('div', class_=EPISODE_CLASS)
        last_episode_anchor = episodes[-1].contents[0]
        last_episode_url    = last_episode_anchor.attrs["href"]

        return last_episode_url
