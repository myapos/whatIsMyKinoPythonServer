import sys
sys.path.append('./utils/')

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
import parsedate
# Generate random numbers in array
import json

randomNumbers= np.random.laplace(loc=15, scale=3, size=500)

# print('randomNumbers', randomNumbers)
# print('---------------------------')
# print('randomNumbers', randomNumbers[:10])

# Create histogram

hist, bin_edges = np.histogram(randomNumbers)
# print('hist:',hist)
# print('bin_edges:',bin_edges)

# testData= [1,2,2,2,2,4,2,1323,432,345,545,6,4,3,45,564,65,3,4,5,4]
# plt.hist(testData)
# plt.savefig('test.png')


randomData=[]
i = 1
while i <= 20:
#   print(i)
  randomData.append(random.randrange(80))
  i += 1

print('randomData',randomData)

# An "interface" to matplotlib.axes.Axes.hist() method
freq, bins, patches = plt.hist(randomData, bins=range(0, 80 + 1, 1), color='#0504aa',
                            alpha=0.7, rwidth=0.85)
plt.savefig('randomData.png')

print('---------')
print('freq',freq)
print('---------')
print('bins',bins)
print('---------')
print('patches',patches)
# print('bins',bins)
# print("Generate random integer number within a given range in Python ")
# #random.randrange() with only one argument
# print("Random number between 0 and 10 : ", random.randrange(80))

# #random.randrange() with two arguments
# print("Random number between 20 and 40 : ", random.randrange(20, 40))

# #random.randrange() with three argument
# print("Random number between 0 and 60 : ", random.randrange(0, 60, 6))

# parsedate.fib(4)


x = '{ "name":"John", "age":30, "city":"New York"}'

y = json.loads(x)
# the result is a Python dictionary:
print('age:',y["age"])
