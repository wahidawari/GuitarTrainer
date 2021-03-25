import tkinter

from tuner_ui_parts.custom_button_image import CustomButton
from tuner_ui_parts.custom_button_rounded import RoundedButton
from settings import Settings
from PIL import Image
from tuner_appearance_manager.image_manager import ImageManager


class ChordsFrame(tkinter.Frame):
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

        self.botton_frame = tkinter.Frame(master=self, bg=self.color_manager.background_layer_0)
        self.botton_frame.place(relx=0,
                                rely=0.5,
                                relheight=0.5,
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
                                         function=self.master.draw_settings_frame)

        self.button_exit.place(anchor="se",
                                relx=0.95,
                                rely=0.9)


        self.button_back = RoundedButton(master=self,
                                         bg_color=self.color_manager.background_layer_1,
                                         fg_color=self.color_manager.theme_main,
                                         hover_color=self.color_manager.theme_light,
                                         text_font=("Avenir", 18),
                                         text="Bm",
                                         text_color=self.color_manager.text_main,
                                         corner_radius=10,
                                         width=100,
                                         height=45,
                                         function=self.master.draw_bm_chord_frame)

        self.button_back.place(anchor="n",
                               relx=0.9,
                               rely=0.15,
                               height=45,
                               width=100)
        
        #tuner tab button
        self.button_back = RoundedButton(master=self,
                                         bg_color=self.color_manager.background_layer_1,
                                         fg_color=self.color_manager.theme_main,
                                         hover_color=self.color_manager.theme_light,
                                         text_font=("Avenir", 18),
                                         text="A",
                                         text_color=self.color_manager.text_main,
                                         corner_radius=10,
                                          width=100,
                                         height=45,
                                         function=self.master.draw_a_chord_frame)

        self.button_back.place(anchor="n",
                               relx=0.1,
                               rely=0.15,
                               height=45,
                               width=100)
        #trainer tab button
        self.button_back = RoundedButton(master=self,
                                         bg_color=self.color_manager.background_layer_1,
                                         fg_color=self.color_manager.theme_main,
                                         hover_color=self.color_manager.theme_light,
                                         text_font=("Avenir", 18),
                                         text="Am",
                                         text_color=self.color_manager.text_main,
                                         corner_radius=10,
                                          width=100,
                                         height=45,
                                         function=self.master.draw_am_chord_frame)

        self.button_back.place(anchor="n",
                               relx=0.35,
                               rely=0.15,
                               height=45,
                                width=100)
        #pictures frame button
        self.button_back = RoundedButton(master=self,
                                         bg_color=self.color_manager.background_layer_1,
                                         fg_color=self.color_manager.theme_main,
                                         hover_color=self.color_manager.theme_light,
                                         text_font=("Avenir", 18),
                                         text="B",
                                         text_color=self.color_manager.text_main,
                                         corner_radius=10,
                                          width=100,
                                         height=45,
                                         function=self.master.draw_b_chord_frame)

        self.button_back.place(anchor="n",
                               relx=0.65,
                               rely=0.15,
                               height=45,
                                width=100)

        self.button_back = RoundedButton(master=self,
                                         bg_color=self.color_manager.background_layer_1,
                                         fg_color=self.color_manager.theme_main,
                                         hover_color=self.color_manager.theme_light,
                                         text_font=("Avenir", 18),
                                         text="Dm",
                                         text_color=self.color_manager.text_main,
                                         corner_radius=10,
                                         width=100,
                                         height=45,
                                         function=self.master.draw_dm_chord_frame)

        self.button_back.place(anchor="n",
                               relx=0.9,
                               rely=0.35,
                               height=45,
                               width=100)
        
        #tuner tab button
        self.button_back = RoundedButton(master=self,
                                         bg_color=self.color_manager.background_layer_1,
                                         fg_color=self.color_manager.theme_main,
                                         hover_color=self.color_manager.theme_light,
                                         text_font=("Avenir", 18),
                                         text="C",
                                         text_color=self.color_manager.text_main,
                                         corner_radius=10,
                                          width=100,
                                         height=45,
                                         function=self.master.draw_c_chord_frame)

        self.button_back.place(anchor="n",
                               relx=0.1,
                               rely=0.35,
                               height=45,
                               width=100)
        #trainer tab button
        self.button_back = RoundedButton(master=self,
                                         bg_color=self.color_manager.background_layer_1,
                                         fg_color=self.color_manager.theme_main,
                                         hover_color=self.color_manager.theme_light,
                                         text_font=("Avenir", 18),
                                         text="Cm",
                                         text_color=self.color_manager.text_main,
                                         corner_radius=10,
                                          width=100,
                                         height=45,
                                         function=self.master.draw_cm_chord_frame)

        self.button_back.place(anchor="n",
                               relx=0.35,
                               rely=0.35,
                               height=45,
                                width=100)
        #pictures frame button
        self.button_back = RoundedButton(master=self,
                                         bg_color=self.color_manager.background_layer_1,
                                         fg_color=self.color_manager.theme_main,
                                         hover_color=self.color_manager.theme_light,
                                         text_font=("Avenir", 18),
                                         text="D",
                                         text_color=self.color_manager.text_main,
                                         corner_radius=10,
                                          width=100,
                                         height=45,
                                         function=self.master.draw_d_chord_frame)

        self.button_back.place(anchor="n",
                               relx=0.65,
                               rely=0.35,
                               height=45,
                                width=100)
        
        self.button_back = RoundedButton(master=self,
                                         bg_color=self.color_manager.background_layer_1,
                                         fg_color=self.color_manager.theme_main,
                                         hover_color=self.color_manager.theme_light,
                                         text_font=("Avenir", 18),
                                         text="Gm",
                                         text_color=self.color_manager.text_main,
                                         corner_radius=10,
                                         width=100,
                                         height=45,
                                         function=self.master.draw_gm_chord_frame)

        self.button_back.place(anchor="n",
                               relx=0.9,
                               rely=0.55,
                               height=45,
                               width=100)
        
        #tuner tab button
        self.button_back = RoundedButton(master=self,
                                         bg_color=self.color_manager.background_layer_1,
                                         fg_color=self.color_manager.theme_main,
                                         hover_color=self.color_manager.theme_light,
                                         text_font=("Avenir", 18),
                                         text="E",
                                         text_color=self.color_manager.text_main,
                                         corner_radius=10,
                                          width=100,
                                         height=45,
                                         function=self.master.draw_e_chord_frame)

        self.button_back.place(anchor="n",
                               relx=0.1,
                               rely=0.55,
                               height=45,
                               width=100)
        #trainer tab button
        self.button_back = RoundedButton(master=self,
                                         bg_color=self.color_manager.background_layer_1,
                                         fg_color=self.color_manager.theme_main,
                                         hover_color=self.color_manager.theme_light,
                                         text_font=("Avenir", 18),
                                         text="Em",
                                         text_color=self.color_manager.text_main,
                                         corner_radius=10,
                                          width=100,
                                         height=45,
                                         function=self.master.draw_em_chord_frame)

        self.button_back.place(anchor="n",
                               relx=0.35,
                               rely=0.55,
                               height=45,
                                width=100)
        #pictures frame button
        self.button_back = RoundedButton(master=self,
                                         bg_color=self.color_manager.background_layer_1,
                                         fg_color=self.color_manager.theme_main,
                                         hover_color=self.color_manager.theme_light,
                                         text_font=("Avenir", 18),
                                         text="G",
                                         text_color=self.color_manager.text_main,
                                         corner_radius=10,
                                          width=100,
                                         height=45,
                                         function=self.master.draw_g_chord_frame)

        self.button_back.place(anchor="n",
                               relx=0.65,
                               rely=0.55,
                               height=45,
                                width=100)
       


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


