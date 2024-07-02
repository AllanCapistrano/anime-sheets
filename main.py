from os import getenv
from time import time
from dotenv import load_dotenv
from rich.progress import track
from rich.console import Console

from services import Sheet, Table, delete_webpage
from services.crawlers import CrawlerAnimesHouseAndAnimesGratis
from services.crawlers import CrawlerAnimesOnline
from services.crawlers import CrawlerGoyabu
from services.crawlers import CrawlerBakashiTv
from services.crawlers import CrawlerAssistirAnimes

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

crawlerAnimesHouseAndAnimesGratis = CrawlerAnimesHouseAndAnimesGratis()
crawlerAnimesOnline               = CrawlerAnimesOnline()
crawlerGoyabu                     = CrawlerGoyabu()
crawlerBakashiTv                  = CrawlerBakashiTv()
crawlerAssistirAnimes             = CrawlerAssistirAnimes()

animeNames        = sheet.get_anime_names()
animeSeasons      = sheet.get_anime_seasons()
animesUrls        = sheet.get_anime_urls()
myEpisodes        = sheet.get_my_episodes()
lastEpisodesSheet = sheet.get_last_episodes()
animeBroadcasts   = sheet.get_anime_broadcasts()

lastEpisodesUpdated     = []
lastEpisodesUrlsUpdated = []

for i in track(range(0, len(animesUrls)), description="[cyan]Atualizando..."):
    # Verifica qual é o site que está sendo utilizado para assistir o anime.
    if(animesUrls[i].find("animesonline")  != -1):
        lastEpisode    = crawlerAnimesOnline.get_last_episode(animesUrls[i])
        lastEpisodeUrl = crawlerAnimesOnline.get_last_episode_url(animesUrls[i])
    elif(
        animesUrls[i].find("animeshouse")  != -1 or 
        animesUrls[i].find("animesgratis") != -1
    ):
        lastEpisode    = crawlerAnimesHouseAndAnimesGratis.get_last_episode(animesUrls[i])
        lastEpisodeUrl = crawlerAnimesHouseAndAnimesGratis.get_last_episode_url(animesUrls[i])
    elif(animesUrls[i].find("goyabu") != -1):
        lastEpisode    = crawlerGoyabu.get_last_episode(animesUrls[i])
        lastEpisodeUrl = crawlerGoyabu.get_last_episode_url(animesUrls[i])
    elif(animesUrls[i].find("bakashi")  != -1):
        lastEpisode    = crawlerBakashiTv.get_last_episode(animesUrls[i])
        lastEpisodeUrl = crawlerBakashiTv.get_last_episode_url(animesUrls[i])
    elif(animesUrls[i].find("assistiranimes")  != -1):
        lastEpisode    = crawlerAssistirAnimes.get_last_episode(animesUrls[i])
        lastEpisodeUrl = crawlerAssistirAnimes.get_last_episode_url(animesUrls[i])
    else:
        print("Erro! Site não suportado.")
        exit()

    lastEpisodesUpdated.append(lastEpisode)
    lastEpisodesUrlsUpdated.append(lastEpisodeUrl)

    try:
        # Evita escritas desnecessárias.
        if(lastEpisodesSheet[i] != lastEpisode):
            sheet.set_last_episode(i, lastEpisode)
            sheet.set_last_episode_url(i, lastEpisodeUrl)
    except IndexError:
        if(myEpisodes[i]):
            sheet.set_last_episode(i, lastEpisode)
            sheet.set_last_episode_url(i, lastEpisodeUrl)

    sheet.change_cell_background_color(float(myEpisodes[i]), float(lastEpisode), i)

# Removendo a página web do último anime da lista
delete_webpage()

# Preenchendo a tabela.
table.fill_table(
    names            = animeNames, 
    seasons          = animeSeasons, 
    urls             = animesUrls, 
    myEpisodes       = myEpisodes, 
    lastEpisodes     = lastEpisodesUpdated, 
    lastEpisodesUrls = lastEpisodesUrlsUpdated, 
    broadcasts       = animeBroadcasts
)

end = time()

execution_time = end - start

console.print(f"Tempo de execução: {execution_time:.2f}s\n", style="bold green")

if(USER_NAME != ""):
    console.print(f"Planilha de animes atualizada com sucesso {USER_NAME}!", style="bold")
if(SHEET_LINK != ""):
    print(f"Link: {SHEET_LINK}")

# Exibindo a tabela.
table.show_table()

print()