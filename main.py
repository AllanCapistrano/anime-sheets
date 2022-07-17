import os
import time
from dotenv import load_dotenv
from rich.progress import track
from rich.console import Console

from services import sheets
from services.crawlerAnimesHouseAndAnimesOnline import CrawlerAnimesHouseAndAnimesOnline
from services.crawlerGoyabu import CrawlerGoyabu

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

animesUrls = sheets.getAnimeUrl()
im         = sheets.getIm()
size       = len(animesUrls)

lastEpisodeSheet = sheets.getLastEpisode()

for i in track(range(0, size), description="[cyan]Atualizando..."):
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

    try:
        # Evita escritas desnecessárias.
        if(lastEpisodeSheet[i] != lastEpisode):
            sheets.setLastEpisode(i, lastEpisode)
            sheets.setLastEpisodeUrl(i, lastEpisodeUrl)
    except :
        if(im[i]):
            sheets.setLastEpisode(i, lastEpisode)
            sheets.setLastEpisodeUrl(i, lastEpisodeUrl)
    
    # Muda a cor da célula, de acordo com o último episódio assistido.
    if(float(im[i]) < float(lastEpisode)):
        sheets.changeCellBackgroundColor(i + 2, COLOR_NOT_OK)
    else:
        sheets.changeCellBackgroundColor(i + 2, COLOR_OK)

    percentage = 100 * (i + 1)/size

end = time.time()

console.print("Tempo de execução: {:.2f}s\n".format(end - start), style="bold green")

if(USER_NAME != ""):
    console.print("Planilha de animes atualizada com sucesso {}!".format(
        USER_NAME), style="bold")
if(SHEET_LINK != ""):
    print("Link: {}".format(SHEET_LINK))

print()