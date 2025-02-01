from scipy.io.wavfile import write
import numpy as np

# normalize data between the range of min to max with a sine curve
def normalize_sine(min, max, data):
    return ((max-min) * np.abs(np.sin(data)) + min)

# normalize data between the range of min to max with a inverse function
def normalize_inverse(min, max, data):
    return ((max-min) * data/max(data) + min)

# normalize to twelve tone
def normalize_twelve_tone(data):
    return np.multiply(63, np.power(2,np.divide(data,12)))

# normalize by scaled
def normalize_scaled(min, max, data):
    return np.subtract(data,np.min(data)) / np.subtract(np.max(data),np.min(data)) * ((max-min)) + min

def play(length, data, data2):
    # total time of the track
    t = length

    # Frequencies to play
    Freq = data
    Freq2 = data2

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

test = np.linspace(1, 50, 50)
test2 = np.linspace(50, 1, 50)
test = normalize_twelve_tone(test)
test2 = normalize_twelve_tone(test2)

play(10, test, test2)
