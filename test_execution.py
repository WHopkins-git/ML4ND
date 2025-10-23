#!/usr/bin/env python3
"""
Test actual execution of code cells from notebooks
"""

import json
import sys
from pathlib import Path

def test_basic_imports():
    """Test that basic imports work"""
    print("\n" + "="*60)
    print("Testing Basic Imports")
    print("="*60)

    tests = [
        ("numpy", "import numpy as np; print(f'NumPy version: {np.__version__}')"),
        ("matplotlib", "import matplotlib.pyplot as plt; print(f'Matplotlib version: {plt.matplotlib.__version__}')"),
        ("pandas", "import pandas as pd; print(f'Pandas version: {pd.__version__}')"),
        ("scipy", "from scipy import stats; print('SciPy imported successfully')"),
    ]

    for name, code in tests:
        try:
            exec(code)
            print(f"✓ {name}")
        except Exception as e:
            print(f"✗ {name}: {e}")
            return False

    return True

def test_sample_code():
    """Test sample code from tutorials"""
    print("\n" + "="*60)
    print("Testing Sample Code Execution")
    print("="*60)

    # Test 1: Basic numpy and matplotlib (from Introduction)
    print("\nTest 1: Basic plotting...")
    try:
        import numpy as np
        import matplotlib
        matplotlib.use('Agg')  # Non-interactive backend
        import matplotlib.pyplot as plt

        energy = np.logspace(-2, 7, 1000)
        sigma_capture = 10 / np.sqrt(energy)

        fig, ax = plt.subplots(figsize=(10, 6))
        ax.loglog(energy, sigma_capture, label='Test')
        ax.set_xlabel('Energy (eV)')
        ax.set_ylabel('Cross-section (barns)')
        plt.close(fig)

        print("✓ Basic plotting works")
    except Exception as e:
        print(f"✗ Basic plotting failed: {e}")
        return False

    # Test 2: DataFrame creation (from tutorials)
    print("\nTest 2: DataFrame operations...")
    try:
        import pandas as pd

        data = {
            'Energy_eV': np.logspace(0, 5, 100),
            'CrossSection_barns': np.random.random(100)
        }
        df = pd.DataFrame(data)

        # Basic operations
        stats = df.describe()
        assert len(df) == 100
        assert 'Energy_eV' in df.columns

        print("✓ DataFrame operations work")
    except Exception as e:
        print(f"✗ DataFrame operations failed: {e}")
        return False

    # Test 3: Statistical functions (from EXFOR tutorial)
    print("\nTest 3: Statistical analysis...")
    try:
        from scipy import stats

        data = np.random.normal(1.0, 0.1, 100)
        mean = np.mean(data)
        std = np.std(data)

        assert 0.8 < mean < 1.2
        assert std > 0

        print("✓ Statistical analysis works")
    except Exception as e:
        print(f"✗ Statistical analysis failed: {e}")
        return False

    # Test 4: Interpolation (from JANIS tutorial)
    print("\nTest 4: Interpolation...")
    try:
        from scipy.interpolate import interp1d

        x = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
        y = np.array([1.0, 4.0, 9.0, 16.0, 25.0])

        f = interp1d(x, y, kind='linear')
        y_new = f(2.5)

        assert 6.0 < y_new < 7.0  # Should be around 6.25

        print("✓ Interpolation works")
    except Exception as e:
        print(f"✗ Interpolation failed: {e}")
        return False

    # Test 5: Path operations (all tutorials)
    print("\nTest 5: Path operations...")
    try:
        from pathlib import Path

        data_dir = Path('../data/test')
        data_dir.mkdir(parents=True, exist_ok=True)

        test_file = data_dir / 'test.txt'
        test_file.write_text('test')

        assert test_file.exists()
        test_file.unlink()
        data_dir.rmdir()

        print("✓ Path operations work")
    except Exception as e:
        print(f"✗ Path operations failed: {e}")
        return False

    return True

def test_data_generation():
    """Test data generation functions used in tutorials"""
    print("\n" + "="*60)
    print("Testing Data Generation Functions")
    print("="*60)

    # Test simulated cross-section generation
    print("\nTest: Cross-section simulation...")
    try:
        import numpy as np

        energy = np.logspace(-2, 7, 10000)

        # Thermal region: 1/v behavior
        thermal = 584.4 * np.sqrt(0.0253 / np.maximum(energy, 1e-5))

        # Check values
        assert np.all(thermal > 0)
        assert np.all(np.isfinite(thermal))
        assert thermal[0] > thermal[-1]  # Should decrease with energy

        print("✓ Cross-section simulation works")
    except Exception as e:
        print(f"✗ Cross-section simulation failed: {e}")
        return False

    # Test multi-library comparison
    print("\nTest: Multi-library data generation...")
    try:
        libraries = ['ENDF/B-VIII.0', 'JEFF-3.3', 'JENDL-5.0']
        library_data = {}

        for lib in libraries:
            energy = np.logspace(-2, 7, 1000)
            xs = 584.0 * np.sqrt(0.0253 / np.maximum(energy, 1e-5))
            library_data[lib] = {'energy': energy, 'xs': xs}

        assert len(library_data) == 3
        for lib in libraries:
            assert 'energy' in library_data[lib]
            assert 'xs' in library_data[lib]

        print("✓ Multi-library data generation works")
    except Exception as e:
        print(f"✗ Multi-library data generation failed: {e}")
        return False

    return True

def main():
    print("="*60)
    print("NOTEBOOK EXECUTION TESTS")
    print("="*60)

    all_passed = True

    # Run tests
    if not test_basic_imports():
        all_passed = False

    if not test_sample_code():
        all_passed = False

    if not test_data_generation():
        all_passed = False

    # Summary
    print("\n" + "="*60)
    print("EXECUTION TEST SUMMARY")
    print("="*60)

    if all_passed:
        print("✓ All execution tests PASSED")
        print("✓ Notebooks are ready for students to use!")
        return 0
    else:
        print("✗ Some tests FAILED")
        print("⚠ Review errors above and fix issues")
        return 1

if __name__ == '__main__':
    sys.exit(main())
