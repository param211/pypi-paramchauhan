from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'My personal Python package'
LONG_DESCRIPTION = 'Trying out how to publish python packages, will update later to be something more specific'

# Setup
setup(
    name="paramchauhan", 
        version=VERSION,
        author="Param Chauhan",
        author_email="paramchauhan21@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed 
        
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)