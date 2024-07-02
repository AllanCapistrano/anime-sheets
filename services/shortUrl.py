from os import getenv
from dotenv import load_dotenv
import pyshorteners

load_dotenv()

# ------------------------------ Constants ----------------------------------- #
SHORT_URL    = getenv("SHORT_URL")
BITLY_TOKEN  = getenv("BITLY_TOKEN")
# ---------------------------------------------------------------------------- #

def shorten_url(url: str) -> str:
    """Encurta uma URL caso seja fornecido o token de acesso.

    Args:
        url (str): URL a ser encurtada

    Raises:
        ValueError: Token de acesso do Bitly incorreto.

    Returns:
        str
    """

    if (BITLY_TOKEN != ""):
        try:
            bitlyShorten = pyshorteners.Shortener(api_key=BITLY_TOKEN)

            return bitlyShorten.bitly.short(url)
        except ValueError as ve:
            raise ValueError("Erro! Token de acesso inválido.") from ve

    return url
