from crawler import Crawler
import sheets
import time

# --- Constants --- #
USER = "Allan"
SHEET_LINK = "https://docs.google.com/spreadsheets/d/1b5aRDVLz2a3zf4x5j0uJOeonr51Kmlu5vaIQ64b0wCY/edit#gid=0"
COLOR_OK = [0, 1, 0]
COLOR_NOT_OK = [1, 0, 0]
# ---------------- #

start = time.time()

crawler = Crawler()
animes_url = sheets.getAnimeUrl()
im = sheets.getIm()
size = len(animes_url)
last_episode_sheet = sheets.getLastEpisode()

for i in range(0, size):
    last_episode = crawler.getLastEpisode(animes_url[i])
    last_episode_url = crawler.getLastEpisodeUrl(animes_url[i])

    try:
        if(last_episode_sheet[i] != last_episode):
            sheets.setLastEpisode(i, last_episode)
            sheets.setLastEpisodeUrl(i, last_episode_url)
    except :
        if(im[i]):
            sheets.setLastEpisode(i, last_episode)
            sheets.setLastEpisodeUrl(i, last_episode_url)
    
    
    if(int(im[i]) < int(last_episode)):
        sheets.changeCellBackgroundColor(i + 2, COLOR_NOT_OK)
    else:
        sheets.changeCellBackgroundColor(i + 2, COLOR_OK)

    percentage = 100 * (i + 1)/size

    print("Anime {}/{} atualizado | {:.2f}%".format(i + 1, size, percentage))

end = time.time()

print("\nPlanilha de animes atualizada com sucesso {}! \nLink: {}\n".format(
    USER, SHEET_LINK))
print("Tempo de execução: {:.2f}s\n".format(end - start))
