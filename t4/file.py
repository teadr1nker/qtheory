#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt

#1
lmbd = 3
mu1 = 4
mu2 = 10
T = 10000
N = 1000
meanEnd = np.zeros(N) #average time spent past time limit
count = [] #amount of requests in the system at current moment
time = []  #time each request spends in the system

for c in range(N):
    t = 0. #time
    n1 = 0 #current number of requests to server 1
    n2 = 0 # -/- 2
    NA = 0 #number of pending requests
    ND = 0 #number of done requests
    tA = np.random.exponential(lmbd) #time remaining for next request
    t1 = np.infty #time for request processing on server 1
    t2 = np.infty # -/- 2
    A1 = [] #time of request n
    A2 = []
    D = [] #time of completion
    print(f'sim {c}')
    end = 0 #last request number
    count.append([])
    while t < T or n1 > 0 or n2 > 0:
        # adding request
        if tA == min([tA, t1, t2]):
            t = tA
            NA += 1
            n1 += 1
            tA = t + np.random.exponential(lmbd) if t < T else np.infty
            t1 = t + np.random.exponential(mu1)
            A1.append(t)
        # passing request to second server
        elif t1 <= t2:
            t = t1
            n1 -= 1
            n2 += 1
            t1 = t + np.random.exponential(mu1) if n1 > 0 else np.infty

            t2 = t + np.random.exponential(mu2)
            A2.append(t)
        # completing the request
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
m = np.mean(meanEnd)
plt.axhline(m, color='orange')
plt.legend(['meaningless plot', f'mean: {m}'])
plt.ylabel('Time')
plt.savefig('meanEnd.png')
plt.clf()

plt.plot(meanTime)
plt.title('Average time per request')
plt.xlabel('Request')
plt.ylabel('Time')
plt.savefig('meanTime.png')
plt.clf()
