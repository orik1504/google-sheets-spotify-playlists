from google_sheets import Sheets
sheet = Sheets()

class SongSort():

    def __init__(self,artist_list,songs_name_list,genere_list):
        self.artist_list = artist_list
        self.genere_list = genere_list
        self.songs_name_list = songs_name_list
        self.sorted_chill_artist_list = []
        self.sorted_rap_artist_list = []
        self.sorted_rock_artist_list = []
        self.sorted_pop_artist_list = []

    def sort_by_genere(self,):
        for index in sheet.get_row_numbers():
