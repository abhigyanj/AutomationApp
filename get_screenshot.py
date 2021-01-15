from tkinter import *
import pyautogui

import datetime


class Application():
    def __init__(self, master, name):
        self.master = master
        self.rect = None
        self.x = self.y = 0
        self.start_x = None
        self.start_y = None
        self.curX = None
        self.curY = None
        self._name = name

        # root.configure(background = 'red')
        # root.attributes("-transparentcolor","red")

        self.master.attributes("-transparent", "blue")
        self.master.geometry('400x50+200+200')  # set new geometry
        self.master.title('Take Screenshot')
        self.menu_frame = Frame(master, bg="blue")
        self.menu_frame.pack(fill=BOTH, expand=YES)

        self.buttonBar = Frame(self.menu_frame, bg="")
        self.buttonBar.pack(fill=BOTH, expand=YES)

        self.master_screen = Toplevel(self.master)
        self.master_screen.withdraw()
        self.master_screen.attributes("-transparent", "blue")
        self.picture_frame = Frame(self.master_screen, background="blue")
        self.picture_frame.pack(fill=BOTH, expand=YES)

        self.createScreenCanvas()

    def takeBoundedScreenShot(self, x1, y1, x2, y2):
        im = pyautogui.screenshot(region=(x1, y1, x2, y2))
        im.save("snips/" + self._name + ".png")

    def createScreenCanvas(self):
        self.master_screen.deiconify()
        self.master.withdraw()

        self.screenCanvas = Canvas(
            self.picture_frame, cursor="cross", bg="grey11")
        self.screenCanvas.pack(fill=BOTH, expand=YES)

        self.screenCanvas.bind("<ButtonPress-1>", self.on_button_press)
        self.screenCanvas.bind("<B1-Motion>", self.on_move_press)
        self.screenCanvas.bind("<ButtonRelease-1>", self.on_button_release)

        self.master_screen.attributes('-fullscreen', True)
        self.master_screen.attributes('-alpha', .3)
        self.master_screen.lift()
        self.master_screen.attributes("-topmost", True)

    def on_button_release(self, event):
        try:
            if self.start_x <= self.curX and self.start_y <= self.curY:
                self.takeBoundedScreenShot(
                    self.start_x, self.start_y, self.curX - self.start_x, self.curY - self.start_y)

            elif self.start_x >= self.curX and self.start_y <= self.curY:
                self.takeBoundedScreenShot(
                    self.curX, self.start_y, self.start_x - self.curX, self.curY - self.start_y)

            elif self.start_x <= self.curX and self.start_y >= self.curY:
                self.takeBoundedScreenShot(
                    self.start_x, self.curY, self.curX - self.start_x, self.start_y - self.curY)

            elif self.start_x >= self.curX and self.start_y >= self.curY:
                self.takeBoundedScreenShot(
                    self.curX, self.curY, self.start_x - self.curX, self.start_y - self.curY)
        except TypeError as e:
            print(e)
        else:
            self.exitScreenshotMode()
            self.exit_application()

    def exitScreenshotMode(self):
        self.screenCanvas.destroy()
        self.master_screen.withdraw()
        self.master.deiconify()

    def exit_application(self):
        self.master.destroy()
        self.master.quit()

    def on_button_press(self, event):
        # save mouse drag start position
        self.start_x = self.screenCanvas.canvasx(event.x)
        self.start_y = self.screenCanvas.canvasy(event.y)

        self.rect = self.screenCanvas.create_rectangle(
            self.x, self.y, 1, 1, fill="blue")

    def on_move_press(self, event):
        self.curX, self.curY = (event.x, event.y)
        # expand rectangle as you drag the mouse
        self.screenCanvas.coords(
            self.rect, self.start_x, self.start_y, self.curX, self.curY)


if __name__ == '__main__':
    root = Tk()
    app = Application(root)
    root.mainloop()
