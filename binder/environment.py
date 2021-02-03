name: module-2-Python
# channels priority
# see https://bioconda.github.io/
# conda-forge has highest prioriy
channels:
    - defaults
    - bioconda
    - conda-forge
dependencies:
    - numpy
    - scipy
    - pandas
    - xlrd
    - matplotlib
    - bokeh
    - jupyterlab
    - ipywidgets
    - scikit-learn
    - scikit-bio
    - nodejs
    - biopython
    - seaborn
    - pip
    - pip:
        - watermark
        - bcbio-gff
