from threading import Lock


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


class GlobalManager(object):
    def __init__(self):
        self.a4_freq = 440
        self.play_sound = False

    def frequencyUp(self):
        self.a4_freq += 1

    def frequencyDown(self):
        self.a4_freq -= 1

