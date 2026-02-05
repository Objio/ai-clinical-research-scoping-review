# -*- coding: utf-8 -*-
"""
FIGURAS DE PUBLICACIÓN - TESIS DOCTORAL
========================================
AI in Clinical Research Scoping Review (2023-2025)

DATOS REALES extraídos de: Scoping_Review_IA_Clinica_MEJORADO.docx
Manuscrito revisado por: José Xavier Barber (Asesor de Tesis)
Universidad Miguel Hernández, Elche, España

Autor: Gilberto Objío Subero
Fecha: Febrero 2026
"""

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import numpy as np
import os

# Configuración de estilo para publicación científica
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams.update({
    'figure.figsize': (12, 8),
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'font.size': 11,
    'font.family': 'serif',
    'axes.labelsize': 12,
    'axes.titlesize': 14,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 9,
    'figure.titlesize': 16
})

# Directorio de salida
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
FIGURES_DIR = os.path.join(OUTPUT_DIR, 'figures_publication_real')
os.makedirs(FIGURES_DIR, exist_ok=True)

print("="*70)
print("FIGURAS DE PUBLICACIÓN - TESIS DOCTORAL")
print("Datos verificados del manuscrito revisado por José Xavier Barber")
print("="*70 + "\n")

# =============================================================================
# DATOS REALES - TABLA 1 DEL MANUSCRITO (VERIFICADOS)
# =============================================================================
# Fuente: Scoping_Review_IA_Clinica_MEJORADO (1).docx
# Total: 8,395 documentos con texto válido para clustering

CLUSTER_DATA = {
    'names': [
        'General ML/DL',
        'AI in Clinical Care',
        'ML Classification Systems',
        'Clinical Studies (Retrospective)',
        'Healthcare Security & Federated',
        'Cardiovascular Risk',
        'EHR Analytics',
        'NLP & LLMs',
        'Cancer Genomics',
        'MRI Imaging',
        'Deep Neural Networks',
        'Medical Image Segmentation',
        'CT Radiomics',
        'Drug Discovery',
        'Breast Cancer Imaging'
    ],
    'n': [1332, 903, 698, 691, 644, 549, 481, 458, 457, 447, 439, 424, 381, 278, 213],
    'pct': [15.9, 10.8, 8.3, 8.2, 7.7, 6.5, 5.7, 5.5, 5.4, 5.3, 5.2, 5.1, 4.5, 3.3, 2.5],
    'y2023': [322, 207, 150, 105, 129, 112, 102, 70, 107, 99, 83, 115, 56, 61, 51],
    'y2025': [543, 418, 276, 341, 301, 255, 207, 238, 198, 187, 192, 180, 184, 115, 89],
    'growth': [69, 102, 84, 225, 133, 128, 103, 240, 85, 89, 131, 57, 229, 89, 75]
}

TOTAL_N = sum(CLUSTER_DATA['n'])
print(f"✓ Total documentos: {TOTAL_N:,} (verificado: 8,395)")

# =============================================================================
# FIGURA 1: DISTRIBUCIÓN DE CLUSTERS (BARRAS HORIZONTALES)
# =============================================================================
def fig1_cluster_distribution():
    """Gráfico de barras horizontales con N por cluster."""
    fig, ax = plt.subplots(figsize=(12, 9))
    
    names = CLUSTER_DATA['names'][::-1]  # Invertir para mayor arriba
    n_values = CLUSTER_DATA['n'][::-1]
    pct_values = CLUSTER_DATA['pct'][::-1]
    
    colors = plt.cm.viridis(np.linspace(0.2, 0.9, len(names)))[::-1]
    
    bars = ax.barh(range(len(names)), n_values, color=colors, edgecolor='white', linewidth=0.5)
    
    ax.set_yticks(range(len(names)))
    ax.set_yticklabels(names)
    ax.set_xlabel('Número de documentos (N)')
    ax.set_title('Figura 1. Distribución de documentos por clúster temático\n(N = 8,395 documentos, período 2023-2025)', 
                 fontweight='bold', pad=15)
    
    # Etiquetas con N y %
    for i, (bar, n, pct) in enumerate(zip(bars, n_values, pct_values)):
        ax.text(bar.get_width() + 20, bar.get_y() + bar.get_height()/2, 
                f'{n:,} ({pct}%)', va='center', fontsize=9)
    
    ax.set_xlim(0, max(n_values) * 1.15)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    plt.tight_layout()
    filepath = os.path.join(FIGURES_DIR, 'fig1_distribucion_clusters.png')
    plt.savefig(filepath, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"✓ Figura 1 guardada: {filepath}")

# =============================================================================
# FIGURA 2: EVOLUCIÓN TEMPORAL 2023 vs 2025
# =============================================================================
def fig2_temporal_evolution():
    """Gráfico de barras agrupadas comparando 2023 vs 2025."""
    fig, ax = plt.subplots(figsize=(14, 8))
    
    names = CLUSTER_DATA['names']
    y2023 = CLUSTER_DATA['y2023']
    y2025 = CLUSTER_DATA['y2025']
    
    x = np.arange(len(names))
    width = 0.38
    
    bars1 = ax.bar(x - width/2, y2023, width, label='2023', color='#3182bd', edgecolor='white')
    bars2 = ax.bar(x + width/2, y2025, width, label='2025', color='#31a354', edgecolor='white')
    
    ax.set_xlabel('Clúster temático')
    ax.set_ylabel('Número de publicaciones')
    ax.set_title('Figura 2. Evolución temporal de publicaciones por clúster (2023 vs 2025)', 
                 fontweight='bold', pad=15)
    ax.set_xticks(x)
    ax.set_xticklabels(names, rotation=45, ha='right', fontsize=9)
    ax.legend(loc='upper right')
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    plt.tight_layout()
    filepath = os.path.join(FIGURES_DIR, 'fig2_evolucion_temporal.png')
    plt.savefig(filepath, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"✓ Figura 2 guardada: {filepath}")

# =============================================================================
# FIGURA 3: CRECIMIENTO PORCENTUAL POR CLUSTER
# =============================================================================
def fig3_growth_rate():
    """Gráfico de barras con % de crecimiento."""
    fig, ax = plt.subplots(figsize=(14, 7))
    
    # Ordenar por crecimiento
    sorted_indices = np.argsort(CLUSTER_DATA['growth'])[::-1]
    names = [CLUSTER_DATA['names'][i] for i in sorted_indices]
    growth = [CLUSTER_DATA['growth'][i] for i in sorted_indices]
    
    # Colores: destacar los de mayor crecimiento
    colors = ['#e31a1c' if g >= 200 else '#fd8d3c' if g >= 100 else '#3182bd' for g in growth]
    
    bars = ax.bar(range(len(names)), growth, color=colors, edgecolor='white', linewidth=0.5)
    
    ax.set_xticks(range(len(names)))
    ax.set_xticklabels(names, rotation=45, ha='right', fontsize=9)
    ax.set_ylabel('Crecimiento (%)')
    ax.set_title('Figura 3. Tasa de crecimiento por clúster temático (2023-2025)\nOrdenado de mayor a menor crecimiento', 
                 fontweight='bold', pad=15)
    
    # Etiquetas de %
    for bar, g in zip(bars, growth):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5, 
                f'+{g}%', ha='center', va='bottom', fontsize=9, fontweight='bold')
    
    # Leyenda de colores
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor='#e31a1c', label='Crecimiento ≥200%'),
        Patch(facecolor='#fd8d3c', label='Crecimiento ≥100%'),
        Patch(facecolor='#3182bd', label='Crecimiento <100%')
    ]
    ax.legend(handles=legend_elements, loc='upper right')
    
    ax.set_ylim(0, max(growth) * 1.15)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    plt.tight_layout()
    filepath = os.path.join(FIGURES_DIR, 'fig3_crecimiento_clusters.png')
    plt.savefig(filepath, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"✓ Figura 3 guardada: {filepath}")

# =============================================================================
# FIGURA 4: TOP 3 CLUSTERS DE MAYOR CRECIMIENTO (DESTACADO)
# =============================================================================
def fig4_top_growth():
    """Gráfico destacando los 3 clusters de mayor crecimiento."""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Top 3 por crecimiento
    top_clusters = [
        ('NLP & LLMs', 70, 238, 240),
        ('CT Radiomics', 56, 184, 229),
        ('Clinical Studies (Retrospective)', 105, 341, 225)
    ]
    
    names = [t[0] for t in top_clusters]
    y2023 = [t[1] for t in top_clusters]
    y2025 = [t[2] for t in top_clusters]
    growth = [t[3] for t in top_clusters]
    
    x = np.arange(len(names))
    width = 0.35
    
    bars1 = ax.bar(x - width/2, y2023, width, label='2023', color='#9ecae1')
    bars2 = ax.bar(x + width/2, y2025, width, label='2025', color='#de2d26')
    
    ax.set_ylabel('Número de publicaciones')
    ax.set_title('Figura 4. Clústeres de mayor crecimiento (2023-2025)\nTop 3 áreas emergentes en IA clínica', 
                 fontweight='bold', pad=15)
    ax.set_xticks(x)
    ax.set_xticklabels(names, fontsize=10)
    ax.legend(loc='upper left')
    
    # Anotar crecimiento
    for i, (bar2, g) in enumerate(zip(bars2, growth)):
        ax.annotate(f'+{g}%', 
                   xy=(bar2.get_x() + bar2.get_width()/2, bar2.get_height()),
                   xytext=(0, 10), textcoords='offset points',
                   ha='center', fontsize=12, fontweight='bold', color='#de2d26')
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    plt.tight_layout()
    filepath = os.path.join(FIGURES_DIR, 'fig4_top_crecimiento.png')
    plt.savefig(filepath, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"✓ Figura 4 guardada: {filepath}")

# =============================================================================
# TABLA RESUMEN (EXPORTADA COMO IMAGEN)
# =============================================================================
def table_summary():
    """Genera tabla resumen como imagen."""
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.axis('off')
    
    # Datos para la tabla
    headers = ['Clúster', 'N', '%', '2023', '2025', 'Crecimiento']
    cell_data = []
    for i in range(len(CLUSTER_DATA['names'])):
        row = [
            CLUSTER_DATA['names'][i],
            f"{CLUSTER_DATA['n'][i]:,}",
            f"{CLUSTER_DATA['pct'][i]}%",
            str(CLUSTER_DATA['y2023'][i]),
            str(CLUSTER_DATA['y2025'][i]),
            f"+{CLUSTER_DATA['growth'][i]}%"
        ]
        cell_data.append(row)
    
    # Añadir total
    cell_data.append(['TOTAL', f"{TOTAL_N:,}", '100%', 
                      str(sum(CLUSTER_DATA['y2023'])),
                      str(sum(CLUSTER_DATA['y2025'])), '—'])
    
    table = ax.table(cellText=cell_data, colLabels=headers,
                     loc='center', cellLoc='center',
                     colColours=['#3182bd']*6)
    
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.8)
    
    # Estilo de encabezados
    for i in range(len(headers)):
        table[(0, i)].set_text_props(color='white', fontweight='bold')
    
    ax.set_title('Tabla 1. Distribución de documentos por clúster temático\n(Datos verificados del manuscrito)', 
                 fontsize=14, fontweight='bold', pad=20)
    
    plt.tight_layout()
    filepath = os.path.join(FIGURES_DIR, 'tabla1_resumen.png')
    plt.savefig(filepath, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"✓ Tabla 1 guardada: {filepath}")

# =============================================================================
# EJECUCIÓN PRINCIPAL
# =============================================================================
if __name__ == "__main__":
    try:
        fig1_cluster_distribution()
        fig2_temporal_evolution()
        fig3_growth_rate()
        fig4_top_growth()
        table_summary()
        
        print("\n" + "="*70)
        print("✅ TODAS LAS FIGURAS GENERADAS EXITOSAMENTE")
        print(f"📁 Ubicación: {FIGURES_DIR}")
        print("="*70)
        
        print("\n⚠️  VERIFICACIÓN REQUERIDA ANTES DE USAR EN TESIS:")
        print("   1. Revisar cada figura visualmente")
        print("   2. Confirmar que los valores coinciden con el manuscrito")
        print("   3. Verificar formato y etiquetas")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
