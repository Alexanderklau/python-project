# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
class Song(object):
    def __init__(self,lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
happy_bday = Song(["Happy birthday!",
                   '吼啊！',
                   '当然啦！',
                   '董先生'])
Bulles = Song(["the are how!@"])

happy_bday.sing_me_a_song()
Bulles.sing_me_a_song()











# if __name__ == '__main__':