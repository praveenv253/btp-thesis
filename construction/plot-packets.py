#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    a = np.load('packets-input-data.npy')
    m = np.load('packets-metric.npy')
    f = np.load('packets-found-packets.npy')

    ax = plt.subplot(111)

    ax.plot(100 * abs(a), 'k')
    ax.plot(m)
    ax.plot(np.real(f), 'm')

    ax.set_xlim(0, a.size)
    ax.set_ylim(0, 1.05)
    ax.set_xlabel('Sample number, $n$')
    ax.set_ylabel(r'Absolute value of received samples $y$, scaled$\times 100$')

    plt.savefig('packets.ps')
