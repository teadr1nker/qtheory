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

    for i in range(100):
        if type[0] == 'm':
            S = np.random.exponential(Es, N-1)
        elif type[0] == 'p':
            S = np.random.pareto(Es, N-1)
        else:
            return None

        if type[1] == 'm':
            T = np.random.exponential(Et, N-1)
        elif type[1] == 'p':
            T = np.random.pareto(Et, N-1)
        else:
            return None

        for j in range(1, N):
            mtx[i, j] = max([
            0,
            mtx[i, j-1] + S[j-1] - T[j-1]
            ])

    EW = None
    if type[1] == 'm':
        EW = (lmbd * np.mean(S ** 2)) / (2*(1 - mu))
        print(EW)
    '''avg = [row.mean() for row in mtx]
    #print(avg)
    plt.plot(avg)
    plt.title(f'Plot {type}, Es:{Es}, Et:{Et}')
    if Ew:
        plt.axhline(Ew, color='orange')
        plt.legend(['avg mean', f'Ew={Ew}'])

    if Es < Et:
        str = '<'
    else:
        str = '>'

    plt.savefig(f'plot_{type}_Es{str}Et.png')
    plt.clf()
    plt.hist(avg, bins=100)
    plt.title(f'Histogram {type}, Es:{Es}, Et:{Et}')
    plt.savefig(f'hist_{type}_Es{str}Et.png')
    plt.clf()'''

    avg = np.array([row.mean() for row in mtx.T])
    plt.plot(avg)
    if EW:
        plt.axhline(EW, color='red')
    plt.title(f'Plot {type}, Es:{Es}, Et:{Et}')
    str = '<' if Es < Et else '>'
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
