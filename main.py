from crawler import Crawler
import sheets

# --- Constants --- #
USER = "Allan"
SHEET_LINK = "https://docs.google.com/spreadsheets/d/1b5aRDVLz2a3zf4x5j0uJOeonr51Kmlu5vaIQ64b0wCY/edit#gid=0"
# ---------------- #

crawler = Crawler()
animes_url = sheets.getAnimeUrl()

for i in range(0, len(animes_url)):
  last_episode = crawler.getLastEpisode(animes_url[i])
  last_episode_url = crawler.getLastEpisodeUrl(animes_url[i])

  sheets.setLastEpisode(i, last_episode)
  sheets.setLastEpisodeUrl(i, last_episode_url)

print("\nPlanilha de animes atualizada com sucesso {}! \nLink: {}\n".format(USER, SHEET_LINK))