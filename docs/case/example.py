import tkinter as tk
from TkGifWidget import AnimatedGif
root = tk.Tk()
# Create an AnimatedGif widget, play when displayed
gif = AnimatedGif('../gif/example.gif', play_mode='display')
gif.pack()
root.mainloop()

