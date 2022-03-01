#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import sys
import scipy.stats as stat
sys.path.append('../common/')
from tex import tex

def density(data, n):
    c, b = np.histogram(data, bins=n)
    return (b[:-1], c)

def centlim(sigma, a, k = 12, n = 10000):
    U = np.random.uniform(size=n)
    for i in range(k-1):
        U = U + np.random.uniform(size=n)

    res = (U - k / 2) / np.sqrt(k / 12)
    return res * a + sigma

V = 18
tex.printhead()
tex.section('Exponential distribution')
#exp
size = 10000
data = np.random.exponential(V, size)
tex.plaintext(data)

labels = []
size2 = 100
for i in range(5):
    data = np.random.exponential(V, size2)
    b, c = density(data, 25)
    plt.plot(b, c / max(c))
    labels.append(f'{size2}')
    size2 *= 10

y = np.exp(-(b / V))
plt.plot(b, y / np.max(y), linestyle='--')
labels.append('Distribution')

plt.legend(labels)
plt.xlabel('Samples'); plt.ylabel('Porb')
plt.savefig('exp.png')
tex.addimage('exp.png')
plt.clf()

#normal
tex.section('Normal distribution')
sigma = 0.1
data = np.random.normal(V, sigma, size)
tex.plaintext(data)

print('Law of large numbers')
means = np.zeros(1000)
for i in range(1000):
    means[i] = np.mean(np.random.normal(V, sigma, size=10 * (i+1)))

plt.plot(np.linspace(10, 10000, 1000), means)
plt.axhline(y=V, color='r', linestyle='--')
plt.savefig('LoLN1.png')
tex.addimage('LoLN1.png')
plt.clf()

labels = []
size2 = 100
for i in range(5):
    data = np.random.normal(V, sigma, size=size2)
    b, c = density(data, 25)
    plt.plot(b, c / max(c))
    labels.append(f'{size2}')
    size2 *= 10

y = 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (b - V)**2 / (2 * sigma**2))
plt.plot(b, y / np.max(y), linestyle='--')
labels.append('Distribution')
plt.legend(labels)
plt.xlabel('Samples'); plt.ylabel('Porb')
plt.savefig('norm.png')
tex.addimage('norm.png')
plt.clf()



#Central limit theorem
sigma = 0.1
tex.section('Central limit theorem')
data = centlim(V, sigma,)
tex.plaintext(data)
print('Law of large numbers')
labels = []
size2 = 100
for i in range(5):
    data = centlim(V, sigma, n=size2)
    b, c = density(data, 25)
    plt.plot(b, c / max(c))
    labels.append(f'{size2}')
    size2 *= 10

y = 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (b - V)**2 / (2 * sigma**2))
plt.plot(b, y / np.max(y), linestyle='--')
labels.append('Distribution')
plt.legend(labels)
plt.xlabel('Samples'); plt.ylabel('Porb')
plt.savefig('clt.png')
tex.addimage('clt.png')
plt.clf()

print('Law of large numbers')
#means = np.zeros(1000)
for i in range(1000):
    means[i] = np.mean(centlim(V, sigma, n=10 * (i+1)))

plt.plot(np.linspace(10, 10000, 1000), means)
plt.axhline(y=V, color='r', linestyle='--')
plt.savefig('LoLN2.png')
tex.addimage('LoLN2.png')
plt.clf()


tex.printline('Kolmogorov-Smirnov test')
ndata = (data - V) / sigma
tex.plaintext(stat.kstest(ndata, 'norm'))

#pareto
tex.section('Pareto distribution')
a, m = V + 2., 1.

data = (np.random.pareto(a, 10000) + 1) * m
data = np.random.exponential(V, size2)
b, c = density(data, 25)
fit = (a*m**a) / (b**(a+1))
plt.plot(b, c / max(c))
plt.plot(b, fit/max(fit), linestyle='--')
plt.legend(['generated', 'Pareto distr'])
plt.xlabel('Samples'); plt.ylabel('Porb')
plt.savefig('pareto.png')
tex.addimage('pareto.png')

tex.printend()
