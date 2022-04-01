#!/usr/bin/python3
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

def queueSim(type, Es, Et):
    mu   = 1/Es
    lmbd = 1/Et
    n = 100
    N = 1000
    mtx = np.zeros((n, N))
    str = '<' if Es < Et else '>'
    print(f'Type: {type}, lambda: {lmbd}, mu: {mu}, Es {str} Et')
    a = 10.0

    for i in range(100):
        if type[1] == 'm':
            S = np.random.exponential(Es, N-1)
        elif type[1] == 'p':
            S = (np.random.pareto(a, N-1)+1) * Es
        else:
            return None

        if type[0] == 'm':
            T = np.random.exponential(Et, N-1)
        elif type[0] == 'p':
            T = (np.random.pareto(a, N-1)+1) * Et
        else:
            return None

        for j in range(1, N):
            mtx[i, j] = max([
            0,
            mtx[i, j-1] + S[j-1] - T[j-1]
            ])

    ro = Es / Et
    #print('aaa', S.mean(), T.mean(), ro)
    EW = None
    if 1 - ro > 0:
        #EW = (lmbd * np.mean(S ** 2)) / (2*(1 - mu))
        #EW = (lmbd*Es**2)/(2*(1-ro))
        if type[0] == 'm':
            if type[1] == 'p':
                #EW = (lmbd*mu) / (2*(mu-2)*(1-(mu*lmbd)/(mu-1)))
                EW = (lmbd*np.mean(S**2))/(2*(1-ro))
            else:
                EW = lmbd/(mu*(mu-lmbd))

    avg = np.array([row.mean() for row in mtx.T])
    plt.plot(avg)

    if EW:
        print(f'EW: {EW} real mean: {avg.mean()}')
        plt.axhline(EW, color='red')
    plt.title(f'Plot {type}, Es:{Es}, Et:{Et}')
    plt.savefig(f'plot_{type}_Es{str}Et.png')
    plt.clf()

queueSim('mm1', 5, 2)
queueSim('mm1', 2, 5)

queueSim('mp1', 5, 2)
queueSim('mp1', 2, 5)

queueSim('pm1', 5, 2)
queueSim('pm1', 2, 5)

queueSim('pp1', 5, 2)
queueSim('pp1', 2, 5)
