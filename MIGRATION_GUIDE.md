# Migration Guide: Removing OpenMC Dependency

**Date:** October 23, 2025
**Status:** ✅ Complete

## Summary of Changes

This guide documents the changes made to remove the OpenMC dependency from the ML4ND tutorial series, making the project more accessible to students on all platforms (especially Windows users who would have needed Docker).

---

## Why This Change?

### Problem:
- **OpenMC requires Docker on Windows** - Complex setup for students
- **Installation barriers** - Reduced accessibility
- **Not essential** - Tutorials can use simpler data access methods

### Solution:
- **Use JANIS web interface** - Easy CSV export
- **Direct data downloads** - From official sources (NNDC, IAEA)
- **Cross-platform friendly** - Works on Windows, Mac, Linux
- **Simpler workflow** - Download CSV → Load in Python → Visualize

---

## What Changed?

### 1. Tutorial 1: ENDF Data ✅ MAJOR UPDATE

**Before:**
```python
import openmc
import openmc.data
u235 = openmc.data.IncidentNeutron.from_endf(endf_file)
xs = u235[18].xs['0K'](energy)
```

**After:**
```python
# Method A: Download CSV from JANIS (Recommended)
# 1. Go to https://www.oecd-nea.org/janisweb/
# 2. Select U-235, reaction (n,f), library ENDF/B-VIII.0
# 3. Export to CSV
# 4. Load with pandas
df = pd.read_csv('u235_fission_janis.csv')
```

**Key Improvements:**
- ✓ Added JANIS web interface method (step-by-step instructions)
- ✓ Sample data generation for demonstration
- ✓ Clear instructions for downloading real data
- ✓ Enhanced visualizations with annotations
- ✓ No OpenMC dependency

**Files Modified:**
- `tutorials/01_ENDF_Data.ipynb` - Complete rewrite

---

### 2. Tutorial 2: EXFOR Data ✅ NO CHANGES NEEDED

**Status:** Already OpenMC-free!

The EXFOR tutorial already used:
- Direct API access with `requests`
- Simulated experimental data
- Clear instructions for IAEA website downloads

**No changes required.**

---

### 3. Tutorial 3: TENDL Data ✅ MINOR FIX ONLY

**Status:** Already OpenMC-free (typo fixed previously)

The TENDL tutorial already used:
- Simulated TENDL-like data
- Manual download instructions
- No OpenMC dependency

**Changes:**
- Fixed typo: `kernelnel` → `kernelspec` (metadata)

---

### 4. Tutorial 4: JANIS API ✅ NO CHANGES NEEDED

**Status:** Already OpenMC-free!

The JANIS tutorial already focused on:
- Web interface CSV export
- Multi-library comparison
- No parsing of raw ENDF files

**No changes required.**

---

### 5. Requirements.txt ✅ UPDATED

**Removed:**
```python
# Nuclear data packages
openmc>=0.13.0
```

**Current Dependencies:**
- Core: numpy, scipy, pandas, matplotlib
- Web: requests, beautifulsoup4, lxml
- Jupyter: jupyter, ipykernel, notebook
- ML (optional): scikit-learn, tensorflow, torch
- Viz: seaborn, plotly
- Utils: h5py, tables, tqdm

**All packages are standard pip-installable, no Docker required!**

---

### 6. README.md ✅ UPDATED

**Changes:**
- Updated Tutorial 1 description
- Removed OpenMC references
- Emphasized JANIS workflow
- Highlighted "no Docker needed"
- Updated duration estimates

---

### 7. Introduction Tutorial ✅ NO CHANGES NEEDED

The introduction (Tutorial 0) never used OpenMC, only numpy and matplotlib for basic demonstrations.

---

## Student Impact

### ✅ Benefits:

1. **Easier Setup**
   - No Docker installation required
   - Works natively on Windows
   - Standard pip install only

2. **Faster Start**
   - Download CSV from web interface
   - Load with pandas immediately
   - Start visualizing in minutes

3. **More Intuitive**
   - Web interface is visual and interactive
   - See data before downloading
   - Compare libraries side-by-side in browser

4. **Better Learning**
   - Focus on physics, not installation
   - Understand data sources directly
   - Real workflow for data validation

### ⚠️ Trade-offs:

1. **Manual Steps**
   - Need to use web browser for downloads
   - Not fully programmatic (but more practical)

2. **File Management**
   - Students must organize downloaded CSVs
   - File paths must be updated in notebooks

**Mitigation:** Clear instructions, standardized file locations, sample data fallback

---

## Migration Instructions for Existing Users

If you were using the old tutorials with OpenMC:

### Step 1: Update Repository
```bash
git pull origin main
```

### Step 2: Update Python Environment
```bash
# Remove OpenMC
pip uninstall openmc

# Verify requirements
pip install -r requirements.txt
```

### Step 3: Download Data from JANIS
1. Visit https://www.oecd-nea.org/janisweb/
2. Follow instructions in Tutorial 1
3. Save CSVs to `data/endf/` directory

### Step 4: Update Notebook Paths
If you have custom notebooks, update file paths:
```python
# Old
u235 = openmc.data.IncidentNeutron.from_endf(endf_file)

# New
df = pd.read_csv(data_dir / 'u235_fission_janis.csv')
```

---

## Testing Status

All tutorials have been tested with the new workflow:

| Tutorial | Status | Notes |
|----------|--------|-------|
| 00_Introduction | ✓ Pass | No changes |
| 01_ENDF_Data | ✓ Pass | Full rewrite, tested |
| 02_EXFOR_Data | ✓ Pass | No changes needed |
| 03_TENDL_Data | ✓ Pass | Typo fixed |
| 04_JANIS_API | ✓ Pass | No changes needed |

**Test Results:**
- All notebooks have valid JSON structure
- All code cells have valid Python syntax
- All imports are available (except sample data packages)
- Execution tests pass
- Requirements.txt is complete

---

## Recommended Workflow for Students

### For ENDF Data (Tutorial 1):

1. **Download from JANIS:**
   ```
   Website: https://www.oecd-nea.org/janisweb/
   Steps:
     1. Click "Search" → "Cross Sections"
     2. Select isotope (e.g., U-235)
     3. Select reaction (e.g., (n,f) for fission)
     4. Check ENDF/B-VIII.0 library
     5. Click "Plot Data"
     6. Click "Export" → "CSV"
     7. Save to data/endf/u235_fission_janis.csv
   ```

2. **Load in Python:**
   ```python
   import pandas as pd
   df = pd.read_csv('data/endf/u235_fission_janis.csv')
   ```

3. **Visualize:**
   ```python
   import matplotlib.pyplot as plt
   plt.loglog(df['Energy_eV'], df['CrossSection_barns'])
   plt.show()
   ```

### For EXFOR Data (Tutorial 2):

1. **Download from IAEA:**
   ```
   Website: https://www-nds.iaea.org/exfor/
   Search for: Target="92-U-235", Reaction="(N,F)"
   Download: CSV format
   Save to: data/exfor/
   ```

2. **Use sample data for learning** (provided in tutorial)

3. **Compare with ENDF** (from Tutorial 1)

---

## Alternative: Advanced Users

For advanced users who want programmatic access:

### Option 1: Use endf-parserpy (Pure Python)
```bash
pip install endf-parserpy
```
```python
from endf_parserpy import EndfParser
parser = EndfParser()
endf_dict = parser.parsefile('n-092_U_235.endf')
```

### Option 2: Use x4i3 for EXFOR
```bash
pip install x4i3
```
```python
import x4i3
results = x4i3.search(target='U-235', reaction='(n,f)')
```

**Note:** These are optional and not required for the tutorials.

---

## FAQ

**Q: Do I need to install Docker?**
A: No! That's the whole point of these changes.

**Q: Can I still use OpenMC if I want to?**
A: Yes, but it's not covered in these tutorials. These tutorials focus on data access and visualization.

**Q: Is the data quality different?**
A: No! JANIS provides the same ENDF/B-VIII.0 data, just in a more accessible format.

**Q: What if I can't access JANIS website?**
A: The tutorials include sample data. You can also download directly from NNDC: https://www.nndc.bnl.gov/endf/

**Q: Will this affect my machine learning work?**
A: No! The CSV data is perfect for ML. Actually easier to work with than ENDF binary format.

---

## Support

If you encounter issues with the new workflow:

1. **Check Tutorial 1** - Detailed step-by-step instructions
2. **Try sample data first** - Included in all tutorials
3. **Verify file paths** - Use absolute paths or Path() objects
4. **Check internet connection** - Required for JANIS downloads
5. **Ask your instructor** - They can demonstrate JANIS interface

---

## Conclusion

The removal of OpenMC simplifies the tutorial series while maintaining full functionality for nuclear data visualization and machine learning preparation. Students can now start learning immediately without complex setup procedures.

**Summary:**
- ✅ Simpler installation
- ✅ Cross-platform compatibility
- ✅ Faster start time
- ✅ Better learning focus
- ✅ Same data quality
- ✅ Ready for machine learning

**Status:** Production ready for student use!

---

**Questions or Feedback?**
Open an issue at: https://github.com/WHopkins-git/ML4ND/issues
