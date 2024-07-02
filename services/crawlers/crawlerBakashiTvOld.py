from deprecated import deprecated

from re import search

from .crawler import Crawler
from .interface import CrawlerInterface

# ------------------------------ Constants ----------------------------------- #
ANCHOR_POSITION = 2
EPISODE_CLASS   = "epnumber"
# ---------------------------------------------------------------------------- #

@deprecated("Esta classe não é mais compatível com o site bakashi")
class CrawlerBakashiTvOld(Crawler, CrawlerInterface):
    """Crawler responsável pela antiga versão do site bakashi.
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
        last_episode                  = episodes[-1].contents[0]
        last_episode_number_sanitized = search(r'\d+', last_episode).group()

        return last_episode_number_sanitized

    def get_last_episode_url(self, url: str) -> str:
        """Função responsável por retornar a url do último episódio do anime.

        Args:
            url (str): Url do site.

        Returns:
            str
        """

        soup = self.req_webpage(url=url)

        episodes               = soup.find_all('div', class_=EPISODE_CLASS)
        last_episode_list_item = episodes[-1].parent
        last_episode_anchor    = last_episode_list_item.contents[ANCHOR_POSITION]
        last_episode_url       = last_episode_anchor.attrs["href"]

        return last_episode_url
