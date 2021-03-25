import tkinter as tk                # python 3
from tkinter import font as tkfont  # python 3
from PIL import ImageTk, Image
import numpy as np
import pyaudio
import os



class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)

    #this is for the appearnce ,copied from main.py



        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, PageFive):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()






class StartPage(tk.Frame):

    def __init__(self, master, *args, **kwargs,):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.controller = controller
        label = tk.Label(self, text="This is the start page")
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Learn Chords",
                            command=lambda: controller.show_frame("PageOne"))
        button1.pack()

        button2 = tk.Button(self, text="Tune Your Guitar",
                            command=lambda: controller.show_frame("PageTwo"))
        button2.pack()
        


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        ##### ADD IMAGE TO SCREEN ####
        render = ImageTk.PhotoImage(Image.open(r'pictures\e.png'))
        # Assigns the image to the label
        img = tk.Label(self, image=render)
        # Renders the image to the screen
        img.image = render
        # Places the image (numbers based on the top left corner of the image I think)
        img.place(x = 1500 // 4, y = 900 // 4)
        ##############################
        
        button = tk.Button(self, text="Go to the Next page",
                           command=lambda: controller.show_frame("PageTwo"))
        button.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        ##### ADD IMAGE TO SCREEN ####
        render = ImageTk.PhotoImage(Image.open(r'\pictures\em.png'))
        # Assigns the image to the label
        img = tk.Label(self, image=render)
        # Renders the image to the screen
        img.image = render
        # Places the image (numbers based on the top left corner of the image I think)
        img.place(x = 1500 // 4, y = 900 // 4)
        ##############################
        button = tk.Button(self, text="Go to the Next page",
                           command=lambda: controller.show_frame("PageThree"))
        button.pack()
        button = tk.Button(self, text="Go to the Previous page",
                           command=lambda: controller.show_frame("PageOne"))
        button.pack()
        


class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        ##### ADD IMAGE TO SCREEN ####
        render = ImageTk.PhotoImage(Image.open(r'\pictures\d.png'))
        # Assigns the image to the label
        img = tk.Label(self, image=render)
        # Renders the image to the screen
        img.image = render
        # Places the image (numbers based on the top left corner of the image I think)
        img.place(x = 1500 // 4, y = 900 // 4)
        ##############################
        
        
        button = tk.Button(self, text="Go to the Next page",
                           command=lambda: controller.show_frame("PageFour"))
        button.pack()

        button = tk.Button(self, text="Go to the Previous page",
                           command=lambda: controller.show_frame("PageTwo"))
        button.pack()
       
class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        ##### ADD IMAGE TO SCREEN ####
        render = ImageTk.PhotoImage(Image.open(r'C:\pictures\c.png'))
        # Assigns the image to the label
        img = tk.Label(self, image=render)
        # Renders the image to the screen
        img.image = render
        # Places the image (numbers based on the top left corner of the image I think)
        img.place(x = 1500 // 4, y = 900 // 4)
        ##############################
        button = tk.Button(self, text="Go to the Next page",
                           command=lambda: controller.show_frame("PageFive"))
        button.pack()
        button = tk.Button(self, text="Go to the Previous page",
                           command=lambda: controller.show_frame("PageThree"))
        button.pack()
       


class PageFive(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        ##### ADD IMAGE TO SCREEN ####
        render = ImageTk.PhotoImage(Image.open(r'\pictures\a.png'))
        # Assigns the image to the label
        img = tk.Label(self, image=render)
        # Renders the image to the screen
        img.image = render
        # Places the image (numbers based on the top left corner of the image I think)
        img.place(x = 1500 // 4, y = 900 // 4)
        ##############################
        
        button = tk.Button(self, text="Go to the Previous page",
                           command=lambda: controller.show_frame("PageTwo"))
        button.pack()
        button = tk.Button(self, text="Go to the Home Page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()



       


if __name__ == "__main__":
    app = SampleApp()
    # Sets the size of the window
    app.geometry("1500x900")
    app.mainloop()