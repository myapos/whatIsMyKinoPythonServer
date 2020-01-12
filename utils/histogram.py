
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

    # print('---------')
    # print('freq',freq)
    # print('---------')
    # print('bins',bins)
    # print('---------')
    # print('patches',patches)

    i=0;
    graphData=[]
    for f in freq:
        # print('f:',f)
        i=i+1
        # dict[i]=f
        dict={
            "kino":i,
            "frequency":f
        }
        graphData.append(dict)

    print('graphData',graphData)

    # print('-------------------')
    # print('frequencies size', len(freq.tolist()))
    # print('bins size', len(bins.tolist()))

    # histogramValues = {
    #     "frequencies": freq.tolist(),
    #     "bins": bins.tolist(),
    #     "kinos": kinos,
    # }
    return graphData