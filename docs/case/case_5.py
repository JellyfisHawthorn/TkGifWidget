from tkinter import *
from tkinter.ttk import Combobox
from TkGifWidget import *
from PIL.Image import new

root = Tk()

# 创建白色背景图
bg_img = new('RGB', (400, 100), 'white')
# 创建动图控件并设置播放模式和背景图
# 未指定动图时背景图为空白，指定动图时背景图为动图第一张图片
gif = AnimatedGif(nogif_bg=bg_img)
gif.pack()
# 创建选择动图和选择播放模式的两个组合框
cbox1 = Combobox(values=('', 'blackline.gif', 'redline.gif', 'greenline.gif'), state='readonly')
cbox1.var = StringVar()
cbox1.configure(textvariable=cbox1.var)
cbox1.var.trace_add('write', lambda *args: gif.set_gif(r'../gif/' + cbox1.get()))
cbox1.pack(side=LEFT, expand=True)

cbox2 = Combobox(values=('click', 'display', 'hover'), state='readonly')
cbox2.var = StringVar(value='click')
cbox2.configure(textvariable=cbox2.var)
cbox2.var.trace_add('write', lambda *args: gif.set_play_mode(cbox2.get()))
cbox2.pack(side=LEFT, expand=True)

root.mainloop()