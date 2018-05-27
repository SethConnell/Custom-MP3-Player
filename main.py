from gifplayer import *
import sys

from pygame import mixer # Load the required library

mixer.init()
mixer.music.load(sys.argv[1])
mixer.music.play(-1)
play = "no"
def close_window():
        mixer.music.stop()
        quit()
def callback(event):
    global play
    if play == "yes":
	play = "no"
	mixer.music.pause()
    else:
	play = "yes"
	mixer.music.unpause()

if __name__ == "__main__":
    from Tkinter import Tk, Label
    root = Tk()
    root.protocol("WM_DELETE_WINDOW", close_window)
    root.title('My MP3 Player --- ' + sys.argv[1])
    root.resizable(False, False)
    # Add the path to a GIF to make the example working
    l = AnimatedGIF(root, "/root/Documents/Code Projects/MP3 Player/gif.gif")
    l.bind("<Button-1>", callback)
    l.pack()

    root.mainloop()
