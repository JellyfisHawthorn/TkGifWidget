from tkinter import *
from TkGifWidget import *
root = Tk()

# 点击时触发
gif1 = AnimatedGif('../gif/example.gif', play_mode='click')
gif1.pack()
# 当鼠标悬浮在控件上时触发，同时更换背景图
gif2 = AnimatedGif('../gif/example.gif', play_mode=HOVER, default_bg='example_bg.png')
gif2.pack()
# 显示时自动播放，播放2次后停止，
gif3 = AnimatedGif('../gif/example.gif', play_mode=DISPLAY, loop=1)
gif3.pack()
# 通过修改Frame控件添加边框
gif4 = AnimatedGif('../gif/example.gif', DISPLAY, relief=SOLID, border=5)
gif4.pack()

root.mainloop()