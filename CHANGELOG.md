### 2024/7/14更新：

1. AnimatedGif类新增play_end_func形参，以便在动图播放结束时回调处理。感谢B站[@只是一个球_](https://space.bilibili.com/1858500718)提出的建议
2. 以下改动（未全部列出）使控件可以修改动图，也可以在指定动图前先创建控件：

    * `AnimatedGif`类`file_path`, `play_mode`形参变为默认值形参。
    * 设置动图的部分移至`set_gif()`方法。
    * `bg_img`属性只读，且值类型变为`Image`对象而非`PhotoImage`。
    * 使用`bg_imgtk`只读属性获取`PhotoImage`对象。
    * 新增`set_bg_img()`方法用于设置当前背景图。（若想指定默认背景图请修改`default_bg`属性）
    * 处理背景图部分移至`apply_bg_func()`方法。
    * 新增`set_play_mode()`方法用于设置播放模式。
    * `AnimatedGif`类`bg_path`属性名称修改为`default_bg`（即使这样不符合向下兼容）。 `default_bg`用于指定默认的背景图，值可以是路径或`Image`对象。

3. 修复调用`end_play()`后，在小于`duration`时间内再调用`start_play()`会使播放速度加倍的BUG。
4. 修改内部图像容器的`borderwidth`为0以确保无边框。
5. `AnimatedGif`类新增`nogif_bg`形参，用于指定没有动图时的背景图。

### 2024/7/28更新：

* 修复动图在播放时透明颜色不能正确显示的BUG。感谢B站[@只是一个球_](https://space.bilibili.com/1858500718)
* 添加帧持续时间缺失时的处理。

### 2025/2/21更新：

* 为模块中的文档字符串添加英文翻译。
* 将该模块添加到PyPI和Github上。

### 2025/6/13更新：

* 更改项目名称为TkGifWidget。（才发现Widget打成Widgit了...）
* 按照[这里说的](https://github.com/Bluecloud-Seao/WarmaDesk--/pull/1)规范化项目。
* 优化README。
* 更新教程。

### 2025/8/15更新：

* 新增pyi存根文件。