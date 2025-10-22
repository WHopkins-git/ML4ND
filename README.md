# Machine Learning for Nuclear Data Validation

A comprehensive tutorial series for physics students exploring nuclear data and machine learning applications in the validation process.

## 📚 Overview

This project provides hands-on tutorials for downloading, visualizing, and analyzing neutron cross-section data from multiple nuclear databases. The tutorials are designed to help students understand nuclear data sources and prepare them for applying machine learning techniques to the validation process.

## 🎯 Learning Objectives

- Understand nuclear cross-sections and their importance
- Access and download data from major nuclear databases
- Visualize cross-section data across different energy ranges
- Compare evaluated libraries with experimental measurements
- Prepare datasets for machine learning applications

## 📂 Project Structure

```
ML4ND/
├── tutorials/               # Jupyter notebook tutorials
│   ├── 00_Introduction.ipynb
│   ├── 01_ENDF_Data.ipynb
│   ├── 02_EXFOR_Data.ipynb
│   ├── 03_TENDL_Data.ipynb
│   └── 04_JANIS_API.ipynb
├── data/                   # Downloaded nuclear data (created during tutorials)
│   ├── endf/
│   ├── exfor/
│   ├── tendl/
│   └── janis/
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Jupyter Notebook or JupyterLab
- Basic knowledge of Python and physics
- ~5 GB free disk space (for nuclear data files)

### Installation

1. **Clone or download this repository:**
   ```bash
   cd ML4ND
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch Jupyter:**
   ```bash
   jupyter notebook
   ```

5. **Navigate to the `tutorials/` directory and start with `00_Introduction.ipynb`**

## 📖 Tutorial Contents

### Tutorial 0: Introduction to Nuclear Cross-Sections
**File:** `00_Introduction.ipynb`

- What are nuclear cross-sections?
- Types of reactions (fission, capture, elastic scattering)
- Overview of nuclear data sources
- Why machine learning for validation?

**Duration:** 20-30 minutes

---

### Tutorial 1: ENDF (Evaluated Nuclear Data File)
**File:** `01_ENDF_Data.ipynb`

**Topics covered:**
- Understanding evaluated nuclear data
- Installing and using OpenMC
- Downloading ENDF/B-VIII.0 data
- Extracting cross-sections for different reactions
- Understanding MT numbers
- Comparing U-235 and U-238

**Key concepts:**
- Evaluated vs experimental data
- ENDF-6 format
- Resonance structure
- Fissile vs fissionable isotopes

**Duration:** 45-60 minutes

---

### Tutorial 2: EXFOR (Experimental Nuclear Reaction Data)
**File:** `02_EXFOR_Data.ipynb`

**Topics covered:**
- Accessing experimental measurements
- Using the IAEA EXFOR database
- Working with measurement uncertainties
- Comparing multiple experiments
- Comparing experimental data with evaluations

**Key concepts:**
- Experimental uncertainties
- Data validation
- Scatter between experiments
- Residual analysis

**Duration:** 45-60 minutes

---

### Tutorial 3: TENDL (TALYS-based Evaluated Nuclear Data Library)
**File:** `03_TENDL_Data.ipynb`

**Topics covered:**
- Automated vs manual evaluations
- Accessing TENDL data
- Comparing TENDL with ENDF
- Working with exotic isotopes
- Understanding evaluation uncertainties

**Key concepts:**
- Systematic evaluations
- Extended isotope coverage
- Uncertainty quantification
- Evaluation methodologies

**Duration:** 45-60 minutes

---

### Tutorial 4: JANIS (Multi-Library Access)
**File:** `04_JANIS_API.ipynb`

**Topics covered:**
- Accessing multiple libraries simultaneously
- Comparing ENDF, JEFF, JENDL, TENDL, CENDL
- Statistical analysis of library differences
- Using library spread for uncertainty estimation

**Key concepts:**
- Multi-library validation
- International cooperation in nuclear data
- Evaluation uncertainty
- Ensemble methods

**Duration:** 45-60 minutes

## 🗄️ Nuclear Data Sources

### Evaluated Libraries (Validated)
- **ENDF/B-VIII.0** (USA): https://www.nndc.bnl.gov/endf/
- **JEFF-3.3** (Europe): https://www.oecd-nea.org/dbdata/jeff/
- **JENDL-5.0** (Japan): https://wwwndc.jaea.go.jp/jendl/
- **TENDL-2021** (PSI/IAEA): https://tendl.web.psi.ch/

### Experimental Data
- **EXFOR** (IAEA): https://www-nds.iaea.org/exfor/

### Unified Access
- **JANIS** (OECD NEA): https://www.oecd-nea.org/janisweb/

## 🔬 Machine Learning Applications

These tutorials prepare data for various ML applications:

1. **Anomaly Detection**: Identify unusual patterns in experimental data
2. **Interpolation**: Predict cross-sections at unmeasured energies
3. **Uncertainty Quantification**: Estimate evaluation uncertainties
4. **Data Comparison**: Systematic comparison of experimental vs evaluated data
5. **Pattern Recognition**: Find systematic errors or trends
6. **Ensemble Methods**: Combine multiple evaluations

## 💡 Tips for Success

1. **Start with Tutorial 0**: It provides essential background
2. **Run cells sequentially**: Each notebook builds on previous cells
3. **Explore the data**: Modify parameters to test different isotopes
4. **Save your work**: Data downloads can take time
5. **Ask questions**: Nuclear data is complex - confusion is normal!

## 📊 Expected Outputs

Each tutorial generates:
- **Visualizations**: High-quality plots of cross-section data
- **Data files**: CSV files for further analysis
- **Comparisons**: Side-by-side library and experiment comparisons

All outputs are saved to the `data/` directory.

## 🛠️ Troubleshooting

### OpenMC installation issues
```bash
# If OpenMC fails to install, try:
conda install -c conda-forge openmc
```

### Data download issues
- Some databases require registration (free)
- Check your internet connection
- Use university network if available (better bandwidth)

### Memory issues
- Reduce the number of energy points in examples
- Close other applications
- Consider processing data in chunks

## 📚 Additional Resources

### Nuclear Physics
- "Introduction to Nuclear Engineering" - Lamarsh & Baratta
- "Nuclear Reactor Analysis" - Duderstadt & Hamilton

### Nuclear Data
- ENDF Format Manual: https://www.nndc.bnl.gov/endfdocs/
- IAEA Nuclear Data Services: https://www-nds.iaea.org/

### Machine Learning
- "Hands-On Machine Learning" - Aurélien Géron
- scikit-learn documentation: https://scikit-learn.org/

### Python for Science
- NumPy documentation: https://numpy.org/doc/
- Matplotlib tutorials: https://matplotlib.org/stable/tutorials/

## 🤝 Contributing

This is an educational project. If you find errors or have suggestions:
1. Document the issue clearly
2. Suggest improvements
3. Share interesting findings!

## 📧 Getting Help

If you encounter issues:
1. Check the troubleshooting section
2. Review the notebook markdown explanations
3. Consult the official documentation for each database
4. Ask your instructor or peers

## 🎓 Next Steps

After completing these tutorials, consider:
1. Exploring other isotopes (Pu-239, Fe-56, etc.)
2. Analyzing other reaction types (capture, elastic, inelastic)
3. Applying machine learning algorithms
4. Contributing to nuclear data evaluation efforts

## 📝 License

This educational material is provided for learning purposes.

Nuclear data accessed through these tutorials is subject to the respective database licenses:
- ENDF: Public domain
- EXFOR: IAEA open data
- TENDL: Free for research use
- JANIS: OECD NEA open access

## 🙏 Acknowledgments

- NNDC for ENDF data
- IAEA for EXFOR and nuclear data services
- PSI for TENDL
- OECD NEA for JANIS
- OpenMC development team
- Nuclear data evaluation community

## 📅 Version History

- **v1.0** (2025): Initial release with 5 comprehensive tutorials
  - Introduction to nuclear cross-sections
  - ENDF data access and visualization
  - EXFOR experimental data
  - TENDL automated evaluations
  - JANIS multi-library comparison

---

**Happy Learning! 🚀☢️🤖**

*Questions? Comments? Discoveries? Document your journey through nuclear data!*
