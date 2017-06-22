#from mythos.domain.generators.generator import Generator
import random

'''
An implementation of the alias method using Vose's algorithm. The alias method samples random values from a discrete
probability distribution in O(1) time after O(n) preprocessing time.
'''


class DiscreteDistributionGenerator:

    # preprocessing
    def __init__(self, probabilities, xvalues=[]):

        # number of items
        self.numvalues = len(probabilities)

        self.alias = {}
        self.probabilities = dict(zip(range(self.numvalues), probabilities))
        self.values = xvalues

        # if no xvalues were given (or the wrong number), we will return integers from 0 to len(probabilities)-1
        if not len(self.values) == self.numvalues:
            self.values = range(self.numvalues)

        # small and large lists of the numbered element for each probability
        small = []
        large = []

        # populate small and large
        for i in range(self.numvalues):

            self.probabilities[i] *= self.numvalues

            if self.probabilities[i] < 1:
                small.append(i)
            else:
                large.append(i)

        '''
        /* As a note: in the mathematical specification of the algorithm, we
         * will always exhaust the small list before the big list.  However,
         * due to floating point inaccuracies, this is not necessarily true.
         * Consequently, this inner loop (which tries to pair small and large
         * elements) will have to check that both lists aren't empty.
         */
         '''
        while len(small) > 0 and len(large) > 0:
            less = small.pop()
            more = large.pop()

            # Populate the alias dict with the column name that will be the alias
            self.alias[less] = more

            # adjust the larger probability to account for turning part of it into the alias
            self.probabilities[more] += self.probabilities[less] - 1

            # if the remaining probability for 'more' is larger than 1, return it to large, else small
            if self.probabilities[more] < 1:
                small.append(more)
            else:
                large.append(more)

            '''
            At this point, everything is in one list, which means that the
            remaining probabilities should all be 1.  Based on this, set them
            appropriately.  Due to numerical issues, we can't be sure which
            stack will hold the entries, so we empty both.
            '''

        while len(small) > 0:
            self.probabilities[small.pop()] = 1.0
        while len(large) > 0:
            self.probabilities[large.pop()] = 1.0

    def generate(self):
        # randomly select the column we will be pulling either the original or the alias from
        column = random.randint(0, self.numvalues - 1)

        # flip an unfair coin for the two options in that column, either returning the column value or the alias value
        coinToss = random.random() < self.probabilities[column]

        if coinToss:
            return self.values[column]
        else:
            return self.values[self.alias[column]]
