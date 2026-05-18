"""
CCS 2226 - Foundations of Artificial Intelligence
Task Two - Constraint Satisfaction Problem (CSP)
Part a - Colour the Australia Map using 3 colours

Rules:
- Use only 3 colours: Blue, Red, Green
- No two regions that share a border can have the same colour
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
import numpy as np


# AUSTRALIA MAP - REGIONS AND THEIR BORDERS


australia = {
    'WA':  ['NT', 'SA'],
    'NT':  ['WA', 'SA', 'QLD'],
    'SA':  ['WA', 'NT', 'QLD', 'NSW', 'VIC'],
    'QLD': ['NT', 'SA', 'NSW'],
    'NSW': ['SA', 'QLD', 'VIC'],
    'VIC': ['SA', 'NSW'],
    'TAS': []
}

colours = ['Blue', 'Red', 'Green']

# ─────────────────────────────────────────────
# CSP SOLVER
# ─────────────────────────────────────────────

def is_valid(region, colour, assignment):
    for neighbour in australia[region]:
        if neighbour in assignment and assignment[neighbour] == colour:
            return False
    return True

def backtrack(assignment):
    if len(assignment) == len(australia):
        return assignment
    unassigned = [r for r in australia if r not in assignment]
    region = unassigned[0]
    for colour in colours:
        if is_valid(region, colour, assignment):
            assignment[region] = colour
            result = backtrack(assignment)
            if result is not None:
                return result
            del assignment[region]
    return None

# ─────────────────────────────────────────────
# RUN SOLVER
# ─────────────────────────────────────────────

print("="*55)
print("  CSP - Australia Map Colouring")
print("  Colours: Blue, Red, Green")
print("  Rule: No two adjacent regions same colour")
print("="*55)

solution = backtrack({})

print("\nSOLUTION:")
print(f"{'Region':<15} {'Colour'}")
print("-"*30)
for region, colour in solution.items():
    print(f"{region:<15} {colour}")

# ─────────────────────────────────────────────
# APPROXIMATE POLYGON SHAPES FOR EACH REGION
# These coordinates approximate real Australia map shapes
# ─────────────────────────────────────────────

region_shapes = {
    'WA': np.array([
        [0, 0], [0, 9], [1, 9], [1, 11], [4, 11],
        [4, 7], [3.5, 5], [4, 0]
    ]),
    'NT': np.array([
        [4, 6], [4, 11], [7, 11], [7, 8], [6.5, 6]
    ]),
    'SA': np.array([
        [4, 0], [3.5, 5], [4, 6], [6.5, 6],
        [7, 4], [6.5, 0]
    ]),
    'QLD': np.array([
        [7, 8], [7, 11], [11, 11], [11, 5], [9, 5],
        [8, 6], [7, 6], [7, 8]
    ]),
    'NSW': np.array([
        [6.5, 3], [7, 4], [8, 6], [9, 5],
        [11, 5], [11, 3], [8.5, 2], [6.5, 3]
    ]),
    'VIC': np.array([
        [6.5, 0], [7, 4], [6.5, 3], [8.5, 2],
        [10, 1], [9, 0]
    ]),
    'TAS': np.array([
        [8, -2], [8, -1], [9.5, -1], [9.5, -2]
    ]),
}

# Label positions (centre of each region)
label_positions = {
    'WA':  (2.0, 5.5),
    'NT':  (5.5, 8.5),
    'SA':  (5.2, 3.0),
    'QLD': (9.0, 8.0),
    'NSW': (9.0, 4.0),
    'VIC': (8.0, 1.5),
    'TAS': (8.75, -1.5),
}

colour_map = {
    'Blue':  '#4A90D9',
    'Red':   '#E05A5A',
    'Green': '#5DBB63'
}

# ─────────────────────────────────────────────
# DRAW THE MAP
# ─────────────────────────────────────────────

fig, ax = plt.subplots(figsize=(11, 9))
ax.set_xlim(-0.5, 12)
ax.set_ylim(-3, 12.5)
ax.set_aspect('equal')
ax.axis('off')
ax.set_facecolor('#AED6F1')  # Light blue ocean background
fig.patch.set_facecolor('#AED6F1')

for region, shape in region_shapes.items():
    colour = solution[region]
    face_colour = colour_map[colour]

    polygon = Polygon(shape, closed=True,
                      facecolor=face_colour,
                      edgecolor='black',
                      linewidth=2,
                      alpha=0.9)
    ax.add_patch(polygon)

    # Label
    lx, ly = label_positions[region]
    ax.text(lx, ly, f"{region}\n({colour})",
            ha='center', va='center',
            fontsize=10, fontweight='bold',
            color='white',
            bbox=dict(boxstyle='round,pad=0.2',
                      facecolor='none',
                      edgecolor='none'))

# Legend
legend_patches = [
    mpatches.Patch(color='#4A90D9', label='Blue'),
    mpatches.Patch(color='#E05A5A', label='Red'),
    mpatches.Patch(color='#5DBB63', label='Green'),
]
ax.legend(handles=legend_patches, loc='lower left',
          fontsize=12, title="Colours Used",
          title_fontsize=12,
          framealpha=0.9)

plt.title(
    "Australia Map Colouring — CSP Solution\n"
    "No two adjacent regions share the same colour",
    fontsize=14, fontweight='bold', pad=15
)

plt.tight_layout()
plt.savefig('australia_map.png', dpi=150, bbox_inches='tight')
print("\nMap saved as australia_map.png")
plt.show()
