# maker a class named Song tha is-a object
class Song(object):
    # class Song has-a __init__that takes self and lyrics parameters
    def __init__(self, lyrics):
        # from self get the attribute lyrics and set it to lyrics
        self.lyrics = lyrics
    # class Song has-a function named sing_me_a_song that takes self parameters

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line


# set happy_bday to an instance of class Song and call it with parameters
# self and "whatever is inside quotes"
happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "so I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

# from happy_bday get the function sing_me_a_song
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
