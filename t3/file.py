#!/usr/bin/python3
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

def queueSim(type, mu, lmbd):

    Es = mu/(mu - 1) if type[1] == 'p' else 1/mu
    Et = 1/lmbd
    #mu   = 1/Es
    #lmbd = 1/Et
    n = 100
    N = 1000
    mtx = np.zeros((n, N))
    str = '<' if Es < Et else '>'
    print(f'Type: {type}, lambda: {lmbd}, mu: {mu}, Es {str} Et')
    a = 50.

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

    ro = Es / Et if type[1] != 'p' else (lmbd*mu)/(mu - 1)
    EW = None
    if ro < 1:
        if type == 'mm1':
            EW = lmbd / (mu * (mu - lmbd))
        elif type == 'mp1':
            #print(type)
            EW = (lmbd*(mu/(mu - 2))) / (2 * (1 - ro))


    avg = np.array([row.mean() for row in mtx.T])
    plt.plot(avg)

    if EW:
        print(f'EW: {EW} real mean: {avg.mean()}')
        plt.axhline(EW, color='red')
    plt.title(f'Plot {type}, Es:{round(Es, 4)}, Et:{round(Et, 4)}')
    plt.xlabel('Request'); plt.ylabel('Waiting time')
    plt.savefig(f'plot_{type}_Es{str}Et.png')
    plt.clf()

queueSim('mm1', 4, 8)
queueSim('mm1', 8, 4)

queueSim('mp1', 8, 0.5)
queueSim('mp1', 2, 8)

queueSim('pm1', 4, 8)
queueSim('pm1', 8, 4)

queueSim('pp1', 4, 8)
queueSim('pp1', 8, 4)
