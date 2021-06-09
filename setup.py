from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='scatter_letters',
    packages=find_packages(include=['scatter_letters']),
    version='0.0.6',
    description="A script to write letters with Matplotlib's scatter plots, create transitions from one plot to the other and build a GIF.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Thiagobc23/Scatter-Letters",
    author='Thiago B Carvalho',
    license='MIT',
    setup_requires=['numpy', 'matplotlib', 'pandas', 'imageio', 'opencv-python'],
    include_package_data = True,
    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License"
     ],
)