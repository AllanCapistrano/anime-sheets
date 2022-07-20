from rich.console import Console

from services.sheet import Sheet
from services.table import Table

def showTable() -> None:
    """ Exibe a tabela com as informações dos animes presentes na planilha.
    """

    console = Console()

    try:
        sheet = Sheet()
    except Exception as error:
        print()
        console.print(error, style="bold red") # TODO: dar raise na exception
        exit()

    table = Table()

    animeNames       = sheet.getAnimeNames()
    animeSeasons     = sheet.getAnimeSeasons()
    animesUrls       = sheet.getAnimeUrls()
    myEpisodes       = sheet.getMyEpisodes()
    lastEpisodes     = sheet.getLastEpisodes()
    lastEpisodesUrls = sheet.getLastEpisodesUrls()
    animeBroadcasts  = sheet.getAnimeBroadcasts()

    # Preenchendo a tabela.
    table.fillTable(
        names            = animeNames, 
        seasons          = animeSeasons, 
        urls             = animesUrls, 
        myEpisodes       = myEpisodes, 
        lastEpisodes     = lastEpisodes, 
        lastEpisodesUrls = lastEpisodesUrls, 
        broadcasts       = animeBroadcasts
    )

    # Exibindo a tabela.
    table.showTable()

    print()