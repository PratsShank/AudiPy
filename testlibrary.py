from AudiPy import standclass as stc
import numpy as np

#print("here")

line = stc.Standard(minf=20, maxf=4000)


# test = np.linspace(220.5, 220.5, 50)
# test2 = np.linspace(138.5, 138.5, 50)
# test3 = np.linspace(164.5, 164.5, 50)
# test4 = np.linspace(10.5, 10.5, 50)
# test5 = np.linspace(40.5, 40.5, 50)
# test6 = np.linspace(50.5, 50.5, 50)

test = np.linspace(1, 50, 50)
test2 = np.linspace(50, 1, 50)
#test3 = np.linspace(164.5, 164.6, 50)

test = line.normalize_twelve_tone(test)
test2 = line.normalize_twelve_tone(test2)
# test3 = line.normalize_twelve_tone(test3)
# test4 = line.normalize_twelve_tone(test4)
# test5 = line.normalize_twelve_tone(test5)
# test6 = line.normalize_twelve_tone(test6)
#  test4, test5, test6
test4 = np.array([test, test2], dtype=object)

t = 10

 # sample rate
SAMPLE_RATE = 44100 
# calculate sample steps
ns = np.linspace(0., t, SAMPLE_RATE * t)
amplitude = np.iinfo(np.int16).max

# samples per pitch
sample_size = int(len(ns)/len(test4[0]))

#Nyquist Theorem
for channel in test4:
    if sample_size <= max(channel) * 2:
        print("Nyquist Theorem is failed!")
        quit

converted_music = []

for channel in test4:
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

print(converted_music)

line.write(time=10, Data=converted_music)