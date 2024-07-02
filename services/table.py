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
        my_episodes: list,
        last_episodes: list,
        last_episodesUrls: list,
        broadcasts: list
    ) -> None:
        """Preenche a tabela com as informações passadas.

        Args:
            names (list): Nomes dos animes.
            seasons (list): Temporadas dos animes.
            urls (list):  URLs dos animes.
            my_episodes (list): Episódio que parei dos animes.
            last_episodes (list): Últimos episódios dos animes.
            last_episodesUrls (list): URLS dos últimos episódios dos animes.
            broadcasts (list): Dia de lançamento de novos episódios dos animes.
        """

        if (
            len(names) > 0 and
            len(seasons) > 0 and
            len(urls) > 0 and
            len(my_episodes) > 0 and
            len(last_episodes) > 0 and
            len(last_episodesUrls) > 0 and
            len(broadcasts) > 0
        ):
            try:
                for i in track(range(len(names)), description="[cyan]Montando a tabela"):
                    self.table.add_row(
                        str(i + 1),
                        names[i],
                        seasons[i],
                        shorten_url(urls[i]),
                        my_episodes[i],
                        last_episodes[i],
                        ("[red]" if float(my_episodes[i]) < float(last_episodes[i]) else "[green]") + shorten_url(last_episodesUrls[i]),
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
