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

    def add_song(self, song_name_add, artist_name_add, year_add):
        new_status = "*\n"
        if self.remainder[-1] == 0:
            self.remainder.remove(self.remainder[-1])
        song_to_add = ("{},{},{},{}".format(song_name_add, artist_name_add, year_add, new_status))
        self.file.append(song_to_add)
        self.list.append(song_to_add)
        # self.export.append(song_to_add)

    def get_num_required(self):
        songs_left = max(self.count_list) - max(self.learnt_count)
        self.remainder.append(songs_left)
        return (songs_left)

    def get_num_learnt(self):
        songs_learnt = max(self.learnt_count)
        return (songs_learnt)