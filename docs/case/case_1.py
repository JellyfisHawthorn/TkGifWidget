from tkinter import *
from TkGifWidget import *
root = Tk()

# Trigger when clicked
gif1 = AnimatedGif('../gif/example.gif', play_mode='click')
gif1.pack()
# Trigger when hovered, and change background
gif2 = AnimatedGif('../gif/example.gif', play_mode=HOVER, default_bg='example_bg.png')
gif2.pack()
# Play automatically, stop after 2 loops
gif3 = AnimatedGif('../gif/example.gif', play_mode=DISPLAY, loop=1)
gif3.pack()
# Add a border by modifying the Frame widget
gif4 = AnimatedGif('../gif/example.gif', DISPLAY, relief=SOLID, border=5)
gif4.pack()

root.mainloop()