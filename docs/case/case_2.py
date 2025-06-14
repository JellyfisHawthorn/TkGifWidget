from tkinter import *
from TkGifWidget import *
root = Tk()

# 在点击控件后删除控件
gif = AnimatedGif('../gif/example.gif', play_mode=HOVER, hover_func=lambda x: x.destroy())
gif.pack()

root.mainloop()