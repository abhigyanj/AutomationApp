import time
import secrets

from get_screenshot import Application
from functions import checkImageOnScreen

from tkinter import Tk, Toplevel, Button, Label, Entry, END, PhotoImage, StringVar, Canvas, SE, Entry, OptionMenu


class MouseNewWindow:
    def __init__(self, root, if_open=True):
        if if_open:
            self.window = Toplevel(root)
        else:
            self.window = Toplevel

        self.type = 1
        self.start_x = 0
        self.start_y = 0
        self.end_x = 0
        self.end_y = 0
        self.offset = 0
        self.seconds = 0
        self.option = StringVar()

        self.option.set("No Click")

    def load(self, content):
        items = content.split("-")

        self.type = int(float(items[0]))
        self.start_x = int(float(items[1]))
        self.start_y = int(float(items[2]))
        self.end_x = int(float(items[3]))
        self.end_y = int(float(items[4]))
        self.option.set(items[5])
        self.offset = int(float(items[6]))
        self.seconds = int(float(items[7]))

        self.window.withdraw()

    def save(self, file):
        with open(file, "a") as f:
            f.write(
                f"Do {self.type}-{self.start_x}-{self.start_y}-{self.end_x}-{self.end_y}-{self.option.get()}-{self.offset}-{self.seconds}\n")

    def change(self):
        try:
            self.start_x = int(self.inputstartx.get())
            self.start_y = int(self.inputstarty.get())
            self.end_x = int(self.inputendx.get())
            self.end_y = int(self.inputendy.get())
            self.offset = int(self.inputoffset.get())
            self.seconds = int(self.inputseconds.get())
        except ValueError:
            self.inputstartx.delete(0, END)
            self.inputstarty.delete(0, END)
            self.inputendx.delete(0, END)
            self.inputendy.delete(0, END)
            self.inputoffset.delete(0, END)
            self.inputseconds.delete(0, END)
        else:
            self.window.withdraw()

    def addItems(self):
        self.text1 = Label(self.window, text="Cordinates:")
        self.text1.grid(row=0, column=0, padx=(10, 10), pady=(10, 0))

        self.text2 = Label(self.window, text="Start X:")
        self.text2.grid(row=0, column=1, padx=(0, 10), pady=(10, 0))

        self.inputstartx = Entry(self.window, width=10)
        self.inputstartx.insert(0, str(self.start_x))
        self.inputstartx.grid(row=0, column=2, padx=(0, 10), pady=(10, 0))

        self.text3 = Label(self.window, text="Start Y:")
        self.text3.grid(row=0, column=3, padx=(0, 10), pady=(10, 0))

        self.inputstarty = Entry(self.window, width=10)
        self.inputstarty.insert(0, str(self.start_y))
        self.inputstarty.grid(row=0, column=4, padx=(0, 10), pady=(10, 0))

        self.text4 = Label(self.window, text="End X:")
        self.text4.grid(row=1, column=1, padx=(0, 10), pady=(10, 0))

        self.inputendx = Entry(self.window, width=10)
        self.inputendx.insert(0, str(self.end_x))
        self.inputendx.grid(row=1, column=2, padx=(0, 10), pady=(10, 0))

        self.text5 = Label(self.window, text="End Y:")
        self.text5.grid(row=1, column=3, padx=(0, 10), pady=(10, 0))

        self.inputendy = Entry(self.window, width=10)
        self.inputendy.insert(0, str(self.end_y))
        self.inputendy.grid(row=1, column=4, padx=(0, 10), pady=(10, 0))

        self.text6 = Label(self.window, text="Randonmize by:")
        self.text6.grid(row=2, column=0, padx=(10, 10), pady=(10, 0))

        self.inputoffset = Entry(self.window, width=10)
        self.inputoffset.insert(0, str(self.offset))
        self.inputoffset.grid(row=2, column=1, padx=(0, 10), pady=(10, 10))

        self.text7 = Label(self.window, text="Seconds:")
        self.text7.grid(row=3, column=0, padx=(10, 10), pady=(10, 0))

        self.inputseconds = Entry(self.window, width=10)
        self.inputseconds.insert(0, str(self.seconds))
        self.inputseconds.grid(row=3, column=1, padx=(0, 10), pady=(10, 10))

        self.update = OptionMenu(
            self.window, self.option, "No Click", "Left Click", "Right Click", "Double Click")
        self.update.grid(row=2, column=2, sticky='news',
                         padx=30, pady=(30, 10))

        self.update = Button(
            self.window, text="Update All", command=self.change)
        self.update.grid(row=2, column=3, columnspan=2,
                         sticky='news', padx=30, pady=(30, 10))

        self.text8 = Label(self.window, text="Enter Only Numbers")
        self.text8.configure(foreground="red")
        self.text8.grid(row=3, column=2, columnspan=3, sticky='news', padx=30)


class RandomDelayWindow:
    def __init__(self, root, if_open=True):
        if if_open:
            self.window = Toplevel(root)
        else:
            self.window = Toplevel
        self.type = 2
        self.random_wait = 0
        self.random_offset = 0

    def load(self, content):
        items = content.split("-")

        self.type = int(float(items[0]))
        self.random_wait = int(float(items[1]))
        self.random_offset = int(float(items[2]))

        self.window.withdraw()

    def save(self, file):
        with open(file, "a") as f:
            f.write(
                f"Do {self.type}-{self.random_wait}-{self.random_offset}\n")

    def change(self):
        try:
            self.random_wait = int(self.inputwait.get())
            self.random_offset = int(self.inputoffset.get())
        except ValueError:
            self.inputwait.delete(0, END)
            self.inputoffset.delete(0, END)
        else:
            self.window.withdraw()

    def addItems(self):
        self.text1 = Label(self.window, text="Random Wait:")
        self.text1.grid(row=0, column=0, padx=(10, 10), pady=(10, 0))

        self.inputwait = Entry(self.window, width=10)
        self.inputwait.insert(0, str(self.random_wait))
        self.inputwait.grid(row=0, column=1, padx=(0, 10), pady=(10, 0))

        self.text2 = Label(self.window, text="Random Offset:")
        self.text2.grid(row=1, column=0, padx=(0, 10), pady=(10, 0))

        self.inputoffset = Entry(self.window, width=10)
        self.inputoffset.insert(0, str(self.random_offset))
        self.inputoffset.grid(row=1, column=1, padx=(0, 10), pady=(10, 0))

        self.update = Button(
            self.window, text="Update All", command=self.change)
        self.update.grid(row=0, column=2, columnspan=2,
                         sticky='news', padx=30, pady=10)

        self.text3 = Label(
            self.window, text="Enter Only Numbers (These are in Milliseconds)")
        self.text3.configure(foreground="red")
        self.text3.grid(row=1, column=2, columnspan=2, sticky='news', padx=30)


class TextWindow:
    def __init__(self, root, if_open=True):
        if if_open:
            self.window = Toplevel(root)
        else:
            self.window = Toplevel
        self.root = root
        self.text = "Enter text here"
        self.type = 3
        self.seconds = 2

    def load(self, content):
        items = content.split("-")

        self.type = int(float(items[0]))
        self.text = items[1]
        self.seconds = int(float(items[2]))

        self.window.withdraw()

    def save(self, file):
        with open(file, "a") as f:
            f.write(f"Do {self.type}-{self.text}-{self.seconds}\n")

    def change(self):
        try:
            self.text = str(self.input1.get())
            self.seconds = float(self.input2.get())

            if not (self.seconds > 0):
                raise ValueError

        except ValueError:
            self.input.delete(0, END)
            self.input2.delete(0, END)
        else:
            self.window.withdraw()

    def addItems(self):
        self.text1 = Label(self.window, text="Enter the text to be written: ")
        self.text1.grid(row=0, column=0)

        self.text2 = Label(self.window, text="Enter the amount of seconds: ")
        self.text2.grid(row=1, column=0)

        self.input1 = Entry(self.window)
        self.input1.insert(0, self.text)
        self.input1.grid(row=0, column=1)

        self.input2 = Entry(self.window)
        self.input2.insert(0, self.seconds)
        self.input2.grid(row=1, column=1)

        self.text2 = Label(self.window, text="Enter \\n for new line")
        self.text2.configure(foreground="red")
        self.text2.grid(row=2, column=0)

        self.button1 = Button(self.window, text="Update", command=self.change)
        self.button1.grid(row=2, column=1, sticky='news')


class ImageWindow:
    def __init__(self, root, if_open=True):
        if if_open:
            self.window = Toplevel(root)
        else:
            self.window = Toplevel
        self.type = 4
        self.hash = secrets.token_hex(nbytes=16)
        self.size = 150
        self.confidence = StringVar()
        self.show_image = False
        self.options = [str(num/10) for num in range(1, 11)]

        self.confidence.set("0.8")

    def load(self, content):
        items = content.split("-")

        self.type = int(float(items[0]))
        self.hash = items[1]
        self.confidence.set(items[2])
        self.show_image = bool(items[3])

        self.window.withdraw()

    def save(self, file):
        with open(file, "a") as f:
            f.write(
                f"If {self.type}-{self.hash}-{self.confidence.get()}-{self.show_image}\n")

    def takeScreenShot(self):
        root = Tk()
        app = Application(root, self.hash)
        root.mainloop()

        self.show_image = True

        self.removeItems()
        self.addItems()

    def removeItems(self):
        for widget in self.window.winfo_children():
            widget.destroy()

    def change(self):
        self.window.withdraw()

    def check(self):
        if self.show_image:
            on_screen = checkImageOnScreen(
                f"./snips/{self.hash}.png", self.confidence.get())

            if not on_screen:
                self.text1.config(text="Image Not Found On Screen")
            else:
                self.text1.config(text="Image Found")
        else:
            self.text1.config(text="Take a Screenshot")

    def addItems(self):
        self.button2 = Button(self.window, text="Test If", command=self.check)
        self.button2.grid(row=0, column=0, padx=30, pady=10, sticky='news')

        self.text1 = Label(self.window, text="Haven't Tested Yet")
        self.text1.grid(row=0, column=1)

        self.canvas1 = Canvas(self.window, width=self.size,
                              height=self.size, bg='white')
        self.canvas1.grid(row=1, column=0, rowspan=2, padx=10, pady=10)

        if self.show_image:
            self.image1 = PhotoImage(file=f"./snips/{self.hash}.png")
            self.canvas1.create_image(
                self.size, self.size, image=self.image1, anchor=SE)

        self.confidence_inp = OptionMenu(
            self.window, self.confidence, *self.options)
        self.confidence_inp.grid(row=1, column=1, padx=30, pady=10)

        self.button1 = Button(
            self.window, text="Take Screenshot", command=self.takeScreenShot)
        self.button1.grid(row=2, column=1, sticky='news', padx=30, pady=10)

        self.button3 = Button(self.window, text="Update", command=self.change)
        self.button3.grid(row=3, column=0, columnspan=2,
                          padx=30, pady=10, sticky='news')


class NoneWindow:
    """
    Dummy Window
    """

    def __init__(self, root):
        self.window = Toplevel
        self.type = None
