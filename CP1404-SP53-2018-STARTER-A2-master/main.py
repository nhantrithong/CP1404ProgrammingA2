'''
Name: Nhan Tri Thong

Date: 1/5/2019

Brief Project Description: creating a GUI which displays a series of song in a list which can mark them as learnt, count the amount og
                            songs, enabling the addtion of new songs as well as a sorting feature

GitHub URL: https://github.com/nhantrithong/CP1404ProgrammingA2

Personal repository is used as given classroom repositoty in the Assignment 2 instruction doc does not work
'''

#importing all necessary modules
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from kivy.uix.button import Button

#importing all necessary classes
from songlist import SongList
from song import Song

#defining all necessary properties
class SongsToLearnApp(App):
    current_sort = StringProperty()
    sort_options = ListProperty()
    learn_count = StringProperty()
    output_label = StringProperty()
    song_summary = StringProperty()
    song_elements = StringProperty()
    finale = StringProperty()

    #initiating all necesary methods from the song and songlist classes (mainly the songlist class)
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

    #building the necessary methods for the GUI
    def build(self):
        self.title = "Songs to Learn 2.0"
        self.root = Builder.load_file('app.kv')
        self.current_sort = "Title"
        self.create_widgets()
        # self.counter()
        # self.sorting()
        return self.root

    #sorting method used to sort list of songs when one of three options (title, artist, year) is selected (does not function properly)
    def sorting(self):
        if self.root.ids.sort_selection.values == 'Title':
            choice = self.list_song_2
        elif self.root.ids.sort_selection.values == 'Artist':
            choice = self.list_artist_2
        elif self.root.ids.sort_selection.values == 'Year':
            choice = self.list_year_2
        return choice

    #method responsible for the main function of the GUI interface where songs are marked learnt as well as the labels which display appropriate messages
    #the counter functions but encounters problems when interacting with other methods
    def create_widgets(self):
        self.root.ids.create_widgets.clear_widgets()
        self.root.ids.output_label.text = "To Learn: {}, Learnt: {}".format(self.get_num_total - self.get_num_learnt,self.get_num_learnt) #label displaying the counter of songs
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
                button_color = [1, 0, 0, 1] #establishing color of buttons depending on their learnt status where * means not learnt and "" means learnt
            elif Status == "":
                button_color = [0, 0, 1, 1] #establishing color of buttons depending on their learnt status where * means not learnt and "" means learnt
            temp_button = Button(text=song_summary, background_color=button_color)
            temp_button.bind(on_release=self.song_display)
            self.root.ids.create_widgets.add_widget(temp_button)

    #method responsible for marking the songs as learnt, changing the color of the buttons and displaying it
    def song_display(self, temp_button):
        temp_button.background_color = [0, 0, 1, 1] #indicates color change when button is released
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
        final = parts[0] + ',' + parts[1] + ',' + parts[2] + ' ' + marked #displays new text on button after click
        final_2 = parts[0] + ',' + parts[1] + ',' + parts[2] + ' ' + marked #displays new label after click
        temp_button.text = final
        self.songlist.save_songs()
        self.root.ids.output_label_2.text = final_2

    #method adds new songs which displays it in the GUI as well as saving them and appending to the songs.csv file
    def add_new_song(self):
        song_name = str(self.root.ids.input_title.text)
        artist_name = str(self.root.ids.input_artist.text)
        year = str(self.root.ids.input_year.text)
        full_description = song_name +","+ artist_name +","+ year +","+ "*"
        self.list.append(full_description) #appending new song into universal list
        self.songlist.save_songs() #saving new song to songs.csv file
        self.root.ids.input_title.text = ""
        self.root.ids.input_artist.text = ""
        self.root.ids.input_year.text = ""
        self.get_num_total += 1 #counter change when song is added
        self.create_widgets()

    #method used to clear the input fields after input had been inserted and appended
    def clear_app(self):
        self.root.ids.input_title.text = "" #emptying title field
        self.root.ids.input_artist.text = "" #emptying artist field
        self.root.ids.input_year.text = "" #emptying year field





SongsToLearnApp().run()