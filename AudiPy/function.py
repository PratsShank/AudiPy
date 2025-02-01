from scipy.io.wavfile import write
import numpy as np

# normalize data between the range of min to max with a sine curve
def normalize_sine(min, max, data):
    return ((max-min) * np.abs(np.sin(data)) + min)

# normalize data between the range of min to max with a inverse function
def normalize_inverse(min, max, data):
    return ((max-min) * data/max(data) + min)

def play(length, data):
    # total time of the track
    t = length

    # Frequencies to play
    Freq = data

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

    write("example.wav", SAMPLE_RATE, data.astype(np.int16))

test = np.linspace(0, 50, 50)
test = normalize_inverse(test)
print(test)
play(10, test)
