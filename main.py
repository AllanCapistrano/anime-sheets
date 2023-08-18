from os import getenv
from time import time
from dotenv import load_dotenv
from rich.progress import track
from rich.console import Console

from services.sheet import Sheet
from services.crawlers.crawlerAnimesHouseAndAnimesGratis import CrawlerAnimesHouseAndAnimesGratis
from services.crawlers.crawlerAnimesOnline import CrawlerAnimesOnline
from services.crawlers.crawlerGoyabuOld import CrawlerGoyabuOld as CrawlerGoyabu
from services.table import Table

load_dotenv()

# ------------------------------ Constants ----------------------------------- #
USER_NAME  = getenv("USER_NAME")
SHEET_LINK = getenv("SHEET_LINK")
# ---------------------------------------------------------------------------- #

console = Console()
table   = Table()

try:
    sheet = Sheet()
except Exception as error:
    print()
    console.print(error, style="bold red")
    
    exit()

start = time()

crawlerAnimesHouseAndAnimesGratis = CrawlerAnimesHouseAndAnimesGratis()
crawlerAnimesOnline               = CrawlerAnimesOnline()
crawlerGoyabu                     = CrawlerGoyabu()

animeNames        = sheet.getAnimeNames()
animeSeasons      = sheet.getAnimeSeasons()
animesUrls        = sheet.getAnimeUrls()
myEpisodes        = sheet.getMyEpisodes()
lastEpisodesSheet = sheet.getLastEpisodes()
animeBroadcasts   = sheet.getAnimeBroadcasts()

lastEpisodesUpdated     = []
lastEpisodesUrlsUpdated = []

for i in track(range(0, len(animesUrls)), description="[cyan]Atualizando..."):
    # Verifica qual é o site que está sendo utilizado para assistir o anime.
    if(animesUrls[i].find("animesonline")  != -1):
        lastEpisode    = crawlerAnimesOnline.getLastEpisode(animesUrls[i])
        lastEpisodeUrl = crawlerAnimesOnline.getLastEpisodeUrl(animesUrls[i])
    elif(
        animesUrls[i].find("animeshouse")  != -1 or 
        animesUrls[i].find("animesgratis") != -1
    ):
        lastEpisode    = crawlerAnimesHouseAndAnimesGratis.getLastEpisode(animesUrls[i])
        lastEpisodeUrl = crawlerAnimesHouseAndAnimesGratis.getLastEpisodeUrl(animesUrls[i])
    elif(animesUrls[i].find("goyabu") != -1):
        lastEpisode    = crawlerGoyabu.getLastEpisode(animesUrls[i])
        lastEpisodeUrl = crawlerGoyabu.getLastEpisodeUrl(animesUrls[i])

    lastEpisodesUpdated.append(lastEpisode)
    lastEpisodesUrlsUpdated.append(lastEpisodeUrl)

    try:
        # Evita escritas desnecessárias.
        if(lastEpisodesSheet[i] != lastEpisode):
            sheet.setLastEpisode(i, lastEpisode)
            sheet.setLastEpisodeUrl(i, lastEpisodeUrl)
    except :
        if(myEpisodes[i]):
            sheet.setLastEpisode(i, lastEpisode)
            sheet.setLastEpisodeUrl(i, lastEpisodeUrl)
    
    sheet.changeCellBackgroundColor(float(myEpisodes[i]), float(lastEpisode), i)

# Preenchendo a tabela.
table.fillTable(
    names            = animeNames, 
    seasons          = animeSeasons, 
    urls             = animesUrls, 
    myEpisodes       = myEpisodes, 
    lastEpisodes     = lastEpisodesUpdated, 
    lastEpisodesUrls = lastEpisodesUrlsUpdated, 
    broadcasts       = animeBroadcasts
)

end = time()

console.print("Tempo de execução: {:.2f}s\n".format(end - start), style="bold green")

if(USER_NAME != ""):
    console.print("Planilha de animes atualizada com sucesso {}!".format(
        USER_NAME), style="bold")
if(SHEET_LINK != ""):
    print("Link: {}".format(SHEET_LINK))

# Exibindo a tabela.
table.showTable()

print()