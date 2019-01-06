from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from kivy.uix.button import Button


from songlist import SongList
from song import Song

class SongsToLearnApp(App):
    current_sort = StringProperty()
    sort_options = ListProperty()
    learn_count = StringProperty()
    output_label = StringProperty()
    song_summary = StringProperty()
    song_elements = StringProperty()
    finale = StringProperty()

    def __init__(self, **kwargs):
        super(SongsToLearnApp, self).__init__(**kwargs)
        self.song = Song()
        self.songlist = SongList()
        self.songlist.load_songs()
        self.song_files = self.songlist.file

        self.list = self.songlist.list

        self.get_song = self.songlist.get_song

        self.get_num_learnt = self.songlist.get_num_learnt()
        self.get_num_required = self.songlist.get_num_required()
        self.get_num_total = self.songlist.get_num_total()

        self.count_list = self.songlist.count_list
        self.learnt_count = self.songlist.learnt_count

        self.songlist.sort()
        self.songlist.sort_artist()
        self.songlist.sort_year()

        self.songlist.sort_list
        self.list_song_2 = self.songlist.sort_list_2

        self.songlist.sort_artist_list
        self.list_artist_2 = self.songlist.sort_artist_list_2

        self.songlist.sort_year_list
        self.list_year_2 = self.songlist.sort_year_list_2

        self.songlist.save_songs()

    def build(self):
        self.title = "Songs to Learn 2.0"
        self.root = Builder.load_file('app.kv')
        self.current_sort = "Title"
        self.create_widgets()
        # self.counter()
        # self.sorting()
        return self.root

    def sorting(self):
        if self.root.ids.sort_selection.values == 'Title':
            choice = self.list_song_2
        elif self.root.ids.sort_selection.values == 'Artist':
            choice = self.list_artist_2
        elif self.root.ids.sort_selection.values == 'Year':
            choice = self.list_year_2
        return choice

    def create_widgets(self):
        self.root.ids.create_widgets.clear_widgets()
        self.root.ids.output_label.text = "To Learn: {}, Learnt: {}".format(self.get_num_total - self.get_num_learnt,
                                                                            self.get_num_learnt)
        temp_button = Button
        result = self.list
        for songs in result:
            song_here = Song()
            comps = songs.split(",")
            Title = comps[0]
            Artist = comps[1]
            Year = comps[2]
            Status = comps[3]
            # song_summary = self.song_display(Title, Artist, Year, Status)
            song_summary = "{},{},{} {}".format(Title, Artist, Year, Status)
            if Status == "*":
                button_color = [1, 0, 0, 1]
            elif Status == "":
                button_color = [0, 0, 1, 1]
            temp_button = Button(text=song_summary, background_color=button_color)
            temp_button.bind(on_release=self.song_display)
            self.root.ids.create_widgets.add_widget(temp_button)

    def song_display(self, temp_button):
        temp_button.background_color = [0, 0, 1, 1]
        self.get_song = self.songlist.get_song
        button_message = temp_button.text
        new_message = button_message.split(",")
        get_title = new_message[0]
        full_song = self.get_song(get_title)
        parts = full_song.split(",")
        if parts[3] == "*":
            marked = "(Learnt)"
        elif parts[3] == "":
            marked = "(Already Learnt)"
        final = parts[0] + ',' + parts[1] + ',' + parts[2] + ' ' + marked
        final_2 = parts[0] + ',' + parts[1] + ',' + parts[2] + ' ' + marked
        temp_button.text = final
        self.songlist.save_songs()
        self.root.ids.output_label_2.text = final_2
