from os import getenv
from gspread import authorize
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv

load_dotenv()

# ------------------------------ Constants ----------------------------------- #
CREDENTIALS_FILE            = getenv("CREDENTIALS_FILE")
SHEET_TITLE                 = "Animes"
COL_NUMBER_ANIME_NAME       = 1
COL_NUMBER_SEASON           = 2
COL_NUMBER_URL              = 3
COL_NUMBER_MY_EPISODES      = 4
COL_NUMBER_LAST_EPISODE     = 5
COL_NUMBER_LAST_EPISODE_URL = 6
COL_NUMBER_BROADCAST        = 7
COL_NAME_LAST_EPISODE       = 'F'
COLOR_OK                    = [0, 1, 0]
COLOR_NOT_OK                = [1, 0, 0]
# ---------------------------------------------------------------------------- #

class Sheet:
    """Classe responsável por lidar com o Google Planilhas
    """

    def __init__(self) -> None:
        """ Método construtor.
        """

        if(CREDENTIALS_FILE == ""):
            raise ValueError("Erro! É necessário informar o arquivo de credenciais.")

        self.scope = [
            "https://spreadsheets.google.com/feeds",
            'https://www.googleapis.com/auth/spreadsheets',
            "https://www.googleapis.com/auth/drive.file",
            "https://www.googleapis.com/auth/drive"
        ]

        # Definindo as credenciais.
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, self.scope)
        # Definindo o client.
        self.client = authorize(self.credentials)
        # Abrindo a planilha.
        self.sheet = self.client.open(SHEET_TITLE).sheet1

    def get_anime_names(self) -> list:
        """Retorna uma lista com os nomes dos animes que estão na planilha.

        Returns:
            list
        """

        animeNames = self.sheet.col_values(COL_NUMBER_ANIME_NAME)
        animeNames.pop(0)

        return animeNames

    def get_anime_seasons(self) -> list:
        """Retorna uma lista com os números das temporadas dos animes que estão 
        na planilha.

        Returns:
            list
        """

        animeSeasons = self.sheet.col_values(COL_NUMBER_SEASON)
        animeSeasons.pop(0)

        return animeSeasons

    def get_anime_urls(self) -> list:
        """Retorna uma lista com as URL dos animes que estão na planilha.

        Returns:
            list
        """

        animeUrls = self.sheet.col_values(COL_NUMBER_URL)
        animeUrls.pop(0)

        return animeUrls

    def get_my_episodes(self) -> list:
        """Retorna uma lista com os episódios que parei dos animes que estão na 
        planilha.

        Returns:
            list
        """

        myEpisodes = self.sheet.col_values(COL_NUMBER_MY_EPISODES)
        myEpisodes.pop(0)

        return myEpisodes

    def get_last_episodes(self) -> list:
        """Retorna uma lista com o número do último episódio lançado dos animes 
        que estão na planilha.

        Returns:
            list
        """

        lastEpisodes = self.sheet.col_values(COL_NUMBER_LAST_EPISODE)
        lastEpisodes.pop(0)

        return lastEpisodes

    def get_anime_broadcasts(self) -> list:
        """Retorna uma lista com os dias de lançamentos dos animes que estão na 
        planilha.

        Returns:
            list
        """

        animeBroadcasts = self.sheet.col_values(COL_NUMBER_BROADCAST)
        animeBroadcasts.pop(0)

        return animeBroadcasts

    def set_last_episode(self, index: int, value: str) -> None:
        """Altera na planilha o número do último episódio lançado.

        Args:
            index (int): Posição na planilha.
            value (str): Número do episódio.
        """

        self.sheet.update_cell(index + 2, COL_NUMBER_LAST_EPISODE, value)

    def set_last_episode_url(self, index: int , value: str) -> None:
        """Altera na planilha a URL do último episódio lançado.

        Args:
            index (int): Posição na planilha.
            value (str):  URL do episódio.
        """

        self.sheet.update_cell(index + 2, COL_NUMBER_LAST_EPISODE_URL, value)

    def set_cell_background_color(self, posX: str, posY: int, color: list) -> None:
        """Alterar a cor de fundo de uma célula na planilha.

        Args:
            posX (str): Posição na planilha, eixo X.
            posY (int): Posição na planilha, eixo Y.
            color (list): Lista com os valores RGB ([red, green, blue]). 
        """

        self.sheet.format(posX + str(posY), {
            "backgroundColor": {
                "red": color[0],
                "green": color[1],
                "blue": color[2]
            }
        })

    def change_cell_background_color(
        self, 
        myEpisode: float,
        lastEpisode: float, 
        pos: int
    ) -> None:
        """Altera a cor de fundo da célula de acordo com o último episódio 
        assistido.

        Args:
            myEpisode (float): Último episódio assistido.
            lastEpisode (float): Último episódio lançado.
            pos (int): Posição na planilha da URL do último episódio lançado.
        """

        if(myEpisode < lastEpisode):
            self.set_cell_background_color(COL_NAME_LAST_EPISODE, pos + 2, COLOR_NOT_OK)
        else:
            self.set_cell_background_color(COL_NAME_LAST_EPISODE, pos + 2, COLOR_OK)
