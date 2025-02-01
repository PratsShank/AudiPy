from AudiPy import StandardScalar as stc
import AudiPy
import numpy as np
from AudiPy import Generator
from AudiPy import StandardScalar
from AudiPy.Output import Output

import AudiPy

#print("here")

Audi = AudiPy()

line = StandardScalar(minf=20, maxf=4000)


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

Gen = Generator()

Matrix = Gen.data_matrix(array=test4, time=t)

Out = Output()

Out.write(Data=Matrix)

# print(converted_music)

# line.write(Data=Matrix)