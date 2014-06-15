#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    plt.figure(0, (8, 2))
    ax = plt.subplot(111)

    # Plot the axis first
    ax.plot([-17, 17], [0, 0], 'k-')

    # Plot the constellation points
    ax.plot(np.linspace(-15, 15, 16), np.zeros(16), 'bx', mec='#1144dd', mew=2, ms=8)

    # Mark the constellation points
    y0 = -1.5
    x0 = -0.95
    xi = 1.02
    for i in range(-15, 1, 2):
        ax.annotate('$'+str(i)+'$', xy=(x0 + xi * i, y0))
    x0 = -0.2
    xi = 0.98
    for i in range(1, 17, 2):
        ax.annotate('$'+str(i)+'$', xy=(x0 + xi * i, y0))

    # Mark the bit sequences
    bits = ['1000', '1001', '1011', '1010', '1110', '1111', '1101', '1100',
            '0000', '0001', '0011', '0010', '0110', '0111', '0101', '0100']
    x0 = -16
    y0 = [1, 2]
    xi = 1
    for i in range(16):
        ax.annotate('$'+bits[i]+'$', xy=(x0 + 2 * xi * i, y0[i % 2]))

    # Set the limits on the figure
    ax.axis('equal')
    ax.set_xlim(-17, 17)
    ax.set_ylim(-1, 1)

    # Remove all axes
    spines_to_remove = ['top', 'right', 'left', 'bottom']
    for spine in spines_to_remove:
        ax.spines[spine].set_visible(False)

    # Get rid of ticks. The position of the numbers is informative enough of
    # the position of the value.
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')

    # Remove axis labels
    ax.set_xticks([])
    ax.set_yticks([])

    plt.savefig('16-pam-constln.ps')
