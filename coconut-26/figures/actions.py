"""Reproduce the "Notebook 10" sketch in xkcd style.

Diagram: a set U with a smaller neighbourhood U<.> inside it, mapped by S
into a hatched region S(u); the image S(<u>) of the small neighbourhood
is highlighted in blue and drops down onto an axis, and the same
"depth" is tracked below as a function (S+delta)(<u>) in red that dips
where U<.> lands and recovers away from it.
"""

import glob
import os

import numpy as np
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt

_xkcd_font = None
for path in glob.glob(os.path.expanduser("~/Library/Fonts/*umor*")) + \
        glob.glob("/Library/Fonts/*umor*") + \
        glob.glob("/System/Library/Fonts/Supplemental/*umor*"):
    fm.fontManager.addfont(path)
    _xkcd_font = fm.FontProperties(fname=path).get_name()


def blob(cx, cy, r, amps, freqs, phases, xscale=1.0, yscale=1.0, rot=0.0, n=300):
    theta = np.linspace(0, 2 * np.pi, n)
    radius = r + sum(a * np.cos(f * theta + p) for a, f, p in zip(amps, freqs, phases))
    x = radius * np.cos(theta) * xscale
    y = radius * np.sin(theta) * yscale
    ca, sa = np.cos(rot), np.sin(rot)
    xr = x * ca - y * sa
    yr = x * sa + y * ca
    return cx + xr, cy + yr


def bezier(p0, p1, p2, p3, n=100):
    t = np.linspace(0, 1, n)[:, None]
    p0, p1, p2, p3 = (np.array(p) for p in (p0, p1, p2, p3))
    pts = (1 - t) ** 3 * p0 + 3 * (1 - t) ** 2 * t * p1 + 3 * (1 - t) * t ** 2 * p2 + t ** 3 * p3
    return pts[:, 0], pts[:, 1]


def arrow(ax, p_from, p_to, **kwargs):
    ax.annotate("", xy=p_to, xytext=p_from,
                arrowprops=dict(arrowstyle="->", lw=2, **kwargs))


def valley(x_left, x_right, x_min, y_min, rise, n=150):
    x = np.linspace(x_left, x_right, n)
    w = max(x_min - x_left, x_right - x_min)
    y = y_min + rise * ((x - x_min) / w) ** 2
    return x, y


# def draw_delta(ax, x, y, size, **kwargs):
#     tri_x = [x, x + size * 0.5, x - size * 0.5, x]
#     tri_y = [y + size * 0.9, y - size * 0.5, y - size * 0.5, y + size * 0.9]
#     ax.plot(tri_x, tri_y, **kwargs)


with plt.xkcd(scale=1.1, length=140, randomness=3):
    if _xkcd_font:
        plt.rcParams["font.family"] = [_xkcd_font]
    fig, ax = plt.subplots(figsize=(7, 10))
    ax.set_xlim(0, 10)
    ax.set_ylim(1.5, 15)
    ax.set_aspect("equal")
    ax.axis("off")

    # --- outer set U and inner neighbourhood U<.> -------------------------
    ux, uy = blob(4.6, 12.6, 2.05, [0.30, 0.15, 0.20], [2, 3, 5], [0.3, 1.1, 2.0])
    ax.plot(ux, uy, color="black", lw=2)
    ax.text(6.0, 12.4, r"$\mathcal{U}$", fontsize=24, style="italic")

    ix, iy = blob(4.55, 13.15, 0.78, [0.16, 0.10], [3, 5], [0.5, 2.2])
    ax.plot(ix, iy, color="tab:blue", lw=2)
    ax.text(4.2, 13.15, r"$\mathcal{U}_{<\cdot>}$", fontsize=16, style="italic")

    # --- S(u): open valley curve, minimum aligned with the red curve below -
    cross_x = 4.05                      # shared minimum x: black curve & red curve
    black_y_min = 9.4
    kx, ky = valley(2.7, 6.3, cross_x, black_y_min, 0.55)
    ax.plot(kx, ky, color="black", lw=2)

    # --- S(<u>): open valley curve above it, minimum visibly to the right --
    blue_min_x = cross_x + 0.6
    blue_y_min = 10.3
    # lead_x, lead_y = bezier((3.4, 12.5), (3.6, 11.6), (2.75, 10.9), (3.0, 10.66))
    vx, vy = valley(3.0, 6.6, blue_min_x, blue_y_min, 0.5)
    # bx, by = np.concatenate([lead_x, vx]), np.concatenate([lead_y, vy])
    ax.plot(vx, vy, color="tab:blue", lw=2)

    # rng = np.random.default_rng(3)
    # for i in range(6):
    #     cx = 3.7 + 0.32 * i
    #     cy = 10.05 - 0.03 * i
    #     dx, dy = 0.5, 0.55
    #     ax.plot([cx - dx * 0.3, cx + dx * 0.3], [cy + dy * 0.35, cy - dy * 0.35],
    #             color="black", lw=1.4)

    arrow(ax, (6.2, 12.0), (5.9, 10))
    ax.text(6.6, 9.95, "S(u)", fontsize=13)

    arrow(ax, (4.25, 13.0), (3.9, 10.5), color="tab:blue")
    ax.text(3.05, 10.05, "S(<u>)", fontsize=13, color="tab:blue")

    cross_y = black_y_min                  # black curve's minimum
    cross2_x, cross2_y = blue_min_x, blue_y_min   # blue curve's minimum

    # --- first axis --------------------------------------------------------
    axis1_y = 7.6
    arrow(ax, (1.3, axis1_y - 0.05), (1.3, axis1_y + 1.3))
    arrow(ax, (1.3, axis1_y), (8.6, axis1_y))

    ax.plot([cross_x, cross_x], [cross_y, axis1_y], color="black", lw=1.6, ls=(0, (5, 4)))
    ax.plot([cross2_x, cross2_x], [cross2_y, axis1_y], color="tab:blue", lw=1.6, ls=(0, (5, 4)))

    # --- second axis and the red curve (S+delta)(<u>) ----------------------
    axis2_top, axis2_base = 5.9, 2.6
    arrow(ax, (1.3, axis2_base - 0.05), (1.3, axis2_top))
    arrow(ax, (1.3, axis2_base), (8.6, axis2_base))

    red_y_min = axis2_base + 2.0
    xr, yr = valley(1.8, 7.7, cross_x, red_y_min, 1.15)
    ax.plot(xr, yr, color="tab:red", lw=2)

    label_y = 4.5
    ax.text(6.3, label_y, r"(S+$\Delta$)(<u>)", fontsize=13, color="tab:red")
    # draw_delta(ax, 6.85, label_y + 0.13, 0.28, color="tab:red", lw=1.8)
    # ax.text(7.05, label_y, ")(<u>)", fontsize=13, color="tab:red")

    ax.plot([cross_x, cross_x], [axis1_y, red_y_min], color="black", lw=1.6, ls=(0, (5, 4)))

    fig.tight_layout()
    fig.savefig("actions_figure.svg", bbox_inches='tight')
    # plt.show()
