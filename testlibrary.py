import numpy as np
import AudiPy

#print("here")

Audi = AudiPy()

# line = StandardScalar(minf=20, maxf=4000)

test = np.linspace(1, 50, 50)
test2 = np.linspace(50, 1, 50)

test4 = np.array([test, test2], dtype=object)

# print(test4)

t = 15
preprocess = Audi.pre_process(filename="C:\\Users\\Cayden\\Downloads\\Save_webP\\ZigZag.png")
final = Audi.convert_to_audio(data=preprocess, min_freq=20, max_freq=4000,  time=t)

# test = line.normalize_twelve_tone(test)
# test2 = line.normalize_twelve_tone(test2)







 # sample rate

# Gen = Generator()

# Matrix = Gen.data_matrix(array=test4, time=t)

# Out = Output()

# Out.write(Data=Matrix)

# print(converted_music)

# line.write(Data=Matrix)