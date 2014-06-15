#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    a = np.load('double-peak-input-data.npy')
    m = np.load('double-peak-metric.npy')

    ax = plt.subplot(111)

    ax.plot(5 * abs(a), 'k')
    ax.plot(m.real)

    ax.set_xlim(0, a.size)
    ax.set_ylim(0, 1)
    ax.set_xlabel('Sample number, $n$')
    ax.set_ylabel(r'Absolute value of received samples $y$, scaled$\times 5$')

    ax.annotate('Plateau', xy=(222, 0.021), xytext=(50, 0.15),
                arrowprops={'arrowstyle':'-',
                            'connectionstyle':'arc,angleA=0,armA=100,'
                                              'angleB=-80,rad=20'})

    plt.savefig('double-peak.ps')
