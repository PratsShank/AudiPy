from scipy.io.wavfile import write
import numpy as np

class Output:
    def __init__(self):
        return
    
    def __call__(self):
        return
    
    def write(self, Data):
        # total time of the track
        self.data = Data

        # print("Data", Data)

        # sample rate
        SAMPLE_RATE = 44100                

        # print("Transposed", Data.T)
        Transposed = Data.T
        # data = np.ndarray(0)

        write("example.wav", SAMPLE_RATE, Transposed.astype(np.float32))