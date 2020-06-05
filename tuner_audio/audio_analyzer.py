from pyaudio import PyAudio, paInt16
import numpy as np

from tuner_settings.audio_settings import *


def freq_to_number(f, a4_freq):
    if f == 0:
        print("Frequency is 0. Most likely your program has no acces to the microphone. Try to start the program from the command prompt, or give your ide acces to the mic.")
        return 0
    return 12 * np.log2(f / a4_freq) + 69


def number_to_freq(n, a4_freq):
    return a4_freq * 2.0**((n - 69) / 12.0)


def note_name(n):
    return NOTE_NAMES[int(round(n) % 12)]


def analyzing_function(runner, protectedList):
    try:
        p = PyAudio()
        stream = p.open(format=paInt16, channels=1, rate=RATE, input=True, frames_per_buffer=CHUNKSIZE)
    except Exception as e:
        print(e)
        return

    # window = 0.5 * (1 - np.cos(np.linspace(0, 2 * np.pi, CHUNKSIZE * BUFFERTIMES, False))) # hanning-window (optional)

    buffer = np.zeros(CHUNKSIZE * BUFFERTIMES)

    while runner.running:
        try:
            data = stream.read(CHUNKSIZE, exception_on_overflow=False)

            data = np.frombuffer(data, dtype=np.int16)

            buffer[:-CHUNKSIZE] = buffer[CHUNKSIZE:]
            buffer[-CHUNKSIZE:] = data

            numpydata = abs(np.fft.fft(buffer))

            freqs = np.fft.fftfreq(len(numpydata), 1. / RATE)

            numpydata = numpydata[:int(len(numpydata) / 2)]
            freqs = freqs[:int(len(freqs) / 2)]

            protectedList.put(round(freqs[np.argmax(numpydata)], 2))
        except:
            print("missed samples")
            pass

    stream.stop_stream()
    stream.close()
    p.terminate()
    print("Audio Stream stopped")
