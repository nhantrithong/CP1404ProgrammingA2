
#song class
class Song:
    def __init__(self, title = '', artist = '', year = 0, status = "*"):
        self.title = title
        self.artist = artist
        self.year = year
        self.status = status

    #method which marks songs as learnt (not used too much)
    def mark_learnt(self):
        self.status = "(Learnt)"

    #returns string after class receives input (not used too much)
    def __str__ (self):
        return("{}, {}, {}, {}").format(str(self.title),str(self.artist),str(self.year),str(self.status))