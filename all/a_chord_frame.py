import tkinter as tk
import tkinter
from tkinter import *
from tuner_ui_parts.custom_button_image import CustomButton
from tuner_ui_parts.custom_button_rounded import RoundedButton
from PIL import ImageTk, Image
from settings import Settings
from PIL import Image
from chords_frame import ChordsFrame

class AchordFrame(tkinter.Frame):
   def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
       
        self.app_pointer = master
        self.color_manager = master.color_manager
        self.image_manager = master.image_manager
        image1 = Image.open(r"C:\Users\wahid\Documents\GuitarTrainer-master\all\assets\images\a.png")
        test = ImageTk.PhotoImage(image1)

        label1 = tkinter.Label(self, image=test)
        label1.image = test

        label1.pack()
    
        text = Label(self, text = "A Chord")
        text.pack()

        


        self.botton_frame = tkinter.Frame(master=self, bg=self.color_manager.background_layer_0)
        self.botton_frame.place(relx=0,
                                rely=0.85,
                                relheight=0.1,
                                relwidth=1)

        self.button_exit = RoundedButton(master=self.botton_frame,
                                         bg_color=self.color_manager.background_layer_0,
                                         fg_color=self.color_manager.theme_main,
                                         hover_color=self.color_manager.theme_light,
                                         text_font=("Avenir", 18),
                                         text="Exit",
                                         text_color=self.color_manager.text_main,
                                         corner_radius=10,
                                         width=120,
                                         height=45,
                                         function=self.master.draw_chords_frame)

        self.button_exit.place(anchor="se",
                                relx=0.95,
                                rely=0.9)