from AudiPy import standclass as stc
import numpy as np

#print("here")

line = stc.Standard(minf=20, maxf=4000)


test = np.linspace(20, 1000, 50)
test2 = np.linspace(1000, 20, 50)
line.write(time=10, Data=test, Data2=test2)
test = line.normalize_twelve_tone(test)
test2 = line.normalize_twelve_tone(test2)




#print(data)
