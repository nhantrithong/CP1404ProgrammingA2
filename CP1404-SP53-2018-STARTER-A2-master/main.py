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
