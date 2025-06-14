from tkinter import *
from TkGifWidget import *
root = Tk()

# Background images are not processed by default
gif1 = AnimatedGif('../gif/example.gif')
gif1.pack()
# Blur the background image
gif2 = AnimatedGif('../gif/example.gif', bg_func=BgFunc.blur)
gif2.pack()
# Specify the background image and darken it.
gif3 = AnimatedGif('../gif/example.gif', default_bg='example_bg.png', bg_func=(BgFunc.darken))
gif3.pack()
# Add a GIF logo after darkening the background image
gif3 = AnimatedGif('../gif/example.gif', bg_func=(BgFunc.darken, BgFunc.gif_sign))
gif3.pack()

root.mainloop()