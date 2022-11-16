from scipy.io.wavfile import read
from os.path import dirname, join as pjoin
import scipy.io


samplerate, data = read(r'Fourier_series_GUI\backend\api_fourier\FourierLogic\audio_test_files\Jairo and Diego on the rocks.wav')
print(f"number of channels = {data.shape[1]}")

length = data.shape[0] / samplerate
print(f"length = {length}s")

import matplotlib.pyplot as plt
import numpy as np
import time


stime = np.linspace(0., length, data.shape[0])
plt.plot(stime, data[:, 0], label="Left channel")
plt.plot(stime, data[:, 1], label="Right channel")
plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()

import sounddevice as sd
sps = 48000 
#Este son los hz adec

sd.play(data[:, 0],sps)
time.sleep(10)
sd.stop()
print("final")



#### This section will cover the lowpass filters

from scipy.signal import butter, lfilter, freqz


def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y