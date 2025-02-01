from scipy.io.wavfile import write
import numpy as np

class StandardScalar:
    def __init__(self):
        return

    def __call__(self):
        return
    
    # normalize data between the range of min to max with a sine curve
    def normalize_sine(self, data, minf, maxf):
        return ((maxf-minf) * np.abs(np.sin(data)) + minf)

    # normalize data between the range of min to max with a inverse function
    def normalize_inverse(self, data, minf, maxf):
        return ((maxf-minf) * data/max(data) + minf)

    # normalize to twelve tone
    def normalize_twelve_tone(self, data, minf=None, maxf=None):
        return np.multiply(63, np.power(2,np.divide(data,12)))

    # normalize by scaled
    def normalize_scaled(self, data, minf, maxf):
        return np.subtract(data,np.min(data)) / np.subtract(np.max(data),np.min(data)) * ((maxf-minf)) + minf
