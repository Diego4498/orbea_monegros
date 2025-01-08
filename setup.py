from setuptools import setup, find_packages

setup(
    name="orbea_package",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "matplotlib",
        "faker",
        # Agrega otras dependencias aquí si las necesitas
    ],
    include_package_data=True,
    description="Paquete para análisis de datos de la Orbea Monegros",
    author="Tu Nombre",
    author_email="dvazquezz@uoc.edu",
    url="https://github.com/Diego4498/orbea_monegros",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
