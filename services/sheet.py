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
COL_NUMBER_BROADCAST = 7
COL_NAME_LAST_EPISODE = 'F'
COLOR_OK     = [0, 1, 0]
COLOR_NOT_OK = [1, 0, 0]
# ---------------------------------------------------------------------------- #

class Sheet:
    def __init__(self) -> None:
        """ Método construtor.
        """

        self.scope = [
            "https://spreadsheets.google.com/feeds",
            'https://www.googleapis.com/auth/spreadsheets',
            "https://www.googleapis.com/auth/drive.file",
            "https://www.googleapis.com/auth/drive"
        ]

        # Definindo as credenciais
        self.creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, self.scope)
        # Definindo o client
        self.client = gspread.authorize(self.creds)
        # Abrindo a planilha
        self.sheet = self.client.open(SHEET_TITLE).sheet1

    def getAnimeNames(self) -> list:
        """ Função que retorna uma lista com os nomes dos animes que estão na 
        planilha.

        Returns
        -----------
        animeNames: :class:`list`
        """

        animeNames = self.sheet.col_values(COL_NUMBER_ANIME_NAME)
        animeNames.pop(0)

        return animeNames

    def getAnimeSeasons(self) -> list:
        """ Função que retorna uma lista com os números das temporadas dos 
        animes que estão na planilha.

        Returns
        -----------
        animeSeasons: :class:`list`
        """

        animeSeasons = self.sheet.col_values(COL_NUMBER_SEASON)
        animeSeasons.pop(0)

        return animeSeasons

    def getAnimeUrls(self) -> list:
        """ Função que retorna uma lista com as URL dos animes que estão na 
        planilha.

        Returns
        -----------
        animeUrls: :class:`list`
        """

        animeUrls = self.sheet.col_values(COL_NUMBER_URL)
        animeUrls.pop(0)

        return animeUrls

    def getMyEpisodes(self) -> list:
        """ Função que retorna uma lista com os episódios que parei dos animes 
        que estão na planilha.

        Returns
        -----------
        myEpisodes: :class:`list`
        """

        myEpisodes = self.sheet.col_values(COL_NUMBER_MY_EPISODES)
        myEpisodes.pop(0)

        return myEpisodes

    def getLastEpisodes(self) -> list:
        """ Função que retorna uma lista com o número do último episódio lançado 
        dos animes que estão na planilha.

        Returns
        -----------
        lastEpisodes: :class:`list`
        """
        
        lastEpisodes = self.sheet.col_values(COL_NUMBER_LAST_EPISODE)
        lastEpisodes.pop(0)

        return lastEpisodes

    def getAnimeBroadcasts(self) -> list:
        """ Função que retorna uma lista com os dias de lançamentos dos animes 
        que estão na planilha.

        Returns
        -----------
        animeBroadcasts: :class:`list`
        """

        animeBroadcasts = self.sheet.col_values(COL_NUMBER_BROADCAST)
        animeBroadcasts.pop(0)

        return animeBroadcasts

    def setLastEpisode(self, index: int, value: str) -> None:
        """ Função que altera na planilha o número do último episódio lançado.

        Parameters
        -----------
        index: :class:`int`
            Posição na planilha.
        index: :class:`str`
            Número do episódio.
        """

        self.sheet.update_cell(index + 2, COL_NUMBER_LAST_EPISODE, value)

    def setLastEpisodeUrl(self, index: int , value: str) -> None:
        """ Função que altera na planilha a URL do último episódio lançado.

        Parameters
        -----------
        index: :class:`int`
            Posição na planilha.
        index: :class:`str`
            Número do episódio.
        """

        self.sheet.update_cell(index + 2, COL_NUMBER_LAST_EPISODE_URL, value)

    def setCellBackgroundColor(self, pos: int, color: list) -> None:
        """ Função para alterar a cor de fundo de uma célula na planilha.

        Parameters
        -----------
        pos: :class:`int`
            Posição na planilha.
        color: :class:`list`
            Lista com os valores RGB ([red, green, blue]). 
        """

        self.sheet.format(COL_NAME_LAST_EPISODE + str(pos), {
            "backgroundColor": {
                "red": color[0],
                "green": color[1],
                "blue": color[2]
            }
        })

    def changeCellBackgroundColor(
        self, 
        myEpisode: float,
        lastEpisode: float, 
        pos: int
    ) -> None:
        """ Altera a cor de fundo da célula de acordo com o último episódio 
        assistido.

        Parameters
        -----------
        myEpisode: :class:`float`
            Último episódio assistido.
        lastEpisode: :class:`float`
            Último episódio lançado.
        pos: :class:`int`
            Posição na planilha da URL do último episódio lançado.
        """
        
        if(myEpisode < lastEpisode):
            self.setCellBackgroundColor(pos + 2, COLOR_NOT_OK)
        else:
            self.setCellBackgroundColor(pos + 2, COLOR_OK)