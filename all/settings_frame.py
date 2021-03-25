import tkinter

from tuner_ui_parts.custom_button_image import CustomButton
from tuner_ui_parts.custom_button_rounded import RoundedButton
from settings import Settings
from PIL import Image
from tuner_appearance_manager.image_manager import ImageManager


class SettingsFrame(tkinter.Frame):
    def __init__(self, master, *args, **kwargs):
        tkinter.Frame.__init__(self, master, *args, **kwargs)

        self.app_pointer = master
        self.color_manager = master.color_manager
        self.image_manager = master.image_manager

        self.configure(bg=self.color_manager.background_layer_1)

        self.bottom_frame = tkinter.Frame(master=self,
                                          bg=self.color_manager.background_layer_0)
        self.bottom_frame.place(relx=0,
                                rely=0.8,
                                relheight=0.2,
                                relwidth=1)

        self.button_back = RoundedButton(master=self,
                                         bg_color=self.color_manager.background_layer_1,
                                         fg_color=self.color_manager.theme_main,
                                         hover_color=self.color_manager.theme_light,
                                         text_font=("Avenir", 18),
                                         text="Chords",
                                         text_color=self.color_manager.text_main,
                                         corner_radius=10,
                                         width=120,
                                         height=45,
                                         function=self.master.draw_chords_frame)

        self.button_back.place(anchor="n",
                               relx=0.8,
                               rely=0.30,
                               height=45,
                               width=120)
        
        #tuner tab button
        self.button_back = RoundedButton(master=self,
                                         bg_color=self.color_manager.background_layer_1,
                                         fg_color=self.color_manager.theme_main,
                                         hover_color=self.color_manager.theme_light,
                                         text_font=("Avenir", 18),
                                         text="Tuner",
                                         text_color=self.color_manager.text_main,
                                         corner_radius=10,
                                         width=120,
                                         height=45,
                                         function=self.master.draw_main_frame)

        self.button_back.place(anchor="n",
                               relx=0.2,
                               rely=0.30,
                               height=45,
                               width=120)
        #trainer tab button
        self.button_back = RoundedButton(master=self,
                                         bg_color=self.color_manager.background_layer_1,
                                         fg_color=self.color_manager.theme_main,
                                         hover_color=self.color_manager.theme_light,
                                         text_font=("Avenir", 18),
                                         text="Trainer",
                                         text_color=self.color_manager.text_main,
                                         corner_radius=10,
                                         width=120,
                                         height=45,
                                         function=self.master.draw_trainer_frame)

        self.button_back.place(anchor="n",
                               relx=0.5,
                               rely=0.30,
                               height=45,
                               width=120)
        #pictures frame button
        
        

       


    def update_color(self):
        self.configure(bg=self.color_manager.background_layer_1)
        self.bottom_frame.configure(bg=self.color_manager.background_layer_0)

        self.button_back.configure_color(bg_color=self.color_manager.background_layer_0,
                                         fg_color=self.color_manager.theme_main,
                                         hover_color=self.color_manager.theme_light,
                                         text_color=self.color_manager.text_main)

        self.label_info_text.configure(bg=self.color_manager.background_layer_1, fg=self.color_manager.text_2)
        self.label_note_text.configure(bg=self.color_manager.background_layer_1, fg=self.color_manager.text_2)

        self.label_frequency.configure_color(bg_color=self.color_manager.background_layer_1,
                                             fg_color=self.color_manager.theme_main,
                                             hover_color=self.color_manager.theme_light,
                                             text_color=self.color_manager.text_main)

        self.button_frequency_up.label.configure(bg=self.color_manager.background_layer_1)
        self.button_frequency_down.label.configure(bg=self.color_manager.background_layer_1)

    def frequency_button_up(self):
        self.master.a4_frequency += 1
        self.label_frequency.set_text(str(self.master.a4_frequency) + " Hz")

    def frequency_button_down(self):
        self.master.a4_frequency -= 1
        self.label_frequency.set_text(str(self.master.a4_frequency) + " Hz")


