import tkinter

from tuner_appearance.tuner_ui_parts.custum_button import CustomButton
from tuner_settings.app_settings import *


class SettingsFrame(tkinter.Frame):
    def __init__(self, master, *args, **kwargs):
        tkinter.Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.color_manager = master.color_manager
        self.image_manager = master.image_manager
        self.global_manager = master.global_manager

        self.configure(bg=self.color_manager.gray)

        self.infoFrame_bottomFrame = tkinter.Frame(master=self,
                                                   bg=self.color_manager.dark_gray)
        self.infoFrame_bottomFrame.place(relx=0,
                                         rely=0.75,
                                         relheight=0.25,
                                         relwidth=1)

        self.buttonBack = CustomButton(master=self.infoFrame_bottomFrame,
                                       custom_bg=self.color_manager.blue,
                                       text="Back",
                                       function=self.master.draw_main_frame)

        self.buttonBack.place(anchor="se",
                              relx=0.95,
                              rely=0.8,
                              height=61,
                              width=144)

        self.labelInfoText = tkinter.Label(master=self,
                                           bg=self.color_manager.gray,
                                           fg=self.color_manager.light_gray,
                                           font=("Avenir", 18),
                                           text=ABOUT_TEXT)

        self.labelInfoText.place(anchor="center",
                                 relx=0.5,
                                 rely=0.12,
                                 relheight=0.2,
                                 relwidth=0.8)

        self.labelInfoText = tkinter.Label(master=self,
                                           bg=self.color_manager.gray,
                                           fg=self.color_manager.light_gray,
                                           font=("Avenir", 32),
                                           text="A4 =")

        self.labelInfoText.place(anchor="center",
                                 relx=0.2,
                                 rely=0.45,
                                 relheight=0.1,
                                 relwidth=0.2)

        self.labelFrequency = CustomButton(master=self,
                                           custom_bg=self.color_manager.blue,
                                           text="440 Hz",
                                           hover=False)

        self.labelFrequency.place(anchor="center",
                                  relx=0.5,
                                  rely=0.45,
                                  relheight=0.15,
                                  relwidth=0.4)

        self.buttonFreqUp = CustomButton(master=self,
                                         custom_bg=self.color_manager.gray,
                                         imageset=[self.image_manager.arrowUp_image,
                                                   self.image_manager.arrowUp_image_hovered] * 2,
                                         function=self.frequency_button_up)

        self.buttonFreqUp.place(anchor="center",
                                relx=0.5,
                                rely=0.3,
                                height=50,
                                width=150)

        self.buttonFreqDown = CustomButton(master=self,
                                           custom_bg=self.color_manager.gray,
                                           imageset=[self.image_manager.arrowDown_image,
                                                     self.image_manager.arrowDown_image_hovered] * 2,
                                           function=self.frequency_button_down)

        self.buttonFreqDown.place(anchor="center",
                                  relx=0.5,
                                  rely=0.6,
                                  height=50,
                                  width=150)

    def frequency_button_up(self):
        self.global_manager.frequencyUp()
        self.labelFrequency.label.configure(text=str(self.global_manager.a4_freq) + " Hz")

    def frequency_button_down(self):
        self.global_manager.frequencyDown()
        self.labelFrequency.label.configure(text=str(self.global_manager.a4_freq) + " Hz")
