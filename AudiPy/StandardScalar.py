from scipy.io.wavfile import write
import numpy as np

class StandardScalar:
    def __init__(self, minf, maxf):
        self.minf = minf
        self.maxf = maxf

    def __call__(self):
        return
    
    # normalize data between the range of min to max with a sine curve
    def normalize_sine(self):
        return ((self.maxf-self.minf) * np.abs(np.sin(self.data)) + self.minf)

    # normalize data between the range of min to max with a inverse function
    def normalize_inverse(self):
        return ((self.maxf-self.minf) * self.data/max(self.data) + self.minf)

    # normalize to twelve tone
    def normalize_twelve_tone(self, data):
        return np.multiply(63, np.power(2,np.divide(data,12)))

    # normalize by scaled
    def normalize_scaled(self):
        return np.subtract(self.data,np.min(self.data)) / np.subtract(np.max(self.data),np.min(self.data)) * ((self.maxf-self.minf)) + self.minf