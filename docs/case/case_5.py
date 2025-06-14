from tkinter import *
from tkinter.ttk import Combobox
from TkGifWidget import *
from PIL.Image import new

root = Tk()

# Creating a white background image
bg_img = new('RGB', (400, 100), 'white')
# Create a GIF widget and set the play mode and background image.
# When GIF is not specified, the background image is blank, when GIF is specified, 
# the background image is the first picture of GIF.
gif = AnimatedGif(nogif_bg=bg_img)
gif.pack()
# Create two combo boxes for selecting GIFs and selecting playback modes
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