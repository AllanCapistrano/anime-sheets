from os import system, name
from sys import exit
from time import time
from rich.console import Console

from modules.updateSheet import updateSheet
from modules.showTable import showTable

if __name__ == "__main__":
    console = Console()

    # TODO: Criar módulo de exibição de opções
    system('cls' if name == 'nt' else 'clear')
    console.print("[1] Exibir tabela", style="bold")
    console.print("[2] Mais informações de um Anime", style="bold")
    console.print("[3] Atualizar informações de um Anime", style="bold")
    console.print("[4] Atualizar último episódio assistido", style="bold")
    console.print("[5] Atualizar planilha", style="bold")
    console.print("[6] Sair", style="bold")

    option = input("Escolha uma das opções acima: ")

    try:
        option = int(option)
    except:
        raise ValueError("Erro! Opção inválida.")

    match option:
        case 1: # Exibir tabela
            system('cls' if name == 'nt' else 'clear')

            start = time()
            updateSheet()
            showTable()
            end = time()

            console.print("Tempo de execução: {:.2f}s".format(end - start), style="bold green")
        case 2: # Mais informações de um Anime
            system('cls' if name == 'nt' else 'clear')

            start = time()
            # TODO
            end = time()

            console.print("Tempo de execução: {:.2f}s".format(end - start), style="bold green")
            raise NotImplementedError("Método ainda não implementado")
        case 3: # Atualizar informações de um Anime
            system('cls' if name == 'nt' else 'clear')

            start = time()
            # TODO
            end = time()

            console.print("Tempo de execução: {:.2f}s".format(end - start), style="bold green")
            raise NotImplementedError("Método ainda não implementado")
        case 4: # Atualizar último episódio assistido
            system('cls' if name == 'nt' else 'clear')

            start = time()
            # TODO
            end = time()

            console.print("Tempo de execução: {:.2f}s".format(end - start), style="bold green")
            raise NotImplementedError("Método ainda não implementado")
        case 5: # Atualizar planilha
            system('cls' if name == 'nt' else 'clear')

            start = time()
            updateSheet(showLog=True)
            end = time()

            console.print("Tempo de execução: {:.2f}s".format(end - start), style="bold green")
        case 6:
            system('cls' if name == 'nt' else 'clear')
            
            console.print("Até logo!", style="bold")
            exit()
        
        case _:
            console.print("Opção inválida! Tente novamente.", style="bold red")

            exit() # Temporário