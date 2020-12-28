from threading import Thread
from playsound import playsound
import time


class SoundThread(Thread):
    def __init__(self, path_to_file, global_manager, mute_button):
        Thread.__init__(self)
        self.running = False
        self.file = path_to_file
        self.global_manager = global_manager
        self.mute_button = mute_button

    def run(self):
        self.running = True
        while self.running:

            if self.global_manager.play_sound is True and not self.mute_button.pressed:
                playsound(self.file)
                time.sleep(1)
                self.global_manager.play_sound = False
            else:
                time.sleep(0.1)
