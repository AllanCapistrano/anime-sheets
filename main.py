import os
import time
from dotenv import load_dotenv
from rich.progress import track
from rich.console import Console

from services import sheets
from services.crawlers.crawlerAnimesHouseAndAnimesOnline import CrawlerAnimesHouseAndAnimesOnline
from services.crawlers.crawlerGoyabu import CrawlerGoyabu

load_dotenv()

# ------------------------------ Constants ----------------------------------- #
USER_NAME    = os.getenv("USER_NAME")
SHEET_LINK   = os.getenv("SHEET_LINK")
COLOR_OK     = [0, 1, 0]
COLOR_NOT_OK = [1, 0, 0]
# ---------------------------------------------------------------------------- #

console = Console()

start = time.time()

crawlerAnimesHouseAndAnimesOnline = CrawlerAnimesHouseAndAnimesOnline()
crawlerGoyabu                     = CrawlerGoyabu()

animeNames        = sheets.getAnimeNames()
animeSeasons      = sheets.getAnimeSeasons()
animesUrls        = sheets.getAnimeUrls()
myEpisodes        = sheets.getMyEpisodes()
lastEpisodesSheet = sheets.getLastEpisodes()

lastEpisodesUpdated     = []
lastEpisodesUrlsUpdated = []

for i in track(range(0, len(animesUrls)), description="[cyan]Atualizando..."):
    # Verifica qual é o site que está sendo utilizado para assistir o anime.
    if(
        animesUrls[i].find("animeshouse")  != -1 or 
        animesUrls[i].find("animesonline") != -1
    ):
        lastEpisode    = crawlerAnimesHouseAndAnimesOnline.getLastEpisode(animesUrls[i])
        lastEpisodeUrl = crawlerAnimesHouseAndAnimesOnline.getLastEpisodeUrl(animesUrls[i])
    elif(animesUrls[i].find("goyabu") != -1):
        lastEpisode    = crawlerGoyabu.getLastEpisode(animesUrls[i])
        lastEpisodeUrl = crawlerGoyabu.getLastEpisodeUrl(animesUrls[i])

    lastEpisodesUpdated.append(lastEpisode)
    lastEpisodesUrlsUpdated.append(lastEpisodeUrl)

    try:
        # Evita escritas desnecessárias.
        if(lastEpisodesSheet[i] != lastEpisode):
            sheets.setLastEpisode(i, lastEpisode)
            sheets.setLastEpisodeUrl(i, lastEpisodeUrl)
    except :
        if(myEpisodes[i]):
            sheets.setLastEpisode(i, lastEpisode)
            sheets.setLastEpisodeUrl(i, lastEpisodeUrl)
    
    # Muda a cor da célula, de acordo com o último episódio assistido.
    if(float(myEpisodes[i]) < float(lastEpisode)):
        sheets.changeCellBackgroundColor(i + 2, COLOR_NOT_OK)
    else:
        sheets.changeCellBackgroundColor(i + 2, COLOR_OK)

end = time.time()

console.print("Tempo de execução: {:.2f}s\n".format(end - start), style="bold green")

if(USER_NAME != ""):
    console.print("Planilha de animes atualizada com sucesso {}!".format(
        USER_NAME), style="bold")
if(SHEET_LINK != ""):
    print("Link: {}".format(SHEET_LINK))

print()