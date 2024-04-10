import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon

fig, ax = plt.subplots()
x = np.linspace(0.5, 6, 200)
ax.plot(x, 1 / x, label='y = 1/x')
ax.set_xlim(0, 5.5)

for i in range(1, 6): 
    poly = Polygon([[i, 0], [i, 1/i], [i+1, 1/(i)], [i+1, 0]], closed=True, facecolor='1', edgecolor='0.3')
    ax.add_patch(poly)

ux = np.linspace(1, 6, 200)
under_graph_verts = [(1, 0), *zip(ux, 1 / ux), (6, 0)]
poly = Polygon(under_graph_verts, closed=True, facecolor='#D67B7BB0', edgecolor='r')
ax.add_patch(poly)

ax.annotate(r'$\ln(x)$', xy=(1, 0.4), xytext=(0.2, 0.6), fontsize=12,
            arrowprops=dict(color='#D67B7B', width=0.5, headwidth=6, shrink=0.05))
ax.annotate(r'$\frac{1}{x}$', xy=(3, 0.5), xytext=(4, 0.45), fontsize=18,
            arrowprops=dict(color='0.3', width=0.5, headwidth=6, shrink=0.05))

fig.savefig('rendered/euler_constant.png', bbox_inches='tight')
ax.clear()

x = np.linspace(1, 5, 100)
ax.plot(x, 1 / x, label='y = 1/x')
ax.set_ylim(0, 0.8)
ax.set_xlim(1.5, 4.5)
ax.set_xticks([2, 4], ['N', 'N+1'])
ax.set_yticks([1/2, 1/4], [r'$\frac{1}{N}$', r'$\frac{1}{N+1}$'])

x = np.linspace(2, 4, 100)
under_graph_verts = [(2, 0), *zip(x, 1 / x), (4, 0)]
under_graph = Polygon(under_graph_verts, fill=False, closed=True, color='0.3', linestyle=':', hatch='\\')
ax.add_patch(under_graph)
rect = Polygon([(2, 0),(2, 0.25), (4, 0.25), (4, 0)], closed=True, color='#D67B7BA0', linestyle='')
ax.add_patch(rect)

ax.annotate(r'$\frac{1}{N+1}$', xy=(2, 0.125), xytext=(1.60, 0.05), fontsize=12,
            arrowprops=dict(color='#D67B7B', width=0.5, headwidth=6, shrink=0.05))
ax.annotate(r'$\int_N^{N+1}\frac{1}{x} \; dx$', xy=(3, 0.33), xytext=(3.4, 0.4), fontsize=12,
            arrowprops=dict(color='0.3', width=0.5, headwidth=6, shrink=0.1))

fig.savefig('rendered/euler_constant_decreasing.png', bbox_inches='tight')
