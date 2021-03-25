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

from chords_frame import ChordsFrame
from settings_frame import SettingsFrame

from settings import Settings

    

    

    
 






class App(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        # os.system("defaults write -g NSRequiresAquaSystemAppearance -bool No")  # only for dark-mode testing
        tkinter.Tk.__init__(self, *args, **kwargs)

        self.main_path = os.path.dirname(os.path.abspath(__file__))

        self.color_manager = ColorManager()
        self.image_manager = ImageManager(self.main_path)

        self.trainer_frame = TrainerFrame(self)
        self.chords_frame = ChordsFrame(self)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def draw_chords_frame(self, event=0):
        self.chords_frame.place(relx=0, rely=0, relheight=1, relwidth=1)   

#everything above is just the skeleton
#below is the real code 




    def start(self):
        while self.chords_frame.running:

            try:
                dark_mode_state = self.color_manager.detect_os_dark_mode()
                if dark_mode_state is not self.dark_mode_active:
                    if dark_mode_state is True:
                        self.color_manager.set_mode("Dark")
                    else:
                        self.color_manager.set_mode("Light")

                    self.dark_mode_active = dark_mode_state
                    self.update_color()


if __name__ == "__main__":
    app = App()
    app.geometry("1500x900")
    app.start()