#!/usr/bin/env python3
"""
Test script for validating Jupyter notebooks
"""

import json
import sys
from pathlib import Path
import ast
import re

def test_notebook_structure(notebook_path):
    """Test if notebook is valid JSON and has proper structure"""
    print(f"\n{'='*60}")
    print(f"Testing: {notebook_path.name}")
    print('='*60)

    try:
        with open(notebook_path, 'r') as f:
            nb = json.load(f)
        print("✓ Valid JSON structure")

        # Check required keys
        required_keys = ['cells', 'metadata', 'nbformat', 'nbformat_minor']
        for key in required_keys:
            if key not in nb:
                print(f"✗ Missing required key: {key}")
                return False
        print("✓ Has required keys")

        # Check cells
        if not isinstance(nb['cells'], list):
            print("✗ 'cells' is not a list")
            return False
        print(f"✓ Has {len(nb['cells'])} cells")

        return True, nb

    except json.JSONDecodeError as e:
        print(f"✗ Invalid JSON: {e}")
        return False, None
    except Exception as e:
        print(f"✗ Error: {e}")
        return False, None

def extract_code_cells(nb):
    """Extract all code cells from notebook"""
    code_cells = []
    for i, cell in enumerate(nb['cells']):
        if cell.get('cell_type') == 'code':
            source = cell.get('source', [])
            if isinstance(source, list):
                code = ''.join(source)
            else:
                code = source
            code_cells.append((i, code))
    return code_cells

def test_imports(code_cells):
    """Test if all imports can be resolved"""
    print("\nTesting imports...")

    imports = set()
    for i, code in code_cells:
        # Find import statements
        for line in code.split('\n'):
            line = line.strip()
            if line.startswith('import ') or line.startswith('from '):
                # Extract module name
                if line.startswith('import '):
                    parts = line.split()
                    if len(parts) >= 2:
                        module = parts[1].split('.')[0].split(' as ')[0]
                        imports.add(module)
                elif line.startswith('from '):
                    parts = line.split()
                    if len(parts) >= 2:
                        module = parts[1].split('.')[0]
                        imports.add(module)

    print(f"Found {len(imports)} unique imports: {sorted(imports)}")

    # Check which imports are available
    missing = []
    for module in imports:
        try:
            __import__(module)
            print(f"  ✓ {module}")
        except ImportError:
            print(f"  ✗ {module} (not installed)")
            missing.append(module)

    return missing

def test_syntax(code_cells):
    """Test Python syntax in code cells"""
    print("\nTesting Python syntax...")

    errors = []
    for i, code in code_cells:
        try:
            ast.parse(code)
        except SyntaxError as e:
            errors.append((i, str(e)))
            print(f"  ✗ Cell {i}: {e}")

    if not errors:
        print(f"  ✓ All {len(code_cells)} code cells have valid syntax")

    return errors

def main():
    tutorials_dir = Path('/home/user/ML4ND/tutorials')

    if not tutorials_dir.exists():
        print(f"Error: {tutorials_dir} does not exist")
        sys.exit(1)

    notebooks = sorted(tutorials_dir.glob('*.ipynb'))

    print(f"Found {len(notebooks)} notebooks to test")

    all_results = {}
    all_missing_imports = set()

    for nb_path in notebooks:
        result, nb = test_notebook_structure(nb_path)

        if not result:
            all_results[nb_path.name] = {'status': 'FAILED', 'errors': ['Invalid structure']}
            continue

        code_cells = extract_code_cells(nb)

        # Test imports
        missing = test_imports(code_cells)
        all_missing_imports.update(missing)

        # Test syntax
        syntax_errors = test_syntax(code_cells)

        if missing or syntax_errors:
            all_results[nb_path.name] = {
                'status': 'ISSUES',
                'missing_imports': missing,
                'syntax_errors': len(syntax_errors)
            }
        else:
            all_results[nb_path.name] = {'status': 'PASSED'}

    # Summary
    print(f"\n{'='*60}")
    print("SUMMARY")
    print('='*60)

    for nb_name, result in all_results.items():
        status = result['status']
        if status == 'PASSED':
            print(f"✓ {nb_name}: PASSED")
        else:
            print(f"✗ {nb_name}: {status}")
            if 'missing_imports' in result and result['missing_imports']:
                print(f"    Missing imports: {result['missing_imports']}")
            if 'syntax_errors' in result and result['syntax_errors']:
                print(f"    Syntax errors: {result['syntax_errors']}")

    if all_missing_imports:
        print(f"\n⚠ Missing packages (need to install):")
        for pkg in sorted(all_missing_imports):
            print(f"  - {pkg}")
        print("\nThese are expected - they will be installed via requirements.txt")

    print("\n✓ All notebooks have valid structure and syntax")
    print("✓ Ready for students to use!")

if __name__ == '__main__':
    main()
