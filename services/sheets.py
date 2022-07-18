import gspread
from oauth2client.service_account import ServiceAccountCredentials

# ------------------------------ Constants ----------------------------------- #
CREDENTIALS_FILE = "creds.json"
SHEET_TITLE = "Animes"
COL_NUMBER_ANIME_NAME = 1
COL_NUMBER_SEASON = 2
COL_NUMBER_URL = 3
COL_NUMBER_MY_EPISODES = 4
COL_NUMBER_LAST_EPISODE = 5
COL_NUMBER_LAST_EPISODE_URL = 6
COL_NAME_LAST_EPISODE = 'F'
# ---------------------------------------------------------------------------- #

scope = [
    "https://spreadsheets.google.com/feeds",
    'https://www.googleapis.com/auth/spreadsheets',
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

# Definindo as credenciais
creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, scope)

# Definindo o client
client = gspread.authorize(creds)

# Abrindo a planilha
sheet = client.open(SHEET_TITLE).sheet1

def getAnimeNames() -> list:
    """ Função que retorna uma lista com os nomes dos animes que estão na 
    planilha.

    Returns
    -----------
    animeNames: :class:`list`
    """

    animeNames = sheet.col_values(COL_NUMBER_ANIME_NAME)
    animeNames.pop(0)

    return animeNames

def getAnimeSeasons() -> list:
    """ Função que retorna uma lista com os números das temporadas dos animes 
    que estão na planilha.

    Returns
    -----------
    animeSeasons: :class:`list`
    """

    animeSeasons = sheet.col_values(COL_NUMBER_ANIME_NAME)
    animeSeasons.pop(0)

    return animeSeasons

def getAnimeUrls() -> list:
    """ Função que retorna uma lista com as URL dos animes que estão na planilha.

    Returns
    -----------
    animeUrls: :class:`list`
    """

    animeUrls = sheet.col_values(COL_NUMBER_URL)
    animeUrls.pop(0)

    return animeUrls

def getMyEpisodes() -> list:
    """ Função que retorna uma lista com os episódios que parei dos animes que 
    estão na planilha.

    Returns
    -----------
    myEpisodes: :class:`list`
    """

    myEpisodes = sheet.col_values(COL_NUMBER_MY_EPISODES)
    myEpisodes.pop(0)

    return myEpisodes

def getLastEpisodes() -> list:
    """ Função que retorna uma lista com o número do último episódio lançado 
    dos animes que estão na planilha.

    Returns
    -----------
    lastEpisodes: :class:`list`
    """
    
    lastEpisodes = sheet.col_values(COL_NUMBER_LAST_EPISODE)
    lastEpisodes.pop(0)

    return lastEpisodes

def setLastEpisode(index: int, value: str):
    """ Função que altera na planilha o número do último episódio lançado.

    Parameters
    -----------
    index: :class:`int`
        Posição na planilha.
    index: :class:`str`
        Número do episódio.
    """

    sheet.update_cell(index + 2, COL_NUMBER_LAST_EPISODE, value)

def setLastEpisodeUrl(index: int , value: str):
    """ Função que altera na planilha a URL do último episódio lançado.

    Parameters
    -----------
    index: :class:`int`
        Posição na planilha.
    index: :class:`str`
        Número do episódio.
    """

    sheet.update_cell(index + 2, COL_NUMBER_LAST_EPISODE_URL, value)

def changeCellBackgroundColor(pos: int, color: list):
    """ Função para alterar a cor de fundo de uma célula na planilha.

    Parameters
    -----------
    pos: :class:`int`
        Posição na planilha.
    color: :class:`list`
        Lista com os valores RGB ([red, green, blue]). 
    """

    sheet.format(COL_NAME_LAST_EPISODE + str(pos), {
        "backgroundColor": {
            "red": color[0],
            "green": color[1],
            "blue": color[2]
        }
    })
