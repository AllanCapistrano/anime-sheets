import gspread
from oauth2client.service_account import ServiceAccountCredentials

# ------------------------------ Constants ----------------------------------- #
CREDS_FILE = "creds.json"
SHEET_TITLE = "Animes"
COL_URL = 3
COL_IM = 4
COL_LE = 5
COL_LEU = 6
COL_LE_NAME = 'F'
# ---------------------------------------------------------------------------- #

scope = [
    "https://spreadsheets.google.com/feeds",
    'https://www.googleapis.com/auth/spreadsheets',
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

# Definindo as credenciais
creds = ServiceAccountCredentials.from_json_keyfile_name(CREDS_FILE, scope)

# Definindo o client
client = gspread.authorize(creds)

# Abrindo a planilha
sheet = client.open(SHEET_TITLE).sheet1

def getAnimeUrl() -> list:
    """ Função que retorna uma lista com as URL dos animes que estão na planilha.

    Returns
    -----------
    animeUrl: :class:`list`
    """

    animeUrl = sheet.col_values(COL_URL)
    animeUrl.pop(0)

    return animeUrl

def getIm() -> list:
    """ Função que retorna uma lista com os episódios que parei dos animes que 
    estão na planilha.

    Returns
    -----------
    im: :class:`list`
    """

    im = sheet.col_values(COL_IM)
    im.pop(0)

    return im


def getLastEpisode() -> list:
    """ Função que retorna uma lista com o número do último episódio lançado 
    dos animes que estão na planilha.

    Returns
    -----------
    lastEpisode: :class:`list`
    """
    
    lastEpisode = sheet.col_values(COL_LE)
    lastEpisode.pop(0)

    return lastEpisode

def setLastEpisode(index: int, value: str):
    """ Função que altera na planilha o número do último episódio lançado.

    Parameters
    -----------
    index: :class:`int`
        Posição na planilha.
    index: :class:`str`
        Número do episódio.
    """

    sheet.update_cell(index + 2, COL_LE, value)

def setLastEpisodeUrl(index: int , value: str):
    """ Função que altera na planilha a URL do último episódio lançado.

    Parameters
    -----------
    index: :class:`int`
        Posição na planilha.
    index: :class:`str`
        Número do episódio.
    """

    sheet.update_cell(index + 2, COL_LEU, value)

def changeCellBackgroundColor(pos: int, color: list):
    """ Função para alterar a cor de fundo de uma célula na planilha.

    Parameters
    -----------
    pos: :class:`int`
        Posição na planilha.
    color: :class:`list`
        Lista com os valores RGB ([red, green, blue]). 
    """

    sheet.format(COL_LE_NAME + str(pos), {
        "backgroundColor": {
            "red": color[0],
            "green": color[1],
            "blue": color[2]
        }
    })
