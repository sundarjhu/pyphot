from setuptools import setup, find_packages

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name = "pyphot",
    version = 0.1,
    description = "A tool for computing photometry from spectra",
    long_description = readme(),
    author = "Morgan Fouesneau",
    author_email = "",
    url = "https://github.com/mfouesneau/pyphot",
    packages = find_packages(),
    package_data = {'pyphot':['libs/*'], 
                    'pyphot.ezunits':['default_en.txt']},
    include_package_data = True,
    data_files=[('demo', ['demo/IRC+10216_ISO_SWS.dat'])],
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Science/Research',
      'Operating System :: OS Independent',
      'Programming Language :: Python',
      'Topic :: Scientific/Engineering :: Astronomy'
      ],
    zip_safe=False
)
