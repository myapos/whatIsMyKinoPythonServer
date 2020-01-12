
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
import parsedate
# Generate random numbers in array
import json

#compute Hist with maptplot
def computeHist(kinos):    # write Fibonacci series up to n
    # Create histogram
    freq, bins, patches = plt.hist(kinos,range(1, 81 + 1, 1),color='#0504aa', rwidth=1)
    # freq, bins, patches = plt.hist(kinos,bins=79, color='#0504aa')

    plt.xlabel('kinos', fontdict=None, labelpad=None)
    plt.ylabel('freq', fontdict=None, labelpad=None)
    plt.savefig('kinos.png')

    i=0;
    graphData=[]
    for f in freq:
        i=i+1
        dict={
            "kino":i,
            "frequency":f
        }
        graphData.append(dict)

    print('graphData',graphData)

    return graphData