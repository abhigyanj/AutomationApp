import re
import traceback

import pyautogui

from functions import generateRandomNumber, MouseHandler, RandomWait, write, checkImageOnScreen
from gui_change_handler import MouseNewWindow, RandomDelayWindow, ImageWindow, TextWindow, NoneWindow
from tkinter import Tk, Label, OptionMenu, StringVar, Button, Toplevel, VERTICAL, END, _setit, messagebox
from tkinter.filedialog import asksaveasfilename, askopenfilename


class App:
    def __init__(self, root):
        # Pre-Configured - Title, Icon
        self.root = root
        self.text_widget_count = 0

        root.resizable(False, True)

    def setup(self):
        self.functions_text = Label(self.root, text="Functions: ")
        self.functions_text.grid(row=0, column=0, padx=(30, 30), pady=(10, 0))

        self.add_button = Button(
            self.root, text="Add Row", command=self.addTextWidget, background="lightblue")
        self.add_button.grid(row=0, column=1, padx=70, pady=(10, 0))

        self.clear_button = Button(
            self.root, text="Clear Row(s)", command=self.clearTextWidget, background="lightblue")
        self.clear_button.grid(row=0, column=2, padx=(50, 70), pady=(10, 0))

        self.load_button = Button(
            self.root, text="Load", command=self.load, background="lightgrey")
        self.load_button.grid(row=0, column=3, padx=(50, 70), pady=(10, 0))

        self.save_button = Button(
            self.root, text="Save", command=self.save, background="lightgrey")
        self.save_button.grid(row=0, column=4, padx=(50, 70), pady=(10, 0))

        self.run_button = Button(
            self.root, text="Run", command=self.run, background="lightgreen")
        self.run_button.grid(row=0, column=5, padx=(30, 70), pady=(10, 0))

    def save(self):
        file = asksaveasfilename(
            initialdir="./saves/", filetypes=[("Automation App Files", "*.aafiles")])

        if (not file == "") and (not file.endswith(".aafiles")):
            file = f"{file}.aafiles"

        open(file, 'w').close()

        clses = list(filter(lambda item: item.startswith("cls"), dir(self)))
        ifdrop = list(
            filter(lambda item: item.startswith("clickedif"), dir(self)))
        optionsdrop = list(filter(lambda item: item.startswith(
            "clicked") and "if" not in item, dir(self)))

        for i, (name, drop1, drop2) in enumerate(zip(clses, ifdrop, optionsdrop)):
            cls = getattr(self, name)
            drop1 = getattr(self, drop1)
            drop2 = getattr(self, drop2)

            op1 = drop1.get()

            if op1 == "Do":
                if cls.type == 1:
                    cls.save(file)
                elif cls.type == 2:
                    cls.save(file)
                elif cls.type == 3:
                    cls.save(file)
                elif cls.type == 4:
                    cls.save(file)
            elif op1 == "If":
                cls.save(file)
            else:
                with open(file, "a") as f:
                    f.write(f"{op1}\n")

    def load(self):
        file = askopenfilename(initialdir="./saves/")

        if file.endswith(".aafiles"):
            self.clearTextWidget()

            with open(file) as f:
                content = f.read()

            lines = content.split("\n")
            self.text_widget_count = 0

            for line in lines:
                if line != "":
                    self.text_widget_count += 1
                    if line.startswith("Do"):
                        cls_type = int(line[3])

                        if cls_type == 1:
                            setattr(
                                self, f"clicked{self.text_widget_count}", StringVar())
                            getattr(self, f"clicked{self.text_widget_count}").set(
                                "1 - Move Mouse")

                            win = MouseNewWindow(self.root)
                            setattr(self, f"cls{self.text_widget_count}", win)

                            win.load(line[3:])

                        elif cls_type == 2:
                            setattr(
                                self, f"clicked{self.text_widget_count}", StringVar())
                            getattr(self, f"clicked{self.text_widget_count}").set(
                                "2 - Random Delay")

                            win = RandomDelayWindow(self.root)
                            setattr(self, f"cls{self.text_widget_count}", win)

                            win.load(line[3:])

                        elif cls_type == 3:
                            setattr(
                                self, f"clicked{self.text_widget_count}", StringVar())
                            getattr(self, f"clicked{self.text_widget_count}").set(
                                "3 - Write Text")

                            win = TextWindow(self.root)
                            setattr(self, f"cls{self.text_widget_count}", win)

                            win.load(line[3:])

                        setattr(
                            self, f"clickedif{self.text_widget_count}", StringVar())
                        getattr(self, f"clickedif{self.text_widget_count}").set(
                            "Do")
                        getattr(self, f"clickedif{self.text_widget_count}").trace(
                            "w", lambda *args, val=self.text_widget_count: self.optionChanged(val))

                        setattr(self, f"if{self.text_widget_count}", OptionMenu(self.root, getattr(
                            self, f"clickedif{self.text_widget_count}"), "Do", "If", "Else", "End If", "End Else"))
                        setattr(self, f"button{self.text_widget_count}", Button(
                            text="Change Functionality", command=lambda val=self.text_widget_count: self.functionalityHandler(val)))
                        setattr(self, f"dropdown{self.text_widget_count}", OptionMenu(self.root, getattr(
                            self, f"clicked{self.text_widget_count}"), "1 - Move Mouse", "2 - Random Delay", "3 - Write Text"))

                    elif line.startswith("If"):
                        cls_type = int(line[3])

                        if cls_type == 4:
                            setattr(
                                self, f"clicked{self.text_widget_count}", StringVar())
                            getattr(self, f"clicked{self.text_widget_count}").set(
                                "4 - Image Recogntion")

                            win = ImageWindow(self.root)
                            setattr(self, f"cls{self.text_widget_count}", win)

                            win.load(line[3:])

                        setattr(
                            self, f"clickedif{self.text_widget_count}", StringVar())
                        getattr(self, f"clickedif{self.text_widget_count}").set(
                            "If")
                        getattr(self, f"clickedif{self.text_widget_count}").trace(
                            "w", lambda *args, val=self.text_widget_count: self.optionChanged(val))

                        setattr(self, f"if{self.text_widget_count}", OptionMenu(self.root, getattr(
                            self, f"clickedif{self.text_widget_count}"), "Do", "If", "Else", "End If", "End Else"))
                        setattr(self, f"button{self.text_widget_count}", Button(
                            text="Change Functionality", command=lambda val=self.text_widget_count: self.functionalityHandler(val)))
                        setattr(self, f"dropdown{self.text_widget_count}", OptionMenu(self.root, getattr(
                            self, f"clicked{self.text_widget_count}"), "4 - Image Recogntion"))

                    else:
                        setattr(
                            self, f"clicked{self.text_widget_count}", StringVar())
                        getattr(self, f"clicked{self.text_widget_count}").set(
                            "None")

                        win = NoneWindow(self.root)
                        setattr(self, f"cls{self.text_widget_count}", win)

                        setattr(
                            self, f"clickedif{self.text_widget_count}", StringVar())
                        getattr(self, f"clickedif{self.text_widget_count}").set(
                            line.strip())
                        getattr(self, f"clickedif{self.text_widget_count}").trace(
                            "w", lambda *args, val=self.text_widget_count: self.optionChanged(val))

                        setattr(self, f"if{self.text_widget_count}", OptionMenu(self.root, getattr(
                            self, f"clickedif{self.text_widget_count}"), "Do", "If", "Else", "End If", "End Else"))
                        setattr(self, f"button{self.text_widget_count}", Button(
                            text="Change Functionality", command=lambda val=self.text_widget_count: self.functionalityHandler(val)))
                        setattr(self, f"dropdown{self.text_widget_count}", OptionMenu(self.root, getattr(
                            self, f"clicked{self.text_widget_count}"), "None"))

                    i = getattr(self, f"if{self.text_widget_count}")
                    b = getattr(self, f"button{self.text_widget_count}")
                    d = getattr(self, f"dropdown{self.text_widget_count}")

                    if self.text_widget_count == 1:
                        i.grid(row=self.text_widget_count + 2,
                               column=0, pady=(50, 10), padx=(10, 0))
                        d.grid(row=self.text_widget_count +
                               2, column=1, pady=(50, 10))
                        b.grid(row=self.text_widget_count +
                               2, column=2, pady=(50, 10))
                    else:
                        i.grid(row=self.text_widget_count + 2,
                               column=0, pady=(0, 10), padx=(10, 0))
                        d.grid(row=self.text_widget_count +
                               2, column=1, pady=(0, 10))
                        b.grid(row=self.text_widget_count +
                               2, column=2, pady=(0, 10))

        else:
            messagebox.showerror("Invaid File Type",
                                 'The file is not a vaild type.')

    def run(self):
        ifstarted = False
        elsestarted = False

        doif = False
        doelse = False

        try:
            clses = list(
                filter(lambda item: item.startswith("cls"), dir(self)))
            ifdrop = list(
                filter(lambda item: item.startswith("clickedif"), dir(self)))
            optionsdrop = list(filter(lambda item: item.startswith(
                "clicked") and "if" not in item, dir(self)))

            for i, (name, drop1, drop2) in enumerate(zip(clses, ifdrop, optionsdrop)):
                drop1 = getattr(self, drop1)
                drop2 = getattr(self, drop2)
                cls = getattr(self, name)

                op1 = drop1.get()
                op2 = drop2.get()

                if op1 == "If":
                    if cls.show_image:
                        on_screen = checkImageOnScreen(
                            f"./snips/{cls.hash}.png", cls.confidence.get())

                        if on_screen:
                            doif = True
                            doelse = False
                        else:
                            doif = False
                            doelse = True
                    else:
                        raise NotImplementedError(
                            f"Add A Screenshot On Line {i}")

                    ifstarted = True

                elif op1 == "End If":
                    ifstarted = False

                elif op1 == "Else":
                    elsestarted = True

                elif op1 == "End Else":
                    elsestarted = False

                elif op1 == "Do":
                    if (ifstarted and doif) or ((not ifstarted) and not (elsestarted)) or (elsestarted and doelse):
                        if cls.type == 1:
                            mh = MouseHandler()
                            mh.move((
                                cls.start_x +
                                    generateRandomNumber(-cls.offset, cls.offset), cls.start_y +
                                    generateRandomNumber(-cls.offset,
                                                         cls.offset)
                                    ), (
                                cls.end_x +
                                    generateRandomNumber(-cls.offset, cls.offset), cls.end_y +
                                    generateRandomNumber(-cls.offset,
                                                         cls.offset)
                                    ),  cls.seconds
                                    )

                            option = cls.option.get()

                            if option.startswith("Left"):
                                pyautogui.click()

                            elif option.startswith("No"):
                                pass

                            elif option.startswith("Right"):
                                pyautogui.click(button='right')

                            elif option.startswith("Double"):
                                pyautogui.click(clicks=2)
                        elif cls.type == 2:
                            rw = RandomWait(cls.random_wait, cls.random_offset)
                            rw.wait()
                        elif cls.type == 3:
                            write(cls.text, cls.seconds)
                        else:
                            raise Exception(
                                f"This should never happen, please send a mail to 'abhigyanjj@gmail.com' about the scenario, send the following info, NUM:{cls.type} NUM_TYPE:{type(cls.type)}")

            if ifstarted and not elsestarted:
                messagebox.showerror("An Error Occured", "'If' wasn't ended")
            if not ifstarted and elsestarted:
                messagebox.showerror("An Error Occured", "'Else' wasn't ended")
            if ifstarted and elsestarted:
                messagebox.showerror("An Error Occured",
                                     "'If' and 'Else' wasn't ended")

        except Exception as e:
            messagebox.showerror("An Error Occured", ''.join(
                traceback.format_exception(None, e, e.__traceback__)))

    def functionalityHandler(self, count):
        win_type = getattr(self, f"clicked{count}")

        if win_type.get().startswith("1"):
            win = getattr(self, f"cls{count}", None)

            if not isinstance(win, MouseNewWindow):
                win = MouseNewWindow(self.root)
                setattr(self, f"cls{count}", win)
            else:
                try:
                    win.window.deiconify()
                except Exception:
                    win = MouseNewWindow(self.root)
                    setattr(self, f"cls{count}", win)

            win.addItems()

        elif win_type.get().startswith("2"):
            win = getattr(self, f"cls{count}", None)

            if not isinstance(win, RandomDelayWindow):
                win = RandomDelayWindow(self.root)
                setattr(self, f"cls{count}", win)
            else:
                try:
                    win.window.deiconify()
                except Exception:
                    win = RandomDelayWindow(self.root)
                    setattr(self, f"cls{count}", win)

            win.addItems()

        elif win_type.get().startswith("3"):
            win = getattr(self, f"cls{count}", None)

            if not isinstance(win, TextWindow):
                win = TextWindow(self.root)
                setattr(self, f"cls{count}", win)
            else:
                try:
                    win.window.deiconify()
                except Exception:
                    win = TextWindow(self.root)
                    setattr(self, f"cls{count}", win)

            win.addItems()

        elif win_type.get().startswith("4"):
            win = getattr(self, f"cls{count}", None)

            if not isinstance(win, ImageWindow):
                win = ImageWindow(self.root)
                setattr(self, f"cls{count}", win)
            else:
                try:
                    win.window.deiconify()
                except Exception:
                    win = ImageWindow(self.root)
                    setattr(self, f"cls{count}", win)

            win.addItems()

        else:
            win = getattr(self, f"cls{count}", None)

            if not isinstance(win, NoneWindow):
                win = NoneWindow(self.root)
                setattr(self, f"cls{count}", win)
            else:
                try:
                    win.window.deiconify()
                except Exception:
                    win = NoneWindow(self.root)
                    setattr(self, f"cls{count}", win)

        # getattr(self, f"button{count}").config(text="Change Functionality")

    def clearTextWidget(self):
        items = list(filter(lambda item: item.startswith("button") or item.startswith("dropdown") or item.startswith(
            "clicked") or item.startswith("if") or item.startswith("clicked") or item.startswith("cls"), dir(self)))

        for item in items:
            try:
                getattr(self, item).grid_forget()
            except AttributeError:
                pass
            finally:
                delattr(self, item)

        self.text_widget_count = 0

    def optionChanged(self, count):
        dropdown = getattr(self, f"dropdown{count}")
        var1 = getattr(self, f"clicked{count}")
        var2 = getattr(self, f"clickedif{count}").get()

        if var2 == "If":
            if not var1.get().startswith("4"):
                var1.set("4 - Image Recogntion")
            dropdown["menu"].delete(0, END)

            new_choices = ("4 - Image Recogntion", )

            for choice in new_choices:
                dropdown['menu'].add_command(
                    label=choice, command=_setit(var1, choice))

        elif var2 == "Do":
            if var1.get().startswith("4") or var1.get().startswith("None"):
                var1.set("1 - Move Mouse")

            dropdown["menu"].delete(0, END)

            new_choices = ("1 - Move Mouse",
                           "2 - Random Delay", "3 - Write Text")

            for choice in new_choices:
                dropdown['menu'].add_command(
                    label=choice, command=_setit(var1, choice))

        else:
            if not var1.get().startswith("None"):
                var1.set("None")
            dropdown["menu"].delete(0, END)

            new_choices = ("None",)

            for choice in new_choices:
                dropdown['menu'].add_command(
                    label=choice, command=_setit(var1, choice))

        self.functionalityHandler(count)

    def addTextWidget(self):
        self.text_widget_count += 1

        setattr(self, f"clicked{self.text_widget_count}", StringVar())
        getattr(self, f"clicked{self.text_widget_count}").set("1 - Move Mouse")

        setattr(self, f"clickedif{self.text_widget_count}", StringVar())
        getattr(self, f"clickedif{self.text_widget_count}").set("Do")
        getattr(self, f"clickedif{self.text_widget_count}").trace(
            "w", lambda *args, val=self.text_widget_count: self.optionChanged(val))

        setattr(self, f"if{self.text_widget_count}", OptionMenu(self.root, getattr(
            self, f"clickedif{self.text_widget_count}"), "Do", "If", "Else", "End If", "End Else"))
        setattr(self, f"button{self.text_widget_count}", Button(
            text="Change Functionality", command=lambda val=self.text_widget_count: self.functionalityHandler(val)))
        setattr(self, f"dropdown{self.text_widget_count}", OptionMenu(self.root, getattr(
            self, f"clicked{self.text_widget_count}"), "1 - Move Mouse", "2 - Random Delay", "3 - Write Text"))

        i = getattr(self, f"if{self.text_widget_count}")
        b = getattr(self, f"button{self.text_widget_count}")
        d = getattr(self, f"dropdown{self.text_widget_count}")

        if self.text_widget_count == 1:
            i.grid(row=self.text_widget_count + 2,
                   column=0, pady=(50, 10), padx=(10, 0))
            d.grid(row=self.text_widget_count + 2, column=1, pady=(50, 10))
            b.grid(row=self.text_widget_count + 2, column=2, pady=(50, 10))
        else:
            i.grid(row=self.text_widget_count + 2,
                   column=0, pady=(0, 10), padx=(10, 0))
            d.grid(row=self.text_widget_count + 2, column=1, pady=(0, 10))
            b.grid(row=self.text_widget_count + 2, column=2, pady=(0, 10))

        self.functionalityHandler(self.text_widget_count)


if __name__ == '__main__':
    root = Tk()

    root.title("Automation App")
    root.geometry("1000x600+192+192")

    app = App(root)

    app.setup()
    # app.addTextWidget()

    root.mainloop()
