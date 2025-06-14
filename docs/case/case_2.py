from tkinter import *
from TkGifWidget import *
root = Tk()

# Delete the widget after clicking on it
gif = AnimatedGif('../gif/example.gif', play_mode=HOVER, hover_func=lambda x: x.destroy())
gif.pack()

root.mainloop()