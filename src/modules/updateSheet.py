from os import getenv
from dotenv import load_dotenv
from rich.console import Console
from rich.progress import track

from services.sheet import Sheet
from services.crawlers.crawlerAnimesHouseAndAnimesOnline import CrawlerAnimesHouseAndAnimesOnline
from services.crawlers.crawlerGoyabu import CrawlerGoyabu

load_dotenv()

# ------------------------------ Constants ----------------------------------- #
USER_NAME  = getenv("USER_NAME")
SHEET_LINK = getenv("SHEET_LINK")
# ---------------------------------------------------------------------------- #

def updateSheet(showLog: bool = False) -> None:
    """ Atualiza as informações da planilha.

    Parameters
    -----------
    showLog: :class:`bool`
        Flag para exibição das mensagens no terminal.
    """

    console = Console()

    try:
        sheet = Sheet()
    except Exception as error:
        print()
        console.print(error, style="bold red") # TODO: dar raise na exception
        exit()

    crawlerAnimesHouseAndAnimesOnline = CrawlerAnimesHouseAndAnimesOnline()
    crawlerGoyabu                     = CrawlerGoyabu()

    animesUrls        = sheet.getAnimeUrls()
    myEpisodes        = sheet.getMyEpisodes()
    lastEpisodesSheet = sheet.getLastEpisodes()

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

    print()
    if(USER_NAME != "" and showLog):
        console.print("Planilha de animes atualizada com sucesso {}!".format(
            USER_NAME), style="bold")
    if(SHEET_LINK != "" and showLog):
        print("Link: {}".format(SHEET_LINK))