from math import *
from matplotlib import pyplot as plt




def functionbucketmaker(func, decimalplaces=2, minmax=[0, 1]):

    #check func for nasty eval stuff

    xvalues=[]
    yvalues=[]
    totalValues = 0
    deltax = 10**(-1*decimalplaces)

    numvalues = int((minmax[1]-minmax[0] * 1.0) / deltax)

    for i in range(numvalues):

        x = round(minmax[0] + i * deltax, decimalplaces)
        xvalues.append(x)

        y = max(eval(func), 0)
        yvalues.append(y)

        totalValues += y

    if totalValues == 0:
        yvalues[0] = 1
        return [xvalues, yvalues]

    scaled = [y * 1.0 / totalValues for y in yvalues]

    return [xvalues, scaled]

# testbuckets = functionbucketmaker('sin(x)+1', 2, [0,2])
# for x in range(len(testbuckets[0])):
#     print(str(testbuckets[0][x])+' - ' + str(testbuckets[1][x]))
# plt.plot(testbuckets[0],testbuckets[1])
# plt.axis([0, 14, 0, 0.01])
# plt.show()