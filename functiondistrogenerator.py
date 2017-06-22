from functionbucketmaker import functionbucketmaker
from discretedistrogenerator import DiscreteDistributionGenerator


class FunctionDistroGenerator:

    def __init__(self, func, decimalplaces=2, minmax=[0, 1]):

        self.func = func
        self.decimalplaces = decimalplaces
        self.minmax = minmax

        bucket = functionbucketmaker(self.func, self.decimalplaces, self.minmax)

        self.discretedistrogenerator = DiscreteDistributionGenerator(bucket[1], bucket[0])

    def generate(self):

        return self.discretedistrogenerator.generate()
