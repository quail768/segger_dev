from setuptools import setup, find_packages

setup(
    name='segger',
    version='0.1.0',
    author='Elyas Heidari',
    author_email='elyas.heidari@dkfz-heidelberg.de',
    description='Fast and accurate cell segmentation for single-molecule spatial omics',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        'torch>=2.0.0',
        'numpy>=1.21.0',
        'pandas>=1.3.0',
        'scipy>=1.7.0',
        'matplotlib>=3.4.0',
        'seaborn>=0.11.0',
        'tqdm>=4.61.0',
        'torchvision>=0.10.0',
        'lightning>=1.9.0',
        'torchmetrics>=0.5.0',
        'scanpy>=1.9.3',
        'squidpy>=1.1.0',
        'adjustText>=0.8',
        'scikit-learn>=0.24.0',
        'geopandas>=0.9.0',
        'shapely>=1.7.0',
        'path>=17.0.0',
        'pyarrow>=17.0.0'
    ],
    extras_require={
        'gpu': [
            'cuml>=21.08',
            'cudf>=21.08',
            'cugraph>=21.08',
            'cuspatial>=21.08',
            'faiss-cpu>=1.7.0',
            'faiss-gpu>=1.7.0; platform_system=="Linux"'
        ],
        'torch-geometric': [
            'torch-scatter>=2.1.2',
            'torch-sparse>=0.6.18',
            'torch-cluster>=1.6.3',
            'torch-geometric>=2.2.0',
        ],
        'multiprocessing': ['multiprocessing'],
        'dev': [
            'pytest',
            'black',
            'flake8',
            'pre-commit',
            'twine>=4.0.2',
        ],
        'docs': [
            'docutils>=0.8,!=0.18.*,!=0.19.*',
            'sphinx>=4.1',
            'sphinx-book-theme>=1.0.0',
            'myst-nb',
            'myst-parser',
            'sphinxcontrib-bibtex>=1.0.0',
            'sphinx-autodoc-typehints',
            'sphinx_rtd_theme',
            'sphinxext-opengraph',
            'sphinx-copybutton',
            'sphinx-design',
            'sphinx-hoverxref',
            'ipykernel',
            'ipython',
            'pandas',
        ],
        'tests': [
            'pytest',
            'coverage',
        ]
    },
    python_requires='>=3.10',
    project_urls={
        'Bug Tracker': 'https://github.com/EliHei2/segger_dev/issues',
        'Documentation': 'https://github.com/EliHei2/segger_dev#readme',
        'Source Code': 'https://github.com/EliHei2/segger_dev',
        'Homepage': 'https://github.com/EliHei2/segger_dev',
    },
)
