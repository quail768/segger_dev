from setuptools import setup, find_packages

setup(
    name='segger_dev',
    version='0.1',
    packages=find_packages(where='src/segger'),
    package_dir={'': 'src/segger'},
    install_requires=[
        'numpy>=1.21.0',
        'pandas>=1.3.0',
        'scipy>=1.7.0',
        'matplotlib>=3.4.0',
        'seaborn>=0.11.0',
        'tqdm>=4.61.0',
        'torch>=2.0.0',
        'torchvision>=0.10.0',
        'pytorch-lightning>=1.3.0',
        'torchmetrics>=0.5.0',
        # 'scanpy>=1.8.0',
        'squidpy>=1.1.0',
        'adjustText>=0.8',
        'scikit-learn>=0.24.0',
        'geopandas>=0.9.0',
        'shapely>=1.7.0',
        "scanpy>=1.9.3",
        "torch-geometric>=2.2.0",
        # 'pyg_lib>=0.0.0',
        'torch_scatter>=2.1.2',
        'torch_sparse>=0.6.18',
        'torch_cluster>=1.6.3'
    ],
)
