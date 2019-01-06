"""(Incomplete) Tests for Song class."""
from song import Song

#status-* = Required to learnt (has not learn yet)
#status-"" = No longer required to learn (song learned/completed)

# test empty song (defaults) with error checking through assert statements
song = Song()
print(song)
assert song.artist == ""
assert song.title == ""
assert song.year == 0
assert song.status in ["","*"]

#status-* = Required to learnt (has not learn yet)
#status-"" = No longer required to learn (song learned/completed)


# test initial-value song
song2 = Song("Amazing Grace", "John Newton", 1779, True)
print(song2)
# TODO: write tests to show this initialisation works


# test mark_learned()
# TODO: write tests to show the mark_learned() method works
song2.mark_learnt()
print(song2)