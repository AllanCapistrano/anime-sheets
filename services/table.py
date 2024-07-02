from rich.console import Console
from rich.table import Table as RichTable
from rich.progress import track
from rich.errors import NotRenderableError

from .shortUrl import shorten_url

class Table:
    """Classe que lida com a tabela que será exibida no terminal.
    """

    def __init__(self) -> None:
        """ Método construtor.
        """

        self.console = Console()
        self.table = RichTable(show_lines=True)
        self.__create_table__()

    def __create_table__(self) -> None:
        """ Cria a tabela que será exibida no terminal.
        """

        self.table.add_column("nº", justify="center", vertical="middle")
        self.table.add_column("Anime", justify="center", vertical="middle")
        self.table.add_column("Season", justify="center", vertical="middle")
        self.table.add_column("URL", justify="center", vertical="middle")
        self.table.add_column("My Episode", justify="center", vertical="middle")
        self.table.add_column("Last Episode", justify="center", vertical="middle")
        self.table.add_column("Last Episode (URL)", justify="center", vertical="middle", no_wrap=True)
        self.table.add_column("Broadcast", justify="center", vertical="middle")

    def fill_table(
        self,
        names: list,
        seasons: list,
        urls: list,
        myEpisodes: list,
        lastEpisodes: list,
        lastEpisodesUrls: list,
        broadcasts: list
    ) -> None:
        """Preenche a tabela com as informações passadas.

        Args:
            names (list): Nomes dos animes.
            seasons (list): Temporadas dos animes.
            urls (list):  URLs dos animes.
            myEpisodes (list): Episódio que parei dos animes.
            lastEpisodes (list): Últimos episódios dos animes.
            lastEpisodesUrls (list): URLS dos últimos episódios dos animes.
            broadcasts (list): Dia de lançamento de novos episódios dos animes.
        """

        if(
            len(names) > 0 and
            len(seasons) > 0 and
            len(urls) > 0 and
            len(myEpisodes) > 0 and
            len(lastEpisodes) > 0 and
            len(lastEpisodesUrls) > 0 and
            len(broadcasts) > 0
        ):
            try:
                for i in track(range(len(names)), description="[cyan]Montando a tabela"):
                    self.table.add_row(
                        str(i + 1),
                        names[i],
                        seasons[i],
                        shorten_url(urls[i]),
                        myEpisodes[i],
                        lastEpisodes[i],
                        ("[red]" if float(myEpisodes[i]) < float(lastEpisodes[i]) else "[green]") + shorten_url(lastEpisodesUrls[i]),
                        broadcasts[i],
                    )
            except NotRenderableError as nre:
                print()
                self.console.print(nre, style="bold red")

                exit()

    def show_table(self) -> None:
        """ Exibe a tabela no terminal.
        """

        print()
        self.console.print(self.table)
