import tkinter as tk                # python 3
from tkinter import font as tkfont  # python 3
from PIL import ImageTk, Image
import numpy as np
import pyaudio
import os


#from tuner
import tkinter
import tkinter.messagebox
import os
import sys
import numpy as np

from tuner_audio.audio_analyzer import AudioAnalyzer
from tuner_audio.threading_helper import ProtectedList
from tuner_audio.sound_thread import SoundThread

from tuner_appearance_manager.color_manager import ColorManager
from tuner_appearance_manager.image_manager import ImageManager
from tuner_appearance_manager.timing import Timer

from tuner_ui_parts.main_frame import MainFrame
from tuner_ui_parts.settings_frame import SettingsFrame
# from tuner above 

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)




        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, PageFive, TunerPage):
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

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the start page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Learn Chords",
                            command=lambda: controller.show_frame("PageOne"))
        button1.pack()

        button2 = tk.Button(self, text="Tune Your Guitar",
                            command=lambda: controller.show_frame("TunerPage"))
        button2.pack()
        


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        ##### ADD IMAGE TO SCREEN ####
        render = ImageTk.PhotoImage(Image.open('e-chord.png'))
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
        render = ImageTk.PhotoImage(Image.open('eminor.png'))
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
        render = ImageTk.PhotoImage(Image.open('d.png'))
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
        render = ImageTk.PhotoImage(Image.open('c.png'))
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
        render = ImageTk.PhotoImage(Image.open('a.png'))
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

#this is the tuner page

class TunerPage(tk.Frame):

    def __init__(self, *args, **kwargs):
        # os.system("defaults write -g NSRequiresAquaSystemAppearance -bool No")  # only for dark-mode testing
        tkinter.Tk.__init__(self, *args, **kwargs)

        self.main_path = os.path.dirname(os.path.abspath(__file__))

        self.color_manager = ColorManager()
        self.image_manager = ImageManager(self.main_path)

        self.main_frame = MainFrame(self)
        self.settings_frame = SettingsFrame(self)
        
        self.frequency_queue = ProtectedList()
        self.audio_analyzer = AudioAnalyzer(self.frequency_queue)
        self.audio_analyzer.start()

        self.play_sound_thread = SoundThread(self.main_path + "/assets/sounds/drop.wav")
        self.play_sound_thread.start()

        self.needle_buffer_array = np.zeros(5)
        self.tone_hit_counter = 0
        self.a4_frequency = 440

        self.dark_mode_active = False

        
        
      

      

        
        self.timer = Timer(Settings.FPS)

        self.draw_main_frame()

    @staticmethod
    def about_dialog():
        tkinter.messagebox.showinfo(title=Settings.APP_NAME,
                                    message=Settings.ABOUT_TEXT)

    def draw_settings_frame(self, event=0):
        self.main_frame.place_forget()
        self.settings_frame.place(relx=0, rely=0, relheight=1, relwidth=1)

    def draw_main_frame(self, event=0):
        self.settings_frame.place_forget()
        self.main_frame.place(relx=0, rely=0, relheight=1, relwidth=1)

    def on_closing(self, event=0):
        # os.system("defaults delete -g NSRequiresAquaSystemAppearance")  # only dark-mode for testing
        self.audio_analyzer.running = False
        self.play_sound_thread.running = False
        self.destroy()

    def update_color(self):
        self.main_frame.update_color()
        self.settings_frame.update_color()

    def start(self):
        while self.audio_analyzer.running:

            try:
                dark_mode_state = self.color_manager.detect_os_dark_mode()
                if dark_mode_state is not self.dark_mode_active:
                    if dark_mode_state is True:
                        self.color_manager.set_mode("Dark")
                    else:
                        self.color_manager.set_mode("Light")

                    self.dark_mode_active = dark_mode_state
                    self.update_color()

                freq = self.frequency_queue.get()
                if freq is not None:

                    number = self.audio_analyzer.freq_to_number(freq, self.a4_frequency)
                    note = self.audio_analyzer.note_name(number)
                    difference = self.audio_analyzer.number_to_freq(round(number), self.a4_frequency) - freq
                    difference_next_note = self.audio_analyzer.number_to_freq(round(number), self.a4_frequency) -\
                                           self.audio_analyzer.number_to_freq(round(number - 1), self.a4_frequency)

                    needle_angle = -90 * ((difference / difference_next_note) * 2)

                    if abs(needle_angle) < 5:
                        self.main_frame.set_needle_color("green")
                        self.tone_hit_counter += 1
                    else:
                        self.main_frame.set_needle_color("red")
                        self.tone_hit_counter = 0

                    if self.tone_hit_counter > 7:
                        self.tone_hit_counter = 0

                        if self.main_frame.button_mute.pressed is not True:
                            self.play_sound_thread.play_sound()

                    self.needle_buffer_array[:-1] = self.needle_buffer_array[1:]
                    self.needle_buffer_array[-1:] = needle_angle

                    self.main_frame.set_needle_angle(np.average(self.needle_buffer_array))

                    self.main_frame.note_label.configure(text=note)

                    self.main_frame.button_frequency.set_text(str(round(-difference, 1)) + " Hz")

                self.update()
                self.timer.wait()

            except Exception as err:
                sys.stderr.write('Error: Line {} {} {}\n'.format(sys.exc_info()[-1].tb_lineno, type(err).__name__, err))
                self.timer.wait()



     
        
        button = tk.Button(self, text="go home",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

            
        

       


if __name__ == "__main__":
    app = SampleApp()
    # Sets the size of the window
    app.geometry("1500x900")
    app.mainloop()