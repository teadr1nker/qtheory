#!/usr/bin/python3
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

def queueSim(type, Es, Et):
    mu   = 1/Es
    lmbd = 1/Et
    mtx = np.zeros((100, 10000))

    for i in range(100):
        if type[0] == 'm':
            S = np.random.exponential(Es, 9999)
        elif type[0] == 'p':
            S = np.random.pareto(Es, 9999)
        else:
            return None

        if type[1] == 'm':
            T = np.random.exponential(Et, 9999)
        elif type[1] == 'p':
            T = np.random.pareto(Et, 9999)
        else:
            return None

        for j in range(1, 10000):
            mtx[i, j] = max([
            0,
            mtx[i, j-1] + S[i-1] - T[i-1]
            ])

    Ew = None
    if type[0] == 'm':
        #print(f'\n{type}')
        Ew = (lmbd * Es**2) / 2 * (1 - mu)
        #print(E)

    avg = [row.mean() for row in mtx]
    #print(avg)
    plt.plot(avg)
    plt.title(f'Plot {type}, Es:{Es}, Et:{Et}')
    if Ew:
        plt.axhline(Ew)
        plt.legend(['avg mean', 'Ew'])

    if Es < Et:
        str = '<'
    else:
        str = '>'

    plt.savefig(f'plot{type}Es{str}Et.png')
    plt.clf()
    plt.hist(avg, bins=100)
    plt.title(f'Histogram {type}, Es:{Es}, Et:{Et}')
    plt.savefig(f'hist{type}Es{str}Et.png')
    plt.clf()

queueSim('mm1', 5, 1)
queueSim('mm1', 1, 5)

queueSim('mp1', 5, 1)
queueSim('mp1', 1, 5)

queueSim('pm1', 5, 1)
queueSim('pm1', 1, 5)

queueSim('pp1', 5, 1)
queueSim('pp1', 1, 5)
