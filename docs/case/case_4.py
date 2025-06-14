# If the GIF will continue to loop after each end of playback, turn the border of the widget red for 300ms, otherwise delete the GIF widget.
from tkinter import *
from TkGifWidget import *
root = Tk()


def func(_gif, is_continue):
    if is_continue:
        _gif.configure(bg='red')
        _gif.after(300, lambda: _gif.configure(bg='green'))
    else:
        _gif.destroy()


# Play the GIF for 5 times, and call the func after each end of playback.
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