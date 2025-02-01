## AudiPy Group 

This will be a Python library, 
that will read in some input and output some audio format version of that input. 
The idea is to specify audio min and max frequencies, 
and then decide how the data is connected to the frequency. 
For instance, do you want the larger data to be higher pitched or lower pitched?

### Functions: 
1. Standard
2. Images
3. Linear Error

### Standard Parameters 
1. Data -ID np.array
2. min_freq -int(0 < n < max)
3. max_freq - int(min < n < 22K)
4. Mode, -String("major", "")
5. Key = "C", -String("A", "A#")
6. Sound
7. Time
8. Ascending
9. Comparison
10. Normalization

### Image Parameters
1. min
2. max
3. mode
4. key
5. data
6. RGB
7. sound
8. time

### Linear Error
1. Data -ID np.array
2. min_freq -int(0 < n < max)
3. max_freq - int(min < n < 22K)
4. Mode, -String("major", "")
5. Key = "C", -String("A", "A#")
6. Sound
