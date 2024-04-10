import matplotlib.pyplot as plt
import numpy as np

def logistic(x, mu, s):
    return 1/(1 + np.exp(-(x - mu)/s))

def density_function(x, mu, s):
    return np.exp(-(x - mu)/s) / (s * (1 + np.exp(-(x - mu)/s))**2)


fig, ax = plt.subplots()

xs = [np.linspace(-15, 15, 1000)] * 3
mu = 3

for i, x in enumerate(xs):
    s = 1 + i * 0.5
    ax.plot(x, density_function(x, mu, s), label=f's={s}')

ax.legend()
ax.set_ylim(-0.01, 0.4)
ax.set_xlim(-15, 15)

ax.set_xticks([3], [r'$\mu$'])
ax.axvline(x=mu, ls=':', lw=1, color='black')

fig.savefig('rendered/logistic_density.png', bbox_inches='tight')
