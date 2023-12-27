from subprocess import run

# ------------------------------ Constants ----------------------------------- #
DIRECTORY_PATH = "web"
# ---------------------------------------------------------------------------- #

def getWebpage(url: str, webpage_name: str = "index.html") -> None:
    """ Baixa uma página de um determinado site no formato HTML.

    Parameter
    ---------
    url: :class:`str`
        Url do site.
    webpage_name: :class:`str`
        Nome do arquivo. Por padrão é `index.html`.
    """

    webpage_name = f"{DIRECTORY_PATH}/{webpage_name}"

    command = ["curl", "--silent", url, "-o", webpage_name]

    try:
        run(command)
    except:
        print(f"Error trying to get '{url}'.")
        exit()

def deleteWebpage(webpage_name: str = "index.html") -> None:
    """ Remove, caso exista, uma página web salva.

    Parameter
    ---------
    webpage_name: :class:`str`
        Nome do arquivo. Por padrão é `index.html`.
    """

    webpage_name = f"{DIRECTORY_PATH}/{webpage_name}"

    command = ["rm", webpage_name]

    try:
        run(command)
    except:
        print(f"Error trying to remove '{webpage_name}'.")
        exit()
