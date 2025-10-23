#!/usr/bin/env python3
"""
Test requirements.txt completeness
"""

import json
from pathlib import Path
import re

def extract_imports_from_notebooks():
    """Extract all imports from all notebooks"""
    tutorials_dir = Path('/home/user/ML4ND/tutorials')
    notebooks = sorted(tutorials_dir.glob('*.ipynb'))

    all_imports = set()

    for nb_path in notebooks:
        with open(nb_path, 'r') as f:
            nb = json.load(f)

        for cell in nb['cells']:
            if cell.get('cell_type') == 'code':
                source = cell.get('source', [])
                if isinstance(source, list):
                    code = ''.join(source)
                else:
                    code = source

                # Find import statements
                for line in code.split('\n'):
                    line = line.strip()
                    if line.startswith('import ') or line.startswith('from '):
                        # Extract module name
                        if line.startswith('import '):
                            parts = line.split()
                            if len(parts) >= 2:
                                module = parts[1].split('.')[0].split(' as ')[0]
                                all_imports.add(module)
                        elif line.startswith('from '):
                            parts = line.split()
                            if len(parts) >= 2:
                                module = parts[1].split('.')[0]
                                all_imports.add(module)

    return all_imports

def read_requirements():
    """Read packages from requirements.txt"""
    req_file = Path('/home/user/ML4ND/requirements.txt')

    packages = set()
    with open(req_file, 'r') as f:
        for line in f:
            line = line.strip()
            # Skip comments and empty lines
            if not line or line.startswith('#'):
                continue
            # Extract package name (before >= or ==)
            pkg = re.split(r'[><=]', line)[0].strip()
            packages.add(pkg)

    return packages

def map_import_to_package():
    """Map import names to package names"""
    mapping = {
        'matplotlib': 'matplotlib',
        'numpy': 'numpy',
        'pandas': 'pandas',
        'scipy': 'scipy',
        'requests': 'requests',
        'bs4': 'beautifulsoup4',
        'openmc': 'openmc',
        'pathlib': 'built-in',
        'json': 'built-in',
        'urllib': 'built-in',
        'zipfile': 'built-in',
        'os': 'built-in',
        'io': 'built-in',
        'time': 'built-in',
        'ast': 'built-in',
        're': 'built-in',
        'sys': 'built-in',
    }
    return mapping

def main():
    print("="*60)
    print("REQUIREMENTS.TXT VERIFICATION")
    print("="*60)

    # Extract imports from notebooks
    notebook_imports = extract_imports_from_notebooks()
    print(f"\nImports found in notebooks: {sorted(notebook_imports)}")

    # Read requirements.txt
    requirements = read_requirements()
    print(f"\nPackages in requirements.txt: {sorted(requirements)}")

    # Map imports to packages
    import_map = map_import_to_package()

    # Check coverage
    print("\n" + "="*60)
    print("COVERAGE CHECK")
    print("="*60)

    missing = []
    for imp in sorted(notebook_imports):
        if imp in import_map:
            pkg = import_map[imp]
            if pkg == 'built-in':
                print(f"✓ {imp:20s} (built-in)")
            elif pkg in requirements:
                print(f"✓ {imp:20s} -> {pkg}")
            else:
                print(f"✗ {imp:20s} -> {pkg} (MISSING FROM requirements.txt)")
                missing.append(pkg)
        else:
            print(f"? {imp:20s} (unknown mapping)")

    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)

    if missing:
        print(f"✗ Missing packages: {missing}")
        return 1
    else:
        print("✓ All required packages are in requirements.txt")
        print("✓ requirements.txt is complete!")
        return 0

if __name__ == '__main__':
    exit(main())
