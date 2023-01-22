#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt

def queueSim(mu, lmbd, N=100):
    Es = 1/mu
    Et = 1/lmbd
    W = np.zeros(N)
    U = np.zeros(N)
    Z = np.zeros(N)
    Wn = np.zeros(N)
    
    s = '<' if Es < Et else '>'
    print(f'Type: mm1, lambda: {lmbd}, mu: {mu}, Es: {Es} Et: {Et} N: {N}')

    S = np.random.exponential(Es, N-1)
    T = np.random.poisson(Et, N-1)

    for i in range(1, N):
        W[i] = max(0, W[i-1] + S[i-1] - T[i-1])
        U[i] = S[i-1] - T[i-1]
        Z[i] = U.sum()
        Wn[i] = max(Z)


    ro = Es / Et
    print(f"ro: {ro}")
    print(f'EW: {W.mean()}')
    print(f'EWn: {Wn.mean()}')
    print(f"EZ: {Z.mean()}")

    dpi = 180
    plt.figure(figsize=(1600/dpi, 900/dpi), dpi=dpi)
    plt.plot(W)
    plt.plot(Wn, "r.")
    plt.xlabel("client number: n")
    plt.ylabel('Waiting time: W')
    plt.title(f'Type: mm1, lambda: {lmbd}, mu: {mu}, Es: {Es} Et: {Et}')
    plt.legend(['W', 'Wn'])
    plt.savefig(f'plotEs{s}Et{N}.png')
    plt.clf()
    #plt.hist(W)
    #plt.hist(Wn)
    #plt.savefig(f'histEs{s}Et{N}.png')
    #plt.clf()

queueSim(4, 8)
queueSim(16, 2)
queueSim(4, 8, 10000)
queueSim(16, 2, 10000)