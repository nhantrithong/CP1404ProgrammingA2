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

    def get_num_total(self):
        total_songs = max(self.count_list)
        return (total_songs)

    def mark_learnt(self):
        for songs in self.list:
            component = songs.split(',')
            status = component[3]
            if status == "*":
                new_status = "Learnt"
                new = component[0] + "," + component[1] + "," + component[2] + "," + new_status
                self.learnt_list.append(new)
        print(self.learnt_list)

    def mark_not_learnt(self):
        for songs in self.list:
            component = songs.split(',')
            status = component[3]
            if status == "":
                new_status = "Not Learnt"
                new = component[0] + "," + component[1] + "," + component[2] + "," + new_status
                self.not_learnt_list.append(new)
        print(self.not_learnt_list)

    def load_songs(self):
        input_file = open("songs.csv", "r")
        file_read = input_file.readlines()
        count_list = []
        learnt_count = 0
        song_number_count = 0
        for lines in self.file:
            song_number_count += 1
            new_lines = lines.split(",")
            song_name = new_lines[0]
            artist_name = new_lines[1]
            year = new_lines[2]
            status = new_lines[3].replace("n", "*").replace("y", "").replace("\n", "")
            final_song_list = ("{},{},{},{}".format(song_name, artist_name, year, status))
            count_list.append(song_number_count)
            if "*" not in status:
                learnt_count += 1
            self.list.append(final_song_list)
            # self.export.append(final_song_list)
            self.learnt_count.append(learnt_count)
            self.count_list.append(max(count_list))
