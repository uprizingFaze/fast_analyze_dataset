from setuptools import setup, find_packages

setup(
    name='fast_analice_dataset',
    version='0.1',
    packages=find_packages(),
    install_requires=['pandas'],
    entry_points={
        'console_scripts': [
            'fast-analice-dataset = fast_analice_dataset.analysis:main'
        ]
    },
    author='Tu Nombre',
    author_email='tu@email.com',
    description='Un paquete para analizar archivos CSV de manera rápida con Pandas',
    url='https://github.com/tu_usuario/fast_analice_dataset',
)
