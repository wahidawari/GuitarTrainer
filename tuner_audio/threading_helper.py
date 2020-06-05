import time

from playsound import playsound
from threading import Thread, Lock


class ProtectedList(object):
    def __init__(self):
        self.elements = []
        self.lock = self.lock = Lock()

    def put(self, element):
        self.lock.acquire()
        self.elements.append(element)
        self.lock.release()

    def get(self):
        self.lock.acquire()
        if len(self.elements) > 0:
            element = self.elements[0]
            del self.elements[0]
        else:
            element = None
        self.lock.release()
        return element

    def __repr__(self):
        self.lock.acquire()
        string = str(self.elements)
        self.lock.release()
        return string


class Runner(object):
    def __init__(self):
        self.running = True


class GlobalManager(object):
    def __init__(self):
        self.a4_freq = 440
        self.playSound = False

    def frequencyUp(self):
        self.a4_freq += 1

    def frequencyDown(self):
        self.a4_freq -= 1


class SoundThread(Thread):
    def __init__(self, runner, file, global_manager, buttonBell):
        Thread.__init__(self)
        self.runner = runner
        self.file = file
        self.global_manager = global_manager
        self.buttonBell = buttonBell

    def run(self):
        while self.runner.running:

            if self.global_manager.playSound is True and not self.buttonBell.pressed:
                playsound(self.file)
                time.sleep(1)
                self.global_manager.playSound = False
            else:
                time.sleep(0.1)
