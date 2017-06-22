from functiondistrogenerator import FunctionDistroGenerator
from matplotlib import pyplot as plt

function = 'sin(x)'
decimalplaces = 2
xrange = [0, 8]
binwidth = 1

gen = FunctionDistroGenerator(function, decimalplaces, xrange)

data = []

for i in range(1000):
    data.append(gen.generate())

print(data[0:10])

plt.hist(data)
plt.show()

