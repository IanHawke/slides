import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(0, 1, 1000)
y1_diff = np.tanh(100*(x-0.5)) + 1
y2_diff = 0.3*(1 - np.tanh(100*(x-0.5)))
y1_sharp = np.where(x<0.5,
                    np.zeros_like(x),
                    2*np.ones_like(x))
y2_sharp = np.where(x>0.5,
                    np.zeros_like(x),
                    0.6*np.ones_like(x))
fig, axes = plt.subplots(2, 1, figsize=(5, 7))
axes[0].plot(x, y1_diff, 'k-', lw=3)
axes[0].fill_between(x, y1_diff, alpha=0.6, color='blue')
axes[0].plot(x, y2_diff, 'k-', lw=3)
axes[0].fill_between(x, y2_diff, alpha=0.6, color='red')
axes[0].set_xticklabels('')
axes[0].set_yticklabels('')
axes[0].set_xticks([])
axes[0].set_yticks([])
axes[0].set_xlim(0, 1)
axes[0].set_ylabel("Diffuse", size=20)
axes[1].plot(x, y1_sharp, 'k-', lw=3)
axes[1].fill_between(x, y1_sharp, alpha=0.6, color='blue')
axes[1].plot(x, y2_sharp, 'k-', lw=3)
axes[1].fill_between(x, y2_sharp, alpha=0.6, color='red')
axes[1].set_xticklabels('')
axes[1].set_yticklabels('')
axes[1].set_xticks([])
axes[1].set_yticks([])
axes[1].set_xlim(0, 1)
axes[1].set_ylabel("Sharp", size=20)
fig.tight_layout()
fig.savefig('diffuse_vs_sharp.png', bbox_inches='tight')

fig, axes = plt.subplots(2, 1, figsize=(5,7), subplot_kw={"projection": "3d"})

theta = np.linspace(0, 2*np.pi, 8)
theta_circle = np.linspace(0, 2*np.pi, 200)
r_circle = 0.5

phase = 10*np.random.rand(len(theta))
rads = 0.05*(1+np.random.rand(len(theta)))
zs = np.linspace(-1, 1, 100)

axes[0].plot(r_circle*np.cos(theta_circle), r_circle*np.sin(theta_circle), 'k-', lw=3)
axes[0].scatter(r_circle*np.cos(theta), r_circle*np.sin(theta), c='b', s=30)
for i in range(len(theta)):
    axes[0].plot(r_circle*np.cos(theta[i])+rads[i]*np.sin(phase[i]*zs),
                 r_circle*np.sin(theta[i])+rads[i]*np.sin(phase[i]*zs),
                 zs, 'k--', lw=1)
axes[0].set_xticklabels('')
axes[0].set_yticklabels('')
axes[0].set_zticklabels('')
axes[0].set_xticks([])
axes[0].set_yticks([])
axes[0].set_zticks([])
axes[0].set_xlim(-1, 1)
axes[0].set_ylim(-1, 1)
axes[0].set_zlim(-1, 1)

x = np.linspace(-1, 1, 200)
y = np.linspace(-1, 1, 200)
X, Y = np.meshgrid(x, y)
Z = 1.5*(0.25 - X**2 - Y**2)

axes[1].plot_surface(X, Y, Z, alpha=0.3)
axes[1].contour(X, Y, Z, levels=[0], colors=['k'], linewidths=3)
axes[1].set_xticklabels('')
axes[1].set_yticklabels('')
axes[1].set_zticklabels('')
axes[1].set_xticks([])
axes[1].set_yticks([])
axes[1].set_zticks([])
axes[1].set_xlim(-1, 1)
axes[1].set_ylim(-1, 1)
axes[1].set_zlim(-1, 1)

fig.tight_layout()
fig.savefig('track_vs_capture.png', bbox_inches='tight')
