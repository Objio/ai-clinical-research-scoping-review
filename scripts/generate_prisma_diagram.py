# -*- coding: utf-8 -*-
"""
PRISMA-ScR Flow Diagram Generator
PhD Thesis: AI in Clinical Research Scoping Review
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import os

def create_prisma_diagram():
    """Generate PRISMA 2020 flow diagram for scoping review."""
    
    fig, ax = plt.subplots(figsize=(12, 14))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 140)
    ax.axis('off')
    
    # Colors
    blue = '#3182bd'
    gray = '#969696'
    green = '#31a354'
    
    # Helper function to draw boxes
    def draw_box(x, y, w, h, text, color=blue, fontsize=9):
        box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02",
                             facecolor='white', edgecolor=color, linewidth=2)
        ax.add_patch(box)
        ax.text(x + w/2, y + h/2, text, ha='center', va='center',
                fontsize=fontsize, wrap=True)
    
    # IDENTIFICATION
    ax.text(5, 135, 'IDENTIFICATION', fontsize=11, fontweight='bold', color=gray)
    draw_box(15, 120, 30, 12, 'Records identified\nfrom Scopus\n(n = 8,522)')
    draw_box(55, 120, 30, 12, 'Duplicate records\nremoved\n(n = 0)')
    
    # Arrow down
    ax.annotate('', xy=(30, 118), xytext=(30, 120),
                arrowprops=dict(arrowstyle='->', color=blue, lw=2))
    
    # SCREENING
    ax.text(5, 108, 'SCREENING', fontsize=11, fontweight='bold', color=gray)
    draw_box(15, 93, 30, 12, 'Records screened\n(n = 8,522)')
    draw_box(55, 93, 30, 12, 'Records excluded:\nNo valid abstract\n(n = 127)')
    
    # Arrow
    ax.annotate('', xy=(45, 99), xytext=(55, 99),
                arrowprops=dict(arrowstyle='->', color=gray, lw=1.5))
    ax.annotate('', xy=(30, 91), xytext=(30, 93),
                arrowprops=dict(arrowstyle='->', color=blue, lw=2))
    
    # ELIGIBILITY
    ax.text(5, 81, 'ELIGIBILITY', fontsize=11, fontweight='bold', color=gray)
    draw_box(15, 66, 30, 12, 'Full-text articles\nassessed\n(n = 8,395)')
    draw_box(55, 66, 30, 12, 'Articles excluded:\nNon-English (n=0)\nNon-research (n=0)')
    
    # Arrow
    ax.annotate('', xy=(45, 72), xytext=(55, 72),
                arrowprops=dict(arrowstyle='->', color=gray, lw=1.5))
    ax.annotate('', xy=(30, 64), xytext=(30, 66),
                arrowprops=dict(arrowstyle='->', color=blue, lw=2))
    
    # INCLUDED
    ax.text(5, 54, 'INCLUDED', fontsize=11, fontweight='bold', color=green)
    draw_box(15, 39, 30, 12, 'Studies included\nin analysis\n(n = 8,395)', color=green)
    
    # Arrow down
    ax.annotate('', xy=(30, 37), xytext=(30, 39),
                arrowprops=dict(arrowstyle='->', color=green, lw=2))
    
    # CLUSTERING
    draw_box(15, 20, 70, 14, 
             'K-Means Clustering (k=15)\n\n'
             'Top clusters: General ML/DL (n=1,332), AI in Clinical Care (n=903)\n'
             'Highest growth: NLP & LLMs (+240%), CT Radiomics (+229%)',
             color=green, fontsize=8)
    
    # Title
    ax.text(50, 138, 'PRISMA-ScR Flow Diagram', ha='center', fontsize=14, fontweight='bold')
    ax.text(50, 136, 'AI in Clinical Research Scoping Review (2023-2025)', 
            ha='center', fontsize=10, style='italic')
    
    # Footer
    ax.text(50, 5, 'From: Objío Subero G. et al. (2026)', ha='center', fontsize=8, color=gray)
    
    plt.tight_layout()
    
    # Save
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures')
    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, 'prisma_flow.png')
    plt.savefig(filepath, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"✓ PRISMA diagram saved: {filepath}")
    return filepath

if __name__ == "__main__":
    create_prisma_diagram()
