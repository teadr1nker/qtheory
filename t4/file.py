#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt

#1
lmbd = 3
mu1 = 6
mu2 = 9
T = 10000
N = 1000
meanEnd = np.zeros(N)
#count = np.array(N, list)
count = []
#time = np.zeros((N, 1000))
time = []

for c in range(N):
    t = 0.
    n1 = 0
    n2 = 0
    NA = 0
    ND = 0
    tA = np.random.exponential(lmbd)
    t1 = np.infty
    t2 = np.infty
    A1 = []
    A2 = []
    D = []
    print(f'sim {c}')
    end = 0
    count.append([])
    while t < T or n1 > 0 or n2 > 0:

        if tA == min([tA, t1, t2]):
            t = tA
            NA += 1
            n1 += 1
            tA = t + np.random.exponential(lmbd) if t < T else np.infty
            #tA = t + np.random.exponential(lmbd)
            t1 = t + np.random.exponential(mu1)
            A1.append(t)

        elif t1 <= t2:
            t = t1
            n1 -= 1
            n2 += 1
            t1 = t + np.random.exponential(mu1) if n1 > 0 else np.infty

            t2 = t + np.random.exponential(mu2)
            A2.append(t)

        else:
            t = t2
            ND += 1
            n2 -= 1
            t2 = t + np.random.exponential(mu2) if n2 > 0 else np.infty
            D.append(t)
            count[c].append(NA - ND)
            if t < T:
                end = ND
    #print(len(D), len(A1))
    time.append(np.array(D) - np.array(A1))


    #2.2
    meanEnd[c] = np.mean(np.array(D[end:]) - T)

#2.3
MIN = min([len(timer) for timer in time])

meanTime = np.zeros(MIN)
for i in range(MIN):
    res = 0.
    for j in range(N):
        res += time[j][i]
    meanTime[i] = res/N

#2.1
MAX = max([len(counter) for counter in count])

meanCount = np.zeros(MAX)
for i in range(MAX):
    res = 0.
    for j in range(N):
        res += count[j][i] if len(count[j]) > i else 0.
    meanCount[i] = res/N

#print(meanCount)

plt.plot(meanCount)
plt.title('Average amount of requests at given moment')
plt.xlabel('Moment')
plt.ylabel('Number of requests')
plt.axvline(end, color='orange')
plt.savefig('meanCount.png')
plt.clf()

plt.plot(meanEnd)
plt.title(f'Average time spent after time limit = {T}')
plt.xlabel('Run number')
plt.ylabel('Time')
plt.savefig('meanEnd.png')
plt.clf()

plt.plot(meanTime)
plt.title('Average time per request')
plt.xlabel('Request')
plt.ylabel('Time')
plt.savefig('meanTime.png')
plt.clf()
