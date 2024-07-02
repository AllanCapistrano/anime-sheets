from subprocess import run, CalledProcessError, PIPE

# ------------------------------ Constants ----------------------------------- #
DIRECTORY_PATH = "web"
# ---------------------------------------------------------------------------- #

def get_webpage(url: str, webpage_name: str = "index.html") -> None:
    """Baixa uma página de um determinado site no formato HTML.

    Args:
        url (str): Url do site.
        webpage_name (str, optional): Nome do arquivo. Por padrão é "index.html".
    """

    webpage_name = f"{DIRECTORY_PATH}/{webpage_name}"

    command = ["curl", "--silent", url, "-o", webpage_name]

    try:
        run(command, check=False)
    except CalledProcessError:
        print(f"Error trying to get '{url}'.")
        exit()

def delete_webpage(webpage_name: str = "index.html") -> None:
    """Remove, caso exista, uma página web salva.

    Args:
        webpage_name (str, optional): Nome do arquivo. Por padrão é "index.html".
    """

    webpage_name = f"{DIRECTORY_PATH}/{webpage_name}"

    command = ["rm", webpage_name]

    try:
        run(command, check=False)
    except CalledProcessError:
        print(f"Error trying to remove '{webpage_name}'.")
        exit()

def list_webpages() -> list:
    """Lista quais são as páginas web baixadas.

    Returns:
        list
    """

    command = ["ls", "./web"]

    try:
        result = run(command, stdout=PIPE, stderr=PIPE, text=True, check=True)

        webpages = result.stdout.split("\n")
        
        webpages_filtered = [line for line in webpages if line.strip()]

        return webpages_filtered
    except CalledProcessError:
        print("Error trying to list the web pages'.")
        exit()
