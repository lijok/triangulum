import setuptools

with open("README.md") as f:
    long_description = f.read()

setuptools.setup(
    name="triangulum",
    version="1.0.0",
    description="Travian Kingdoms API Client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lijok/triangulum",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU General Public License v3.0",
        "Operating System :: OS Independent",
    ],
)
