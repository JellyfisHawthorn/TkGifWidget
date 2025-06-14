# 动图每次结束播放后若还会继续循环播放，则将控件边框变红300ms，否则删除动图控件
from tkinter import *
from TkGifWidget import *
root = Tk()


def func(_gif, is_continue):
    if is_continue:
        _gif.configure(bg='red')
        _gif.after(300, lambda: _gif.configure(bg='green'))
    else:
        _gif.destroy()


# 总共播放五次，每次播放完成后回调func
gif = AnimatedGif(
    '../gif/Line_LtoR.gif',
    play_mode=CLICK,
    play_end_func=func,
    loop=4,
    bd=3,
    bg='green'
)
gif.pack()

root.mainloop()