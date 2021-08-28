import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json",scope)

client = gspread.authorize(creds)

sheet = client.open("playlist maker").sheet1

data = sheet.get_all_records()

class Sheets():
    
    def get_artists_list(self):
        return sheet.col_values(4)[1::]
    
    def get_songs_list(self):
        return sheet.col_values(2)[1::]
    
    def get_genere_list(self):
        return sheet.col_values(3)[1::]
    
    def get_row_numbers(self):
        return sheet.row_count
    
    def clear(self):
        sheet.clear()

    def del_row(self,row):
        sheet.delete_row(row)
    