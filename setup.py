import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nl5py",
    version="0.1.0",
    author="Donny Zimmanck",
    author_email="dzimmanck@enphaseenergy.com.com",
    description="Python library for interfacing to the NL5 DLL based circuit simulator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[
        "numpy>=1.21.3",
    ],
    extras_require={
        "dev": [
            "pytest",
        ],
    },
    python_requires=">=3.9",
)
