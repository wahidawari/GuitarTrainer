import tkinter
from math import sin, radians

from tuner_ui_parts.custom_button_image import CustomButton
from tuner_ui_parts.custom_button_rounded import RoundedButton
from settings import Settings


class TrainerFrame(tkinter.Frame):
    def __init__(self, master, *args, **kwargs):
        tkinter.Frame.__init__(self, master, *args, **kwargs)

        self.app_pointer = master
        self.color_manager = master.color_manager
        self.image_manager = master.image_manager
        self.image_manager = master.image_manager

        self.configure(bg=self.color_manager.background_layer_1)

        self.under_canvas = tkinter.Canvas(master=self,
                                           bg=self.color_manager.background_layer_1,
                                           highlightthickness=0)

        self.under_canvas.place(anchor="center",
                                relx=0.5,
                                rely=0.5,
                                height=Settings.CANVAS_SIZE,
                                width=Settings.CANVAS_SIZE)


        

        self.display_background_line = self.under_canvas.create_line(Settings.CANVAS_SIZE * 0.5,
                                                                     Settings.CANVAS_SIZE * 0.5,
                                                                     Settings.CANVAS_SIZE * 0.5,
                                                                     -Settings.CANVAS_SIZE * 0.5,
                                                                     fill=self.color_manager.background_layer_1,
                                                                     width=Settings.CANVAS_SIZE * 0.06)

        

        self.display_inner_circle_1 = self.under_canvas.create_oval(Settings.CANVAS_SIZE * 0.2,
                                                                    Settings.CANVAS_SIZE * 0.2,
                                                                    Settings.CANVAS_SIZE * 0.8,
                                                                    Settings.CANVAS_SIZE * 0.8,
                                                                    fill=self.color_manager.theme_dark,
                                                                    width=0)

        self.botton_frame = tkinter.Frame(master=self, bg=self.color_manager.background_layer_0)
        self.botton_frame.place(relx=0,
                                rely=0.5,
                                relheight=0.5,
                                relwidth=1)

        self.upper_canvas = tkinter.Canvas(master=self.botton_frame,
                                           bg=self.color_manager.background_layer_0,
                                           highlightthickness=0)
        self.upper_canvas.place(anchor="n",
                                relx=0.5,
                                rely=0,
                                height=Settings.CANVAS_SIZE / 2,
                                width=Settings.CANVAS_SIZE)

        self.display_inner_circle_2 = self.upper_canvas.create_oval(Settings.CANVAS_SIZE * 0.2,
                                                                    -Settings.CANVAS_SIZE * 0.3,
                                                                    Settings.CANVAS_SIZE * 0.8,
                                                                    Settings.CANVAS_SIZE * 0.3,
                                                                    fill=self.color_manager.theme_dark,
                                                                    width=0)

        self.note_label = tkinter.Label(master=self,
                                        text="A",
                                        bg=self.color_manager.theme_dark,
                                        fg=self.color_manager.text_2,
                                        font=("Avenir", 80))

        self.note_label.place(relx=0.5,
                              rely=0.5,
                              anchor="center")

        

       
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

        

    def update_color(self):
        self.configure(bg=self.color_manager.background_layer_1)

        self.under_canvas.configure(bg=self.color_manager.background_layer_1)
        self.under_canvas.itemconfig(self.display_background_line, fill=self.color_manager.background_layer_1)
        
        self.under_canvas.itemconfig(self.display_inner_circle_1, fill=self.color_manager.theme_dark)

        self.upper_canvas.configure(bg=self.color_manager.background_layer_0)
        self.upper_canvas.itemconfig(self.display_inner_circle_2, fill=self.color_manager.theme_dark)

        self.note_label.configure(bg=self.color_manager.theme_dark, fg=self.color_manager.text_2)
        

        self.botton_frame.configure(bg=self.color_manager.background_layer_0)

        

        

   

       