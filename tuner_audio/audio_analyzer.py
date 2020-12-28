from pyaudio import PyAudio, paInt16
from threading import Thread
import numpy as np
import sys

from tuner_settings.audio_settings import *


class AudioAnalyzer(object):
    def __init__(self, queue):
        self.buffer = np.zeros(CHUNKSIZE * BUFFERTIMES)
        self.running = False

        try:
            self.audio_object = PyAudio()
            self.stream = self.audio_object.open(format=paInt16,
                                                 channels=1,
                                                 rate=RATE,
                                                 input=True,
                                                 frames_per_buffer=CHUNKSIZE)
        except Exception as e:
            print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
            return

        self.analyze_thread = Thread(target=self.analyzing_thread_function,
                                     args=[queue])

    def start(self):
        self.running = True
        self.analyze_thread.start()

    @staticmethod
    def freq_to_number(f, a4_freq):
        if f == 0:
            print("""Frequency is 0. Most likely your program has no acces to the microphone.
                     Try to start the program from the command prompt, or give your ide acces to the mic.""")
            return 0
        return 12 * np.log2(f / a4_freq) + 69

    @staticmethod
    def number_to_freq(n, a4_freq):
        return a4_freq * 2.0**((n - 69) / 12.0)

    @staticmethod
    def note_name(n):
        return NOTE_NAMES[int(round(n) % 12)]

    def analyzing_thread_function(self, queue):
        """Main function where the microphone buffer gets read and
           the fourier transformation gets applied"""

        while self.running:
            try:
                data = self.stream.read(CHUNKSIZE, exception_on_overflow=False)
                data = np.frombuffer(data, dtype=np.int16)

                self.buffer[:-CHUNKSIZE] = self.buffer[CHUNKSIZE:]
                self.buffer[-CHUNKSIZE:] = data

                numpydata = abs(np.fft.fft(self.buffer))
                numpydata = numpydata[:int(len(numpydata) / 2)]

                freqs = np.fft.fftfreq(len(numpydata), 1. / RATE)

                queue.put(round(freqs[np.argmax(numpydata)], 2))

            except Exception as e:
                print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)

        self.stream.stop_stream()
        self.stream.close()
        self.audio_object.terminate()
