# import normaldistrogenerator
# from matplotlib import pyplot as plt
import math
#
# gen = normaldistrogenerator.NormalDistroGenerator('number',25,50)
#
# data = []
#
# for i in range(100):
#     data.append(gen.generate_values())
#
# plt.hist(data)
# plt.show()
# from functiondistrogenerator import FunctionDistroGenerator
# from matplotlib import pyplot as plt
#
# gen = FunctionDistroGenerator('sin(x)', 2, [0,8])
# xvalues=[]
# for i in range(100):
#     xvalues.append(gen.generate())
#
# plt.hist(xvalues)
# plt.show()

print(eval('math.floor(11.1243)'))


#
#
# from discretedistrogenerator import DiscreteDistributionGenerator
#
# gen = DiscreteDistributionGenerator([.3, 0, .3, .3, .1],['a','b','c'])
#
# for i in range(100):
#     print(gen.generate())
# #
# gen = DiscreteDistributionGenerator([.3, 0, .7],['a','c'])
#
# for i in range(10):
#     print(gen.generate())
#
# gen = DiscreteDistributionGenerator([.3, 0, .7])
#
# for i in range(10):
#     print(gen.generate())

# __author__ = 'jjam13'
# #Found at http://www.keithschwarz.com/darts-dice-coins/
# import random,time
#
#
# '''
# An implementation of the alias method using Vose's algorithm. The alias method samples random values from a discrete
# probability distribution in O(1) time after O(n) preprocessing time.
# '''
#
# class AliasMethod:
#
#     #probability and alias dictionaries
#     alias = {}
#     probability = {}
#
#     #preprocessing
#     def aliasmethod(self, probabilities):
#
#         #number of items
#         n = len(probabilities)
#         #compute the average of the probabilities
#         average = 1.0/n
#
#         #small and large lists of the numbered element for each probability
#         small = []
#         large = []
#
#         #populate small and large
#         for i in range(n):
#             if probabilities[i]< average:
#                 small.append(i)
#             else:
#                 large.append(i)
#
#         '''
#         /* As a note: in the mathematical specification of the algorithm, we
#          * will always exhaust the small list before the big list.  However,
#          * due to floating point inaccuracies, this is not necessarily true.
#          * Consequently, this inner loop (which tries to pair small and large
#          * elements) will have to check that both lists aren't empty.
#          */
#          '''
#         while (len(small)>0 and len(large)>0):
#             less = small.pop()
#             more = large.pop()
#
#             #Populate the probability dict with the scaled small probability
#             #Populate the alias dict with the column name that will be the alias
#             self.probability[less]=probabilities[less] * n
#             self.alias[less]=more
#
#             #adjust the larger probability to account for turning part of it into the alias
#             probabilities[more]=probabilities[more]+probabilities[less]-average
#
#             #if the remaining probability for 'more' is larger than average, return it to large, else small
#             if probabilities[more]>average:
#                 large.append(more)
#             else:
#                 small.append(more)
#
#         '''
#                 /* At this point, everything is in one list, which means that the
#          * remaining probabilities should all be 1/n.  Based on this, set them
#          * appropriately.  Due to numerical issues, we can't be sure which
#          * stack will hold the entries, so we empty both.
#          */
#         '''
#         while len(small)>0:
#             self.probability[small.pop()]=1.0
#         while len(large)>0:
#             self.probability[large.pop()]=1.0
#
#
#     #this method is to acquire a rolling of the weighted die on an AliasMethod object
#     def next(self):
#         #randomly select the column we will be pulling either the original or the alias from
#         column = random.randint(0,len(self.probability)-1)
#
#         #flip an unfair coin for the two options in that column, either returning the column or the alias
#         coinToss = random.random()<self.probability[column]
#
#         if coinToss:
#             return column
#         else:
#             return self.alias[column]
#
# #test run
# start = time.clock()
# x=AliasMethod()
# x.aliasmethod([.3,.3,0,.4])
# distro = {0:0,1:0,2:0,3:0}
# num=6000000
#
# for i in range(num):
#     distro[x.next()]+=1.0
#
#
# for r in distro.keys():
#     distro[r]= distro[r]/num
# print(distro)
# print(time.clock()-start)
#
#
#
