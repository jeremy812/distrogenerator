import normaldistrogenerator
from matplotlib import pyplot as plt

gen = normaldistrogenerator.NormalDistroGenerator('number',25,50)

data = []

for i in range(1000):
    data.append(gen.generate_values())

plt.hist(data)
plt.show()
