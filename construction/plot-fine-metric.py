#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

if __name__ == '__main__':
    a = np.load('metric-input-data.npy')
    m = np.load('metric-metric.npy')
    fm = np.load('fine-metric-fine-metric.npy')

    ax = plt.subplot(111)

    # Add the threshold line
    threshold = 0.8
    ax.plot(np.arange(m.size), threshold * np.ones(m.size), '#888888')

    ax.plot(100 * abs(a), 'k')
    ax.plot(m)

    # Make the shaded region
    x = np.where(m > threshold)[0]
    a = x[0]
    b = x[-1]
    points = [(i, m[i]) for i in x]
    verts = [(a, 0)] + points + [(b, 0)]
    poly = Polygon(verts, facecolor='0.92', edgecolor='0.5')
    ax.add_patch(poly)

    ax.plot(abs(fm))

    ax.set_xlim(0, m.size)
    ax.set_ylim(0, 1.1)
    ax.set_xlabel('Sample number, $n$')
    ax.set_ylabel(r'Absolute value of received samples $y$, scaled$\times 100$')

    plt.savefig('fine-metric.ps')
