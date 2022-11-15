from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import numpy as np
from os.path import join 
import time

dummie_path = (r'Fourier_series_GUI\backend\api_fourier\FourierLogic\audio_test_files\Jairo and Diego on the rocks.wav')

class audio:
    def __init__(self,path) -> None:
        self.path = path
        pass 
        
    def audio_wave_serie(self):
        samplerate, data = read(self.path)
        length = data.shape[0] / samplerate
        stime = np.linspace(0., length, data.shape[0])
        plt.plot(stime, data[:, 0], label="Left channel")
        plt.plot(stime, data[:, 1], label="Right channel")
        plt.legend()
        plt.xlabel("Time [s]")
        plt.ylabel("Amplitude")
        plt.show()

a = audio(path=dummie_path)
a.audio_wave_serie()


