import Input
import StandardScalar
import Generator
import Output

class AudiPy():

    def __init__(self):
        self.scalar = StandardScalar()
        self.generator = Generator()
        self.output = Output()
        return

    def pre_process(self, filename):
        matrix = Input(filename)
        return matrix
    
    def convert_to_audio(self, data, min_freq, max_freq, sound, ascending, time):
        matrix = self.scalar.normalize_twelve_tone(data, min_freq, max_freq)
        wave = self.generator.data_matrix(matrix, time)
        return self.output.write(wave)
