#from mythos.domain.generators.generator import Generator
import numpy as np

#class NormalDistroGenerator(Generator):
class NormalDistroGenerator:


    def __init__(self, column_name, stddev, mean):

        self.column_name = column_name
        self.stddev = stddev
        self.mean = mean

        self.var = self.stddev**0.5

    def generate_values(self, generator_options=None):

        value = self.var * np.random.randn()+self.mean
        #return {self.column_name: value}
        return value