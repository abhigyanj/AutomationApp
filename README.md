# Automation App

## Overview

This is an automation app. It has 4 files, [`functions.py`](functions.py) contain the main functions, [`get_screenshot.py`](get_screenshot.py) is a Tkinter Application that will provide a nice UI to take a screenshot, [`gui_change_handler.py`](gui_change_handler.py) handles the important events and [`gui.py`](gui.py) is the main file which hadles the main Tkinter Application.

## Pictures

Here are some sample pictures:
![Picture 1](pictures/picture1.png)
![Picture 2](pictures/picture2.png)
![Picture 3](pictures/picture3.png)


## Features

It has the following features:
 * Move from point A to B in a curved line using [`PyClick`][1]
 * Wait `x` seconds, with an random offset
 * Write text at a specific speed
 * Recognize if an image is on a screen
 * Compiled to `.exe` using [`pyinstaller`][2], which can be found at [`/exe/gui.exe`](exe/gui.exe)

## Functions

The function for writing text, moving the mouse, wait `x` seconds with an offset and recognize if an image is on a screen can be found in at [`functions.py`](functions.py).


  [1]: https://pypi.org/project/pyclick/
  [2]: https://pypi.org/project/pyinstaller/
