import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [
  "https://spreadsheets.google.com/feeds",
  'https://www.googleapis.com/auth/spreadsheets',
  "https://www.googleapis.com/auth/drive.file",
  "https://www.googleapis.com/auth/drive"
]

# --- Constants --- #
CREDS_FILE= "creds.json"
SHEET_TITLE = "Animes"
COL_URL = 3
COL_LE = 5
COL_LEU = 6
# ---------------- #

#Definindo as credenciais
creds = ServiceAccountCredentials.from_json_keyfile_name(CREDS_FILE, scope)

#Definindo o client
client = gspread.authorize(creds)

#Abrindo a planilha
sheet = client.open(SHEET_TITLE).sheet1

#Função que retorna uma lista das URL dos animes que estão na planilha.
def getAnimeUrl():
  anime_url = sheet.col_values(COL_URL)
  anime_url.pop(0)

  return anime_url

#Função que altera na planilha o número do último episódio lançado.
def setLastEpisode(index, value):
  sheet.update_cell(index + 2, COL_LE, value)

#Função que altera na planilha a URL do último episódio lançado.
def setLastEpisodeUrl(index, value):
  sheet.update_cell(index + 2, COL_LEU, value)