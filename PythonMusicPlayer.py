from tkinter import *
from tkinter import filedialog
from pygame import mixer
import pygame

class MusicPlayer:
    def __init__(self, window ):
        window.geometry('384x384'); window.title('Music Player'); window.resizable(0,0); window.configure(bg='black')
        Load = Button(window, text = 'Load',  width = 10, font = ('Arial Black', 10), command = self.load, bg = 'deepskyblue', borderwidth="4")
        Play = Button(window, text = 'Play',  width = 10,font = ('Arial Black', 10), command = self.play, bg = 'deepskyblue', borderwidth="4")
        Pause = Button(window,text = 'Pause',  width = 10, font = ('Arial Black', 10), command = self.pause, bg = 'deepskyblue', borderwidth="4")
        Stop = Button(window ,text = 'Stop',  width = 10, font = ('Arial Black', 10), command = self.stop, bg = 'deepskyblue', borderwidth="4")
        Load.place(x=26,y=178);Play.place(x=144,y=178);Pause.place(x=262,y=178);Stop.place(x=144,y=225) 


        self.music_file = False
        self.playing_state = False
    def load(self):
        self.music_file = filedialog.askopenfilename()
    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()
    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state=True
        else:
            mixer.music.unpause()
            self.playing_state = False
    def stop(self):
        mixer.music.stop()
root = Tk()


# background image
photo = PhotoImage(file = r"C:\Users\Brice\Desktop\musicpic.png") 

Button(root, image = photo).pack(side = TOP) 

app= MusicPlayer(root)
root.mainloop()