from functiondistrogenerator import FunctionDistroGenerator
from matplotlib import pyplot as plt
import time



function = 'sin(x)'
decimalplaces = 0
xrange = [1, 4]
binwidth = 1

starttime = time.clock()

gen = FunctionDistroGenerator(function, decimalplaces, xrange)

preprocessingtime = time.clock()

print('Preprocesseing time: '+str(preprocessingtime-starttime))

data = []

for i in range(1):
    data.append(gen.generate())

postgeneratetime = time.clock()

print('Generate 1 million times: '+str(postgeneratetime - preprocessingtime))

print(' ')

print('Sample Data')
print(data[0:10])

plt.hist(data)
#plt.show()
