# TkGifWidget

A widget that displays GIFs in Tkinter.  
一个能在Tkinter中显示GIF动图的控件。

![GitHub License](https://img.shields.io/github/license/JellyfisHawthorn/TkGifWidgit)
![PyPI - Version](https://img.shields.io/pypi/v/TkGifWidget)
![dependce](https://img.shields.io/badge/dependence-Pillow-brightgreen?link=https%3A%2F%2Fgithub.com%2Fpython-pillow%2FPillow
)


## Language

- [English](#english)
- [简体中文](#简体中文)

---

## English

### Overview

This module provides a widget class called AnimatedGif, which can display GIF animations (including some other formats).

The AnimatedGif widget supports setting the number of loops, the image to be displayed when the animation is not playing, and the callback function to be executed when the animation is completed, etc.

In addition, the AnimatedGif widget supports three playback modes, which are:

- click: background image is displayed before the animation starts, and the animation is played when clicked, and the background image is displayed again when clicked again.

![click](https://github.com/JellyfisHawthorn/TkGifWidget/blob/main/docs/gif/en_us/click.gif)

- display: the animation is played when the AnimatedGif widget is mapped, and the animation is stopped when the widget is unmapped.

![display](https://github.com/JellyfisHawthorn/TkGifWidget/blob/main/docs/gif/en_us/display.gif)

- hover: the animation is played when the mouse moves over the AnimatedGif widget, and the animation is stopped when the mouse moves out of the widget.

![hover](https://github.com/JellyfisHawthorn/TkGifWidget/blob/main/docs/gif/en_us/hover.gif)

### Installation and Import

Install using pip:
```
pip install TkGifWidget
```

Import:
```
from TkGifWidget import *
# or import TkGifWidget
```

### Usage
[example.py](https://github.com/JellyfisHawthorn/TkGifWidget/blob/main/docs/case/example.py):
```
import tkinter as tk
from TkGifWidget import AnimatedGif
root = tk.Tk()
# Create an AnimatedGif widget, play when displayed
gif = AnimatedGif('../gif/example.gif', play_mode='display')
gif.pack()
root.mainloop()
```

For more information, please refer to the Wiki:

https://github.com/JellyfisHawthorn/TkGifWidget/wiki/English

### Shortcoming

Because of the way Tk loads images, GIF animations with **irregular** opacity can be slow to load.

---

## 简体中文

### 概述

此模块提供了一个名为AnimatedGif的控件类，用于显示GIF动图（也支持一些其他动图格式）。

动图控件支持设置动图的循环次数、未播放时显示的图片、播放完成后执行的回调函数等等。

此外，动图控件支持三种播放模式，分别是：

- click（点击）：点击前显示背景图，点击后播放动图，再次点击重新显示背景图。

![点击](https://github.com/JellyfisHawthorn/TkGifWidget/blob/main/docs/gif/zh_cn/click.gif)

- display（显示）：动图控件被映射时开始播放动图，取消映射时结束播放动图。

![显示](https://github.com/JellyfisHawthorn/TkGifWidget/blob/main/docs/gif/zh_cn/display.gif)

- hover：当鼠标移动到动图控件上时播放动图，移出动图控件结束播放动图。

![悬停](https://github.com/JellyfisHawthorn/TkGifWidget/blob/main/docs/gif/zh_cn/hover.gif)

### 安装和导入

使用pip安装：
```
pip install TkGifWidget
```

导入方式：
```
from TkGifWidget import *
# 或者使用import TkGifWidget
```

### 使用

[example.py](https://github.com/JellyfisHawthorn/TkGifWidget/blob/main/docs/case/example.py)：
```
import tkinter as tk
from TkGifWidget import AnimatedGif
root = tk.Tk()
# 创建动图控件，显示时播放
gif = AnimatedGif('../gif/example.gif', play_mode='display')
gif.pack()
root.mainloop()
```

具体请查看Wiki：https://github.com/JellyfisHawthorn/TkGifWidget/wiki/%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87

Bilibili上的介绍文章（版本较旧）：https://www.bilibili.com/read/cv31300353/  

### 缺陷

因为Tk的图像加载方式，极少部分透明度**不规则**的GIF动图加载速度会极慢。
