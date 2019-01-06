from songlist import SongList

# test empty SongList
song_list = SongList()
print(song_list) #if # removed, program wont work because of the __str__ as the list is still empty so theres nothing for the __str__ to work with
assert len(song_list.list) == 0

#test loading songs
song_list = SongList()
song_list.load_songs()
print(song_list)
assert len(song_list.list) > 0  # assuming CSV file is not empty

# test sorting songs
order = song_list.sort()
print("Ordered song list - By Title:",order)

order_2 = song_list.sort_artist()
print("Order song list - by Artist:",order_2)

order_3 = song_list.sort_year()
print("Order song list - By Year:",order_3)

# test getting the number of required and learned songs (separately)
a = song_list.get_num_total()
print(a)
b = song_list.get_num_learnt()
print(b)
c = song_list.get_num_required()
print(c)

# test adding a new Song
song_list.add_song('Starboy', 'The Weeknd', 2016)

# test get_song()
#song_list.get_song("Starboy")

#test mark_learnt()
song_list.mark_learnt()

#test mark_not_learnt()
song_list.mark_not_learnt()

# test saving songs (check CSV file manually to see results)
song_list.save_songs()