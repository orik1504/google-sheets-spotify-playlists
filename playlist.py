import tekore as tk
from client_ids import ClientIds

CLIENT_ID = ClientIds.get_client_id()
CLIENT_SECRET = ClientIds.get_client_secret()
REDIRECT_URI = ClientIds.get_redirect_uri()


creds = tk.RefreshingCredentials(CLIENT_ID,CLIENT_SECRET,REDIRECT_URI)
scope = tk.scope.playlist_modify_public
refresh_token = tk.prompt_for_user_token(CLIENT_ID,CLIENT_SECRET,REDIRECT_URI,scope) 
token = refresh_token.access_token
spotify = tk.Spotify(token)

web_url = creds.user_authorisation_url(scope) # not finished web url, need to open and copy the new one




class Song():

    """ Will create a song to return the uri of the searched song """

    def __init__(self,song_name,artist,genere): # need to add genere
        self.song_name = song_name
        self.artist = artist
        self.genere = genere 
    
    def get_uri(self,):
            return (spotify.search(self.__create_query(), types=('track',)))[0].items[0].uri
        
        # don't worry about the problem
    
    
    def __add_plus(self,name):
        #example -> "foo fee" = "foo+fee" 
        return name.replace(" ","+")
    
    def __create_query(self):
        return f"{self.__add_plus(self.song_name)}+{self.__add_plus(self.artist)}"

    




class Playlist():


    def __init__(self, genere):
        self.playlist_id = self.__check_genere(genere)
        
    
    def __check_genere(self,genere):
        
        genere_dict = {
            "pop":"2CHrNUOs5VHaetkJNG36lr",
            "rock":"5JuLHcnusAsiAjlhu5ydhn",
            "chill":"6MU0PhigCoXPKZM5ncPpvJ",
            "hiphop":"1SaOAakLNJuJIQX6pCFwX4",
            "test":"4Ul9OleRqhNKGmhHGfLv1o"}
        
        if genere in genere_dict.keys():
            return genere_dict[genere]
        
        #TODO: add playlists ids to the dict

    def add_to_playlist(self,song_uri_list):
        return(spotify.playlist_add(self.playlist_id ,song_uri_list))
        


