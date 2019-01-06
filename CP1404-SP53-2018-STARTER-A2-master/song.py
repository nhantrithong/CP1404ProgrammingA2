
class Song:
    def __init__(self, title = '', artist = '', year = 0, status = "*"):
        self.title = title
        self.artist = artist
        self.year = year
        self.status = status

    def mark_learnt(self):
        self.status = "(Learnt)"

    def __str__ (self):
        return("{}, {}, {}, {}").format(str(self.title),str(self.artist),str(self.year),str(self.status))