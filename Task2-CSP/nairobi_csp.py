"""
CCS 2226 - Foundations of Artificial Intelligence
Task Two - Constraint Satisfaction Problem (CSP)
Part b - Colour Nairobi 17 Sub-Counties

Goal: Use the LEAST possible number of colours
Rule: No two adjacent sub-counties can share the same colour
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Polygon
import numpy as np

# ─────────────────────────────────────────────
# NAIROBI 17 SUB-COUNTIES AND THEIR BORDERS
# ─────────────────────────────────────────────

nairobi = {
    'Westlands':        ['Roysambu', 'Kasarani', 'Starehe', 'Dagoretti North'],
    'Dagoretti North':  ['Westlands', 'Dagoretti South', 'Kibra', 'Starehe'],
    'Dagoretti South':  ['Dagoretti North', 'Kibra', 'Langata'],
    'Langata':          ['Dagoretti South', 'Kibra', 'Embakasi West'],
    'Kibra':            ['Dagoretti North', 'Dagoretti South', 'Langata', 'Starehe', 'Embakasi West'],
    'Roysambu':         ['Westlands', 'Kasarani', 'Mathare'],
    'Kasarani':         ['Westlands', 'Roysambu', 'Mathare', 'Ruaraka', 'Embakasi North'],
    'Ruaraka':          ['Kasarani', 'Mathare', 'Embakasi North', 'Makadara'],
    'Embakasi North':   ['Kasarani', 'Ruaraka', 'Embakasi Central', 'Embakasi East'],
    'Embakasi Central': ['Embakasi North', 'Embakasi East', 'Embakasi South', 'Embakasi West', 'Makadara'],
    'Embakasi East':    ['Embakasi North', 'Embakasi Central', 'Embakasi South'],
    'Embakasi South':   ['Embakasi Central', 'Embakasi East', 'Embakasi West'],
    'Embakasi West':    ['Langata', 'Kibra', 'Embakasi Central', 'Embakasi South', 'Makadara'],
    'Makadara':         ['Ruaraka', 'Embakasi Central', 'Embakasi West', 'Kamukunji', 'Starehe'],
    'Kamukunji':        ['Makadara', 'Starehe', 'Mathare'],
    'Starehe':          ['Westlands', 'Dagoretti North', 'Kibra', 'Makadara', 'Kamukunji', 'Mathare'],
    'Mathare':          ['Roysambu', 'Kasarani', 'Ruaraka', 'Kamukunji', 'Starehe'],
}

# ─────────────────────────────────────────────
# CSP SOLVER - TRY WITH MINIMUM COLOURS
# ─────────────────────────────────────────────

def is_valid(region, colour, assignment):
    for neighbour in nairobi[region]:
        if neighbour in assignment and assignment[neighbour] == colour:
            return False
    return True

def backtrack(assignment, colours):
    if len(assignment) == len(nairobi):
        return assignment
    unassigned = [r for r in nairobi if r not in assignment]
    region = unassigned[0]
    for colour in colours:
        if is_valid(region, colour, assignment):
            assignment[region] = colour
            result = backtrack(assignment, colours)
            if result is not None:
                return result
            del assignment[region]
    return None

# Try increasing number of colours until a solution is found
print("="*55)
print("  CSP - Nairobi Sub-Counties Map Colouring")
print("  Rule: No two adjacent sub-counties same colour")
print("  Goal: Use the LEAST possible number of colours")
print("="*55)

all_colours = ['Red', 'Blue', 'Green', 'Yellow', 'Orange']
solution = None
colours_used = None

for num_colours in range(2, len(all_colours) + 1):
    colours = all_colours[:num_colours]
    print(f"\nTrying with {num_colours} colours: {colours}...")
    result = backtrack({}, colours)
    if result is not None:
        solution = result
        colours_used = colours
        print(f"Solution found with {num_colours} colours!")
        break
    else:
        print(f"Not possible with {num_colours} colours.")

# ─────────────────────────────────────────────
# PRINT SOLUTION
# ─────────────────────────────────────────────

print("\n" + "="*55)
print(f"MINIMUM COLOURS NEEDED: {len(colours_used)}")
print("="*55)
print(f"\n{'Sub-County':<25} {'Colour'}")
print("-"*40)
for region, colour in solution.items():
    print(f"{region:<25} {colour}")

# ─────────────────────────────────────────────
# VISUAL MAP - GRID LAYOUT
# ─────────────────────────────────────────────

# Grid positions (col, row) for each sub-county
positions = {
    'Roysambu':         (1, 4),
    'Westlands':        (0, 3),
    'Kasarani':         (2, 4),
    'Mathare':          (2, 3),
    'Ruaraka':          (3, 4),
    'Dagoretti North':  (0, 2),
    'Starehe':          (1, 3),
    'Kamukunji':        (2, 2),
    'Embakasi North':   (3, 3),
    'Dagoretti South':  (0, 1),
    'Kibra':            (1, 2),
    'Makadara':         (2, 2.8),
    'Embakasi Central': (3, 2),
    'Embakasi East':    (4, 3),
    'Langata':          (0, 0),
    'Embakasi West':    (2, 1),
    'Embakasi South':   (3, 1),
}

colour_map = {
    'Red':    '#E05A5A',
    'Blue':   '#4A90D9',
    'Green':  '#5DBB63',
    'Yellow': '#F4D03F',
    'Orange': '#E67E22',
}

fig, ax = plt.subplots(figsize=(13, 10))
ax.set_xlim(-0.8, 5.5)
ax.set_ylim(-0.8, 5.5)
ax.axis('off')
ax.set_facecolor('#F0F0F0')
fig.patch.set_facecolor('#F0F0F0')

box_w = 0.85
box_h = 0.55

for region, (cx, cy) in positions.items():
    colour = solution[region]
    fc = colour_map[colour]

    rect = mpatches.FancyBboxPatch(
        (cx - box_w/2, cy - box_h/2), box_w, box_h,
        boxstyle="round,pad=0.05",
        linewidth=1.5,
        edgecolor='black',
        facecolor=fc,
        alpha=0.9
    )
    ax.add_patch(rect)

    # Shorten long names for display
    display = region.replace('Embakasi ', 'Emb.\n').replace('Dagoretti ', 'Dag.\n')
    ax.text(cx, cy, display,
            ha='center', va='center',
            fontsize=7.5, fontweight='bold',
            color='white')

# Legend
legend_patches = [
    mpatches.Patch(color=colour_map[c], label=c)
    for c in colours_used
]
ax.legend(handles=legend_patches, loc='lower right',
          fontsize=11, title=f"Colours Used ({len(colours_used)} total)",
          title_fontsize=11, framealpha=0.9)

plt.title(
    f"Nairobi Sub-Counties CSP Colouring\n"
    f"Minimum colours needed: {len(colours_used)} — No two adjacent sub-counties share the same colour",
    fontsize=13, fontweight='bold', pad=15
)

plt.tight_layout()
plt.savefig('nairobi_map.png', dpi=150, bbox_inches='tight')
print("\nMap saved as nairobi_map.png")
plt.show()
