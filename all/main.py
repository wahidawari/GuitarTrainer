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

from settings import Settings


class App(tkinter.Tk):
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

        self.title(Settings.APP_NAME)
        self.geometry(str(Settings.WIDTH) + "x" + str(Settings.HEIGHT))
        self.resizable(True, True)
        self.minsize(Settings.WIDTH, Settings.HEIGHT)
        self.maxsize(Settings.MAX_WIDTH, Settings.MAX_HEIGHT)
        self.configure(background=self.color_manager.background_layer_1)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        if sys.platform == "darwin":  # MacOS X and MacOS 11
            self.bind("<Command-q>", self.on_closing)
            self.bind("<Command-w>", self.on_closing)
            self.createcommand('tk::mac::Quit', self.on_closing)

            menu_bar = tkinter.Menu(master=self)
            app_menu = tkinter.Menu(menu_bar, name='apple')
            menu_bar.add_cascade(menu=app_menu)

            app_menu.add_command(label='About ' + Settings.APP_NAME, command=self.about_dialog)
            app_menu.add_separator()

            self.config(menu=menu_bar)

        elif "win" in sys.platform:  # Windows
            self.bind("<Alt-Key-F4>", self.on_closing)

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


if __name__ == "__main__":
    app = App()
    app.start()
