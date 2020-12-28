import tkinter
from math import sin, radians

from tuner_appearance.tuner_ui_parts.custum_button import CustomButton
from tuner_settings.app_settings import *


class MainFrame(tkinter.Frame):
    def __init__(self, master, *args, **kwargs):
        tkinter.Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.color_manager = master.color_manager
        self.image_manager = master.image_manager
        self.image_manager = master.image_manager

        self.configure(bg=self.color_manager.gray)

        self.underCanvas = tkinter.Canvas(master=self,
                                          bg=self.color_manager.gray,
                                          highlightthickness=0)

        self.underCanvas.place(anchor="center",
                               relx=0.5,
                               rely=0.5,
                               height=CANVAS_SIZE,
                               width=CANVAS_SIZE)

        self.underCanvas.create_oval(0,
                                     0,
                                     CANVAS_SIZE - 1,
                                     CANVAS_SIZE - 1,
                                     fill=self.color_manager.blue,
                                     outline=self.color_manager.blue)

        self.underCanvas.create_line(CANVAS_SIZE * 0.5,
                                     CANVAS_SIZE * 0.5,
                                     CANVAS_SIZE * 0.5,
                                     -CANVAS_SIZE * 0.5,
                                     fill=self.color_manager.gray,
                                     width=CANVAS_SIZE * 0.06)

        self.needle = self.underCanvas.create_line(CANVAS_SIZE * 0.5,
                                              CANVAS_SIZE * 0.5,
                                              CANVAS_SIZE * 0.5,
                                              CANVAS_SIZE * 0.05,
                                              fill=self.color_manager.red,
                                              width=CANVAS_SIZE * 0.03)

        self.underCanvas.create_oval(CANVAS_SIZE * 0.2,
                                     CANVAS_SIZE * 0.2,
                                     CANVAS_SIZE * 0.8,
                                     CANVAS_SIZE * 0.8,
                                     fill=self.color_manager.dark_blue,
                                     outline=self.color_manager.dark_blue)

        self.mainFrame_bottomFrame = tkinter.Frame(master=self, bg=self.color_manager.dark_gray)
        self.mainFrame_bottomFrame.place(relx=0,
                                         rely=0.5,
                                         relheight=0.5,
                                         relwidth=1)

        self.upperCanvas = tkinter.Canvas(master=self.mainFrame_bottomFrame,
                                          bg=self.color_manager.dark_gray,
                                          highlightthickness=0)
        self.upperCanvas.place(anchor="n",
                               relx=0.5,
                               rely=0,
                               height=CANVAS_SIZE / 2,
                               width=CANVAS_SIZE)

        self.upperCanvas.create_oval(CANVAS_SIZE * 0.2,
                                     -CANVAS_SIZE * 0.3,
                                     CANVAS_SIZE * 0.8,
                                     CANVAS_SIZE * 0.3,
                                     fill=self.color_manager.dark_blue,
                                     outline=self.color_manager.dark_blue)

        self.noteLabel = tkinter.Label(master=self,
                                       text="A",
                                       bg=self.color_manager.dark_blue,
                                       fg=self.color_manager.light_gray,
                                       font=("Avenir", 80))

        self.noteLabel.place(relx=0.5,
                             rely=0.5,
                             anchor="center")

        self.buttonHertz = CustomButton(master=self.mainFrame_bottomFrame,
                                        custom_bg=self.color_manager.blue,
                                        text="440 Hz",
                                        hover=False)

        self.buttonHertz.place(anchor="sw",
                               relx=0.05,
                               rely=0.9,
                               height=61,
                               width=144)

        self.buttonInfo = CustomButton(master=self.mainFrame_bottomFrame,
                                       custom_bg=self.color_manager.blue,
                                       text="Info",
                                       function=self.master.draw_settings_frame)
        self.buttonInfo.place(anchor="se",
                              relx=0.95,
                              rely=0.9,
                              height=61,
                              width=144)

        self.mute_button = CustomButton(master=self,
                                        custom_bg=self.color_manager.gray,
                                        imageset=[self.image_manager.bell_image,
                                                  self.image_manager.bell_hovered_image,
                                                  self.image_manager.bell_muted_image,
                                                  self.image_manager.bell_muted_hovered_image])
        self.mute_button.place(anchor="ne",
                               relx=0.95,
                               rely=0.05,
                               height=self.image_manager.bell_image.height(),
                               width=self.image_manager.bell_image.width())

    def set_needle_angle(self, deg):
        x = sin(radians(180 - deg))
        y = sin(radians(270 - deg))

        self.underCanvas.coords(self.needle,
                                CANVAS_SIZE * 0.5,
                                CANVAS_SIZE * 0.5,
                                CANVAS_SIZE * 0.5 + (CANVAS_SIZE * 0.45 * x),
                                CANVAS_SIZE * 0.5 + (CANVAS_SIZE * 0.45 * y))
        return x, y

