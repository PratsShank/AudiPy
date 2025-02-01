from scipy.io.wavfile import write
import numpy as np

class Standard:
    def __init__(self, minf, maxf):
        self.minf = minf
        self.maxf = maxf
        self.data = 0
        self.data2 = 0
        self.time = 0 
    
    # normalize data between the range of min to max with a sine curve
    def normalize_sine(self):
        return ((self.maxf-self.minf) * np.abs(np.sin(self.data)) + self.minf)

    # normalize data between the range of min to max with a inverse function
    def normalize_inverse(self):
        return ((self.maxf-self.minf) * self.data/max(self.data) + self.minf)

    # normalize to twelve tone
    def normalize_twelve_tone(data):
        return np.multiply(63, np.power(2,np.divide(data,12)))

    # normalize by scaled
    def normalize_scaled(self):
        return np.subtract(self.data,np.min(self.data)) / np.subtract(np.max(self.data),np.min(self.data)) * ((self.maxf-self.minf)) + self.minf

    def write(self, time, Data, Data2):
        # total time of the track
        self.time = time
        self.data = Data
        self.data2 = Data2
        t =  self.time

        # Frequencies to play
        Freq = Data
        Freq2 = Data2

        # sample rate
        SAMPLE_RATE = 44100

        # calculate sample steps
        ns = np.linspace(0., t, SAMPLE_RATE * t)
        amplitude = np.iinfo(np.int16).max

        # samples per pitch
        sample_size= int(len(ns)/len(Freq))

        #Nyquist Theorem
        if sample_size <= max(Freq) * 2:
            print("Nyquist Theorem is failed!")
            quit

        previous_samples = 0
        data = np.ndarray(0)
        for freq in Freq:
            cur_samples = ns[previous_samples:(previous_samples+sample_size)]
            previous_samples += sample_size
            data = np.append(data, amplitude * np.sin(2. * np.pi * freq * cur_samples))

        previous_samples = 0
        data_interval = np.ndarray(0)
        for freq in Freq2:
            cur_samples = ns[previous_samples:(previous_samples+sample_size)]
            previous_samples += sample_size
            data_interval = np.append(data_interval, amplitude * np.sin(2. * np.pi * (freq) * cur_samples))

        data = np.column_stack((data, data_interval))
        print(data)
        write("example.wav", SAMPLE_RATE, data.astype(np.float32))
