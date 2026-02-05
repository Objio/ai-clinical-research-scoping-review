# AI in Clinical Research: A Computational Scoping Review (2023-2025)

[![DOI](https://img.shields.io/badge/DOI-10.xxxx%2Fzenodo.xxxxx-blue)](https://doi.org/10.xxxx/zenodo.xxxxx)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

## Overview

Computational scoping review analyzing **8,395 scientific documents** on Artificial Intelligence in Clinical Research, following JBI and PRISMA-ScR guidelines.

**Author:** Gilberto Objío Subero  
**Thesis Advisor:** José Xavier Barber  
**Institution:** Universidad Miguel Hernández, Elche, España  
**Period:** 2023-2025

## Key Findings

| Metric | Value |
|--------|-------|
| Documents analyzed | 8,395 |
| Clusters identified (K-Means) | 15 |
| Top growth: NLP & LLMs | +240% |
| Top growth: CT Radiomics | +229% |

## Repository Structure

```
├── analysis/
│   └── AIReviewer_Scientific_Text_Analysis.ipynb  # Main analysis notebook
├── figures/
│   ├── fig1_distribucion_clusters.png
│   ├── fig2_evolucion_temporal.png
│   ├── fig3_crecimiento_clusters.png
│   ├── fig4_top_crecimiento.png
│   └── tabla1_resumen.png
├── scripts/
│   └── generate_figures_real_data.py  # Figure generation script
├── data/
│   └── README.md  # Data access instructions
├── manuscript/
│   ├── Scoping_Review_IA_Clinica_MEJORADO.docx
│   └── Material_Suplementario_PRISMA_ScR.docx
└── README.md
```

## Methodology

1. **Data Collection**: Scopus database search (2023-2025)
2. **Text Processing**: NLP preprocessing and embedding generation
3. **Clustering**: K-Means algorithm (k=15)
4. **Analysis**: Temporal evolution and growth rate calculation

## Requirements

```bash
pip install -r requirements.txt
```

Key dependencies:
- Python 3.9+
- pandas, numpy
- scikit-learn
- matplotlib, seaborn
- python-docx

## Reproducibility

To regenerate the publication figures:

```bash
python scripts/generate_figures_real_data.py
```

## Citation

```bibtex
@article{objio2026ai_clinical,
  title={AI in Clinical Research: A Computational Scoping Review (2023-2025)},
  author={Objío Subero, Gilberto},
  journal={[Journal Name]},
  year={2026}
}
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

- **Author**: Gilberto Objío Subero
- **Email**: [your.email@institution.edu]
- **ORCID**: [0000-0000-0000-0000]
