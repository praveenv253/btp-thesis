#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    a = np.load('metric-input-data.npy')
    m = np.load('metric-metric.npy')
    f = np.load('metric-found-packets.npy')

    ax = plt.subplot(111)

    ax.plot(100 * abs(a), 'k')
    ax.plot(m)
    ax.plot(np.real(f), 'm')

    ax.set_xlim(0, a.size)
    ax.set_ylim(0, 1.1)
    ax.set_xlabel('Sample number, $n$')
    ax.set_ylabel(r'Absolute value of received samples $y$, scaled$\times 100$')

    plt.savefig('metric.ps')
