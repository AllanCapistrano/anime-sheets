from os import system, name
from sys import exit
from time import time
from rich.console import Console

from modules.showOptions import showOptions
from modules.updateSheet import updateSheet
from modules.showTable import showTable

if __name__ == "__main__":
    console       = Console()
    clearTerminal = True

    while(True):
        showOptions(clearTerminal=clearTerminal)
        option = input("Escolha uma das opções acima: ")

        try:
            option        = int(option)
            clearTerminal = True
        except:
            system('cls' if name == 'nt' else 'clear')

            console.print("Opção inválida! Tente novamente.\n", style="bold red")
            clearTerminal = False
        else:
            match option:
                case 1: # Exibir tabela
                    system('cls' if name == 'nt' else 'clear')

                    start = time()
                    updateSheet()
                    showTable()
                    end = time()

                    console.print("Tempo de execução: {:.2f}s".format(end - start), style="bold green")
                    input("\nPressione Enter para voltar...")
                case 2: # Mais informações de um Anime
                    system('cls' if name == 'nt' else 'clear')

                    start = time()
                    # TODO
                    end = time()

                    console.print("Tempo de execução: {:.2f}s".format(end - start), style="bold green")
                    input("\nPressione Enter para voltar...")
                    raise NotImplementedError("Método ainda não implementado")
                case 3: # Atualizar informações de um Anime
                    system('cls' if name == 'nt' else 'clear')

                    start = time()
                    # TODO
                    end = time()

                    console.print("Tempo de execução: {:.2f}s".format(end - start), style="bold green")
                    input("\nPressione Enter para voltar...")
                    raise NotImplementedError("Método ainda não implementado")
                case 4: # Atualizar último episódio assistido
                    system('cls' if name == 'nt' else 'clear')

                    start = time()
                    # TODO
                    end = time()

                    console.print("Tempo de execução: {:.2f}s".format(end - start), style="bold green")
                    input("\nPressione Enter para voltar...")
                    raise NotImplementedError("Método ainda não implementado")
                case 5: # Atualizar planilha
                    system('cls' if name == 'nt' else 'clear')

                    start = time()
                    updateSheet(showLog=True)
                    end = time()

                    console.print("Tempo de execução: {:.2f}s".format(end - start), style="bold green")
                    input("\nPressione Enter para voltar...")
                case 6:
                    console.print("\nAté logo!", style="bold")
                    exit()
                case _:
                    system('cls' if name == 'nt' else 'clear')

                    console.print("Opção inválida! Tente novamente.\n", style="bold red")
                    clearTerminal = False