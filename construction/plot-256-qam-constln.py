#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    grid = np.mgrid[-15:15:16j, -15:15:16j]
    x = grid[0]
    y = grid[1]

    mew = 2
    plt.figure(0, (8, 8))
    ax = plt.subplot(111)

    ax.plot(x, y, color='none', mec='#262626', marker='x', mew=mew)
    ax.plot(x + 32, y, 'rx', mew=mew)
    ax.plot(x - 32, y, 'gx', mew=mew)
    ax.plot(x, y + 32, 'bx', mew=mew)
    ax.plot(x, y - 32, 'yx', mew=mew)
    ax.plot(x - 32, y + 32, 'cx', mew=mew)
    ax.plot(x + 32, y + 32, 'mx', mew=mew)
    ax.plot(x + 32, y - 32, color='none', mec='brown', marker='x', mew=mew)
    ax.plot(x - 32, y - 32, color='none', mec='chartreuse', marker='x', mew=mew)

    ax.axis('equal')
    ax.set_xlim(-22, 22)
    ax.set_xticks((-21, -15, -9, -3, 3, 9, 15, 21))
    ax.set_ylim(-22, 22)
    ax.set_yticks((-21, -15, -9, -3, 3, 9, 15, 21))
    plt.savefig('256-qam-reptd-constln.ps')
