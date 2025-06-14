from tkinter import *
from TkGifWidget import *
root = Tk()

# 默认不处理背景图
gif1 = AnimatedGif('../gif/example.gif')
gif1.pack()
# 将背景图模糊
gif2 = AnimatedGif('../gif/example.gif', bg_func=BgFunc.blur)
gif2.pack()
# 指定背景图，将背景图变暗
gif3 = AnimatedGif('../gif/example.gif', default_bg='example_bg.png', bg_func=(BgFunc.darken))
gif3.pack()
# 将背景图变暗后添加GIF标志
gif3 = AnimatedGif('../gif/example.gif', bg_func=(BgFunc.darken, BgFunc.gif_sign))
gif3.pack()

root.mainloop()