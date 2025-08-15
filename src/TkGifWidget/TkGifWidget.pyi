import tkinter as tk
from PIL import Image, ImageTk, GifImagePlugin
from _typeshed import StrOrBytesPath
from typing import Literal, Callable, Iterator, Sequence

__all__ = ['AnimatedGif', 'CLICK', 'DISPLAY', 'HOVER', 'BgFunc']

CLICK = 'click'
DISPLAY = 'display'
HOVER = 'hover'


class AnimatedGif(tk.Frame):
    _cbid: str | None
    play_state: str
    loop: int | None
    remain_loop: int
    image_lst: list[ImageTk.PhotoImage]
    duration_lst: list[int]
    image_iter: Iterator[ImageTk.PhotoImage]
    duration_iter: Iterator[int]
    play_end_func: Callable[[AnimatedGif, bool], None]
    hover_func: Callable[[AnimatedGif], None]
    bg_func: Callable[[Image.Image], Image.Image] | Sequence[Callable[[Image.Image], Image.Image]]
    default_bg: StrOrBytesPath
    nogif_bg: StrOrBytesPath | Image.Image
    img_container: tk.Label

    def __init__(
            self,
            file_path: StrOrBytesPath = None,
            play_mode: Literal['click', 'display', 'hover'] | str = ...,
            default_bg: StrOrBytesPath = None,
            bg_func: Callable[[Image.Image], Image.Image] | Sequence[Callable[[Image.Image], Image.Image]] = None,
            nogif_bg: StrOrBytesPath | Image.Image = None,
            hover_func: Callable[[AnimatedGif], None] = None,
            play_end_func: Callable[[AnimatedGif, bool], None] = None,
            loop: int | None = -1,
            master: tk.Misc = None,
            **kwargs
    ) -> None:
        ...

    def set_play_mode(self, play_mode: Literal['click', 'display', 'hover'] | str) -> None: ...

    def set_gif(self, file_path: StrOrBytesPath) -> None: ...

    @property
    def bg_img(self) -> GifImagePlugin.GifImageFile: ...

    @bg_img.setter
    def bg_img(self, _) -> None: ...

    @property
    def bg_imgtk(self) -> ImageTk.PhotoImage: ...

    @property
    def play_mode(self) -> Literal['click', 'display', 'hover'] | str: ...

    @play_mode.setter
    def play_mode(self, _) -> None: ...

    @property
    def __first_img(self) -> Image.Image | None: ...

    @__first_img.setter
    def __first_img(self, _) -> None: ...

    @property
    def __bg_img(self) -> Image.Image | None: ...

    @__bg_img.setter
    def __bg_img(self, _) -> None: ...

    @property
    def __bg_imgtk(self) -> ImageTk.PhotoImage | str: ...

    @__bg_imgtk.setter
    def __bg_imgtk(self, _) -> None: ...

    @property
    def __play_mode(self) -> Literal['click', 'display', 'hover'] | str: ...

    @__play_mode.setter
    def __play_mode(self, _) -> None: ...

    def set_bg_img(self, value) -> None: ...

    def apply_bg_func(self, bg_func=None) -> None: ...

    def _update_bg_img(self) -> None: ...

    def _click_to_switch(self) -> None: ...

    def start_play(self) -> None: ...

    def end_play(self) -> None: ...

    def _update_iter(self) -> None: ...

    def _next_frame(self) -> None: ...


class BgFunc:
    @staticmethod
    def darken(img: Image.Image) -> Image.Image: ...

    @staticmethod
    def gif_sign(img: Image.Image) -> Image.Image: ...

    @staticmethod
    def blur(img: Image.Image) -> Image.Image: ...
