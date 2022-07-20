from os import system, name
from rich.console import Console

def showOptions(clearTerminal: bool = True) -> None:
    """ Exibe as opções da CLI.

    Parameters
    -----------
    clearTerminal: :class:`bool`
        Flag para limpar ou não o terminal antes da exibição das opções.
    """
    
    console = Console()

    if(clearTerminal):
        system('cls' if name == 'nt' else 'clear')

    console.print("[1] Exibir tabela", style="bold")
    console.print("[2] Mais informações de um Anime", style="bold")
    console.print("[3] Atualizar informações de um Anime", style="bold")
    console.print("[4] Atualizar último episódio assistido", style="bold")
    console.print("[5] Atualizar planilha", style="bold")
    console.print("[6] Sair", style="bold")