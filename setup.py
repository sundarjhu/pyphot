from setuptools import setup, find_packages
import os

def readme():
    with open('README.rst') as f:
        return f.read()

def get_file_list(directory):
    paths = []
    for (path, directories, filenames) in os.walk('pyphot/'+directory):
        for filename in filenames:
            paths.append(os.path.join(path, filename))
    data_files = []
    for file in paths:
        data_files.append((directory, [file]))
    return data_files

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
    data_files = get_file_list('demo'),
    #data_files = [('demo/', ['pyphot/demo/demo_pyphot.ipynb'])],
    include_package_data = True,
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Science/Research',
      'Operating System :: OS Independent',
      'Programming Language :: Python',
      'Topic :: Scientific/Engineering :: Astronomy'
      ],
    zip_safe=False
)
