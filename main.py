from os import getenv
from time import time
from dotenv import load_dotenv
from rich.progress import track
from rich.console import Console

from services import Sheet, Table, delete_webpage
from services.crawlers import CrawlerAnimesGratis
from services.crawlers import CrawlerAnimesOnline
from services.crawlers import CrawlerGoyabu
from services.crawlers import CrawlerBakashiTv
from services.crawlers import CrawlerAssistirAnimes
from services.crawlers import CrawlerAnimesHouse

load_dotenv()

# ------------------------------ Constants ----------------------------------- #
USER_NAME  = getenv("USER_NAME")
SHEET_LINK = getenv("SHEET_LINK")
# ---------------------------------------------------------------------------- #

console = Console()
table   = Table()

try:
    sheet = Sheet()
except ValueError as ve:
    print()
    console.print(ve, style="bold red")

    exit()

start = time()

anime_names        = sheet.get_anime_names()
anime_seasons      = sheet.get_anime_seasons()
animes_urls         = sheet.get_anime_urls()
my_episodes        = sheet.get_my_episodes()
last_episodesSheet = sheet.get_last_episodes()
anime_broadcasts   = sheet.get_anime_broadcasts()

last_episodesUpdated     = []
last_episodesUrlsUpdated = []

for i in track(range(0, len(animes_urls)), description="[cyan]Atualizando..."):
    # Verifica qual é o site que está sendo utilizado para assistir o anime.
    if (animes_urls[i].find("animesonline")  != -1):
        crawler_animes_online = CrawlerAnimesOnline()

        last_episode     = crawler_animes_online.get_last_episode(animes_urls[i])
        last_episode_url = crawler_animes_online.get_last_episode_url(animes_urls[i])
    elif (animes_urls[i].find("animesgratis") != -1):
        crawler_animes_gratis = CrawlerAnimesGratis()

        last_episode     = crawler_animes_gratis.get_last_episode(animes_urls[i])
        last_episode_url = crawler_animes_gratis.get_last_episode_url(animes_urls[i])
    elif (animes_urls[i].find("animeshouse")):
        crawler_animes_house = CrawlerAnimesHouse()

        last_episode     = crawler_animes_house.get_last_episode(animes_urls[i])
        last_episode_url = crawler_animes_house.get_last_episode_url(animes_urls[i])
    elif (animes_urls[i].find("goyabu") != -1):
        crawler_goyabu = CrawlerGoyabu()

        last_episode     = crawler_goyabu.get_last_episode(animes_urls[i])
        last_episode_url = crawler_goyabu.get_last_episode_url(animes_urls[i])
    elif (animes_urls[i].find("bakashi")  != -1):
        crawler_bakashi_tv = CrawlerBakashiTv()

        last_episode     = crawler_bakashi_tv.get_last_episode(animes_urls[i])
        last_episode_url = crawler_bakashi_tv.get_last_episode_url(animes_urls[i])
    elif (animes_urls[i].find("assistiranimes")  != -1):
        crawler_assistir_animes = CrawlerAssistirAnimes()

        last_episode     = crawler_assistir_animes.get_last_episode(animes_urls[i])
        last_episode_url = crawler_assistir_animes.get_last_episode_url(animes_urls[i])
    else:
        print("Erro! Site não suportado.")
        exit()

    last_episodesUpdated.append(last_episode)
    last_episodesUrlsUpdated.append(last_episode_url)

    try:
        # Evita escritas desnecessárias.
        if (last_episodesSheet[i] != last_episode):
            sheet.set_last_episode(i, last_episode)
            sheet.set_last_episode_url(i, last_episode_url)
    except IndexError:
        if (my_episodes[i]):
            sheet.set_last_episode(i, last_episode)
            sheet.set_last_episode_url(i, last_episode_url)

    sheet.change_cell_background_color(float(my_episodes[i]), float(last_episode), i)

# Removendo a página web do último anime da lista
delete_webpage()

# Preenchendo a tabela.
table.fill_table(
    names             = anime_names,
    seasons           = anime_seasons,
    urls              = animes_urls,
    my_episodes       = my_episodes,
    last_episodes     = last_episodesUpdated,
    last_episodesUrls = last_episodesUrlsUpdated,
    broadcasts        = anime_broadcasts
)

end = time()

execution_time = end - start

console.print(f"Tempo de execução: {execution_time:.2f}s\n", style="bold green")

if (USER_NAME != ""):
    console.print(f"Planilha de animes atualizada com sucesso {USER_NAME}!", style="bold")
if (SHEET_LINK != ""):
    print(f"Link: {SHEET_LINK}")

# Exibindo a tabela.
table.show_table()

print()
