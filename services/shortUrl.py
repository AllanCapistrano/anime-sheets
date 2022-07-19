from os import getenv
from dotenv import load_dotenv
import pyshorteners

load_dotenv()

# ------------------------------ Constants ----------------------------------- #
SHORT_URL    = getenv("SHORT_URL")
BITLY_TOKEN  = getenv("BITLY_TOKEN")
# ---------------------------------------------------------------------------- #

def shortenUrl(url: str) -> str:
    """ Encurta uma URL caso seja fornecido o token de acesso.

    Parameters
    -----------
    url: :class:`str`
        URL a ser encurtada

    Returns
    -----------
    shortUrl: :class:`str`
    """

    if(BITLY_TOKEN != ""):
        try:
            bitlyShorten = pyshorteners.Shortener(api_key=BITLY_TOKEN)

            return bitlyShorten.bitly.short(url)
        except:
            raise ValueError("Erro! Token de acesso inválido.") 
    
    return url