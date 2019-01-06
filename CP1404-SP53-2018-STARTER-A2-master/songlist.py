input_file = open("songs.csv", "r")
FILES = input_file.readlines()

class SongList:
    def __init__(self, list = []):
        self.list = list
        self.file = FILES

        self.count_list = []
        self.learnt_count = []

        self.remainder = [1]

        self.sort_list = []
        self.sort_list_2 = []

        self.sort_artist_list = []
        self.sort_artist_list_2 = []

        self.sort_year_list = []
        self.sort_year_list_2 = []

        self.learnt_list = []
        self.not_learnt_list = []

    def get_song(self, title):
        for lines in self.list:
            if title in lines:
                return (lines)