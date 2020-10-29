from crawler import Crawler
import sheets
import time

# --- Constants --- #
USER = "Allan"
SHEET_LINK = "https://docs.google.com/spreadsheets/d/1b5aRDVLz2a3zf4x5j0uJOeonr51Kmlu5vaIQ64b0wCY/edit#gid=0"
# ---------------- #

start = time.time()

crawler = Crawler()
animes_url = sheets.getAnimeUrl()
size = len(animes_url)

for i in range(0, size):
  last_episode = crawler.getLastEpisode(animes_url[i])
  last_episode_url = crawler.getLastEpisodeUrl(animes_url[i])

  sheets.setLastEpisode(i, last_episode)
  sheets.setLastEpisodeUrl(i, last_episode_url)

  percentage = 100 * (i + 1)/size

  print("Anime {}/{} atualizado | {:.2f}%".format(i + 1, size, percentage))

end = time.time()

print("\nPlanilha de animes atualizada com sucesso {}! \nLink: {}\n".format(USER, SHEET_LINK))
print("Tempo de execução: {:.2f}s\n".format(end - start))