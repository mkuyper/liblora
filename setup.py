import setuptools

setuptools.setup(
        name="liblora",
        version="0.0.1",
        author="Michael Kuyper",
        author_email="mkuyper@mkdata.ch",
        description="A library with functions related to LoRaWAN, derived from Basic MAC",
        url="https://github.com/mkuyper/liblora",
        packages=setuptools.find_packages(),
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: BSD License",
            "Operating System :: OS Independent",
            ],
        python_requires='>=3.8',
        )
