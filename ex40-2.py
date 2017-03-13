class Song():

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

#  Here we set a variable to a list of words
somesong = ["uno", "dos", "tres", "and so on"]

# Here we set newsong to an instance of the class named Song and call it with
# parameter saelf and somesong being defined prevoiously
newsong = Song(somesong)

# from newsong we can now get the function sing_me_a_song and just call it
# with self parameter
newsong.sing_me_a_song()
