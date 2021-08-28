from google_sheets import Sheets
from playlist import Song
from playlist import Playlist


sheet = Sheets()
artist_list = sheet.get_artists_list()
songs_list = sheet.get_songs_list()
genere_list = sheet.get_genere_list()

for index in range(sheet.get_row_numbers()-1):
    try:
        song = Song(songs_list[index],artist_list[index],genere_list[index])
        playlist = Playlist(song.genere)
        playlist.add_to_playlist([song.get_uri()])
        sheet.del_row(index)
    except :
        continue
sheet.clear()

#print(f" the url is:{aa.get_web_url()} ")

    
