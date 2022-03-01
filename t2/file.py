#!/usr/bin/python3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import sys
import scipy.stats as stat
#sys.path.append('../common/')
#from tex import tex

'''
class MarkovChain:
    def __init__(self, p, s):
        self.P = p
        if s >= 1 and s <= p.shape[0]:
            self.state = s
        else:
            return None
        self.maxStates = p.shape[0]

    def changeState(self):
        prob = np.random.uniform()
        s = self.P[self.state - 1]
        p = 0.0
        for i in range(self.maxStates):
            p += s[i]
            if prob < p:
                self.state = i + 1
                break

        return self.state
'''

V = 18
df = pd.read_csv('Lab2.Matrix.txt', delimiter='\t')
dfv = df.iloc[[V]]
P = np.array([dfv['p_11'], dfv['p_12'], dfv['p_13'],
              dfv['p_21'], dfv['p_22'], dfv['p_23'],
              dfv['p_31'], dfv['p_32'], dfv['p_33']]).reshape(3, 3)

#1
print('1)')
A=np.append(P.T-np.identity(3),[[1,1,1]],axis=0)
b=np.array([0,0,0,1]).T
statDist = np.linalg.solve(A.T.dot(A), A.T.dot(b))
print(f'Stationary distribution {statDist}')

#2
print('2)')
for i in range(P.shape[0]):
    print()
    state=[np.zeros(P.shape[0])]
    state[0][i] = 1.0
    stateHist=state
    dfStateHist=pd.DataFrame(state)
    #distr_hist = [[0,0,0]]
    for x in range(10000):
        state=np.dot(state, P)
        stateHist=np.append(stateHist,state,axis=0)
        if x == 9 or x == 99 or x == 999 or x ==9999:
            print(f'Distance at {x + 1} :{abs(np.prod(state[0] - statDist))}')
    print(f'Start state {i}: {state[0]}')
    dfDistrHist = pd.DataFrame(stateHist)
    dfDistrHist.plot()
    plt.title(f'Start state: {i}')
    plt.savefig(f'plot{i}.png')
    plt.clf()

#3
print('3)')
e = 1e-30
for i in range(P.shape[0]):
    state=[np.zeros(P.shape[0])]
    state[0][i] = 1.0
    distr_hist = [[0,0,0]]
    count = 0
    n = e+1
    while n > e:
        count += 1
        state=np.dot(state, P)
        n = np.min([
        abs(np.prod(state[0] - statDist)) for i in range(P.shape[0])
        ])
    print(f'Requieres {count} steps, from state {i}')
