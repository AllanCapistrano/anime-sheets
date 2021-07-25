import time
import sheets

from services.crawlerAnimesHouse import CrawlerAnimesHouse
from services.crawlerGoyabu import CrawlerGoyabu

# ------------------------------ Constants ----------------------------------- #
USER = "your_name"
SHEET_LINK = "your_sheet_link"
COLOR_OK = [0, 1, 0]
COLOR_NOT_OK = [1, 0, 0]
# ---------------------------------------------------------------------------- #

start              = time.time()

crawlerAnimesHouse = CrawlerAnimesHouse()
crawlerGoyabu      = CrawlerGoyabu()

animesUrls         = sheets.getAnimeUrl()
im                 = sheets.getIm()
size               = len(animesUrls)

lastEpisodeSheet = sheets.getLastEpisode()

for i in range(0, size):
    # Verifica qual é o site que está sendo utilizado para assisitir o anime.
    if(animesUrls[i].find("animeshouse") != -1):
        lastEpisode = crawlerAnimesHouse.getLastEpisode(animesUrls[i])
        lastEpisodeUrl = crawlerAnimesHouse.getLastEpisodeUrl(animesUrls[i])
    elif(animesUrls[i].find("goyabu") != -1):
        lastEpisode = crawlerGoyabu.getLastEpisode(animesUrls[i])
        lastEpisodeUrl = crawlerGoyabu.getLastEpisodeUrl(animesUrls[i])

    try:
        # Evitar escritas desnecessárias.
        if(lastEpisodeSheet[i] != lastEpisode):
            sheets.setLastEpisode(i, lastEpisode)
            sheets.setLastEpisodeUrl(i, lastEpisodeUrl)
    except :
        if(im[i]):
            sheets.setLastEpisode(i, lastEpisode)
            sheets.setLastEpisodeUrl(i, lastEpisodeUrl)
    
    # Muda a cor da célula, de acordo com o último episódio assisitido.
    if(int(im[i]) < int(lastEpisode)):
        sheets.changeCellBackgroundColor(i + 2, COLOR_NOT_OK)
    else:
        sheets.changeCellBackgroundColor(i + 2, COLOR_OK)

    percentage = 100 * (i + 1)/size

    print("Anime {}/{} atualizado | {:.2f}%".format(i + 1, size, percentage))

end = time.time()

print("\nPlanilha de animes atualizada com sucesso {}! \nLink: {}\n".format(
    USER, SHEET_LINK))
print("Tempo de execução: {:.2f}s\n".format(end - start))
