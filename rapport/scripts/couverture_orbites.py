from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from visual_style import COLORS as C

OUT = Path(__file__).resolve().parents[1] / 'figures'
fig, ax = plt.subplots(figsize=(8.6, 5.3))
fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
ax.set_aspect('equal')
ax.set(xlim=(-3.35, 1.55), ylim=(-2.25, 2.25))
ax.axis('off')

# Même foyer et même paramètre p = 1 que la figure 4 ; traits fins et pleins.
for e, color, width in [
    (0, C['accent'], 1.0),
    (.55, C['schemaGreen'], 1.0),
    (1.3, C['schemaPurple'], .85),
    (1.9, C['schemaOrange'], .85),
]:
    limit = np.pi if e < 1 else np.arccos(-1/e) - .06
    theta = np.linspace(-limit, limit, 2400)
    radius = 1 / (1 + e * np.cos(theta))
    ax.plot(radius * np.cos(theta), radius * np.sin(theta),
            color=color, lw=width, solid_capstyle='round')

# Le centre d'attraction constitue l'unique repère de l'illustration.
ax.plot(0, 0, 'o', color=C['schemaOrange'], ms=4, markeredgewidth=0, zorder=5)
fig.savefig(OUT / 'couverture_orbites.pdf', transparent=True,
            bbox_inches='tight', pad_inches=.02)
fig.savefig(OUT / 'couverture_orbites.png', transparent=True,
            bbox_inches='tight', pad_inches=.02, dpi=180)
plt.close(fig)
