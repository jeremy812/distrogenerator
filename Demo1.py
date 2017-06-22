from functionbucketmaker import functionbucketmaker
from matplotlib import pyplot as plt

function = 'sin(x)'
decimalplaces = 1
range = [0, 8]


buckets = functionbucketmaker(function, decimalplaces, range)

plt.plot(buckets[0], buckets[1], marker = 'o')
plt.show()

