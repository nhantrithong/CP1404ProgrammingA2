"""(Incomplete) Tests for Song class."""
from song import Song

#status-True = Required to learnt (has not learn yet)
#status-False = No longer required to learn (song learned/completed)

# test empty song (defaults)
song = Song()
print(song)
assert song.artist == ""
assert song.title == ""
assert song.year == 0
#assert song.is_required
assert song.status in ["","*"]

# test initial-value song
song2 = Song("Amazing Grace", "John Newton", 1779, True)
print(song2)
# TODO: write tests to show this initialisation works


# test mark_learned()
# TODO: write tests to show the mark_learned() method works
song2.mark_learnt()
print(song2)