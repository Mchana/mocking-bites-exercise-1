class Track:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def matches(self, keyword):
        if self.title == keyword or self.artist == keyword:
            return True
        
        else:
            return False