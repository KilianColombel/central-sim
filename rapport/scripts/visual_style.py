from pathlib import Path
import re

PALETTE_FILE = Path(__file__).resolve().parents[1] / 'figures' / 'palette.tex'
_DEFINITION = re.compile(
    r'\\definecolor\{([^}]+)\}\{HTML\}\{([0-9A-Fa-f]{6})\}'
)

COLORS = {
    name: f'#{value.upper()}'
    for name, value in _DEFINITION.findall(PALETTE_FILE.read_text(encoding='utf-8'))
}

_REQUIRED = {
    'accent', 'schemaOrange', 'schemaGreen', 'schemaInk', 'schemaMuted',
    'schemaPurple', 'schemaNeutral', 'schemaGrid',
}
_MISSING = _REQUIRED - COLORS.keys()
if _MISSING:
    raise ValueError(f'Couleurs absentes de {PALETTE_FILE.name} : {sorted(_MISSING)}')


def configure_matplotlib(plt, font_size=9):
    plt.rcParams.update({
        'font.family': 'DejaVu Sans',
        'font.size': font_size,
        'text.color': COLORS['schemaInk'],
        'axes.labelcolor': COLORS['schemaInk'],
        'axes.edgecolor': COLORS['schemaMuted'],
        'axes.titlecolor': COLORS['schemaInk'],
        'xtick.color': COLORS['schemaMuted'],
        'ytick.color': COLORS['schemaMuted'],
        'grid.color': COLORS['schemaGrid'],
        'axes.spines.top': False,
        'axes.spines.right': False,
        'axes.titleweight': 'bold',
        'pdf.fonttype': 42,
    })
