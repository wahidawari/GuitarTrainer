import tkinter
import tkinter.messagebox
import os
import sys

from numpy import zeros, average
from threading import Thread
import time

from tuner_audio.audio_analyzer import analyzing_function, freq_to_number, number_to_freq, note_name
from tuner_audio.threading_helper import ProtectedList, Runner, GlobalManager, SoundThread

from tuner_appearance.color_manager import ColorManager
from tuner_appearance.image_manager import ImageManager
from tuner_appearance.tuner_ui_parts.main_frame import MainFrame
from tuner_appearance.tuner_ui_parts.settings_frame import SettingsFrame

from tuner_settings.global_settings import *

MAIN_PATH = os.path.dirname(__file__)


class App(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)

        self.color_manager = ColorManager()
        self.image_manager = ImageManager(MAIN_PATH)
        self.runner = Runner()
        self.global_manager = GlobalManager()
        self.queue = ProtectedList()

        self.main_frame = MainFrame(self)
        self.settings_frame = SettingsFrame(self)

        self.analyzeThread = Thread(target=analyzing_function,
                                    args=[self.runner, self.queue])
        self.analyzeThread.start()

        self.playSoundThread = SoundThread(self.runner,
                                           MAIN_PATH + "/assets/sounds/drop.wav",
                                           self.global_manager,
                                           self.main_frame.buttonBell)
        self.playSoundThread.start()

        self.needleBuffer = zeros(5)
        self.hitCounter = 0

        self.minsize(WIDTH, HEIGHT)
        self.resizable(True, True)
        self.title(APP_NAME)
        self.geometry(str(WIDTH) + "x" + str(HEIGHT))
        self.configure(background=self.color_manager.gray)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.bind("<Command-q>", self.on_closing)
        self.bind("<Command-w>", self.on_closing)

        menubar = tkinter.Menu(master=self)
        app_menu = tkinter.Menu(menubar, name='apple')
        menubar.add_cascade(menu=app_menu)

        app_menu.add_command(label='About ' + APP_NAME, command=self.about_dialog)
        app_menu.add_separator()

        self.createcommand('tk::mac::Quit', self.on_closing)
        self.config(menu=menubar)

        self.draw_main_frame()

    def about_dialog(self):
        tkinter.messagebox.showinfo(title=APP_NAME,
                                    message=ABOUT_TEXT)

    def draw_settings_frame(self, event=0):
        self.main_frame.place_forget()
        self.settings_frame.place(relx=0, rely=0, relheight=1, relwidth=1)

    def draw_main_frame(self, event=0):
        self.settings_frame.place_forget()
        self.main_frame.place(relx=0, rely=0, relheight=1, relwidth=1)

    def on_closing(self, event=0):
        self.runner.running = False
        self.destroy()
        exit()

    def start(self):
        while True:
            if self.runner.running:
                try:
                    freq = self.queue.get()
                    if freq != None:

                        number = freq_to_number(freq, self.global_manager.a4_freq)
                        note = note_name(number)
                        difference = number_to_freq(round(number), self.global_manager.a4_freq) - freq
                        differenceNextNote = number_to_freq(round(number), self.global_manager.a4_freq) - \
                                             number_to_freq(round(number - 1), self.global_manager.a4_freq)

                        needleAngle = -90 * (difference / differenceNextNote * 2)

                        if abs(needleAngle) < 5:
                            self.main_frame.underCanvas.itemconfig(self.main_frame.needle, fill=self.color_manager.green)
                            self.hitCounter += 1
                        else:
                            self.main_frame.underCanvas.itemconfig(self.main_frame.needle, fill=self.color_manager.red)
                            self.hitCounter = 0

                        if self.hitCounter > 7:
                            self.hitCounter = 0
                            self.global_manager.playSound = True

                        self.needleBuffer[:-1] = self.needleBuffer[1:]
                        self.needleBuffer[-1:] = needleAngle

                        self.main_frame.set_needle_angle(average(self.needleBuffer))

                        self.main_frame.noteLabel.configure(text=note)
                        self.main_frame.buttonHertz.label.configure(text=str(round(-difference, 1)) + " Hz")

                    self.update()
                except Exception as e:
                    print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
                    time.sleep(1 / FPS)
            else:
                print("-- program ended --")
                break


if __name__ == "__main__":
    app = App()
    app.start()
