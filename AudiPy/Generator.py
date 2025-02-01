import numpy as np

class Generator:
    def __init__(self):
        return

    def __call__(self):
        return

    def data_matrix(self, array, time):
        SAMPLE_RATE = 44100 
        # calculate sample steps
        ns = np.linspace(0., time, SAMPLE_RATE * time)
        amplitude = np.iinfo(np.int16).max

        # samples per pitch
        sample_size = int(len(ns)/len(array[0]))

        #Nyquist Theorem
        for channel in array:
            if SAMPLE_RATE <= max(channel) * 2:
                print("Nyquist Theorem is failed!")
                quit

        converted_music = []

        for channel in array:
            previous_samples = 0
            print("New channel!")
            new_channel = []

            for freq in channel:
                cur_samples = ns[previous_samples:(previous_samples + sample_size)]
                previous_samples += sample_size
                sine_wave = (amplitude * np.sin(2. * np.pi * freq * cur_samples))
                new_channel.append(sine_wave)

            new_channel = np.concatenate(new_channel)
            print(new_channel)
            converted_music.append(new_channel)

        # each row is a channel
        converted_music = np.vstack(converted_music)

        return converted_music
    
    def rgb_matrix(self, matrix):
        return