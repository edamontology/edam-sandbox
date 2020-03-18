# EDAM playground
In this folder, you will find jupyter notebooks to demo how EDAM can be tooled with SPARQL queries and python code aimed at checking the content and the structure of the ontology. 

## Environment setup
Any Python environment would be fine but Conda is an easy to use environment / package manager. 
Conda can be installed from https://docs.conda.io/en/latest/miniconda.html.
The following commands aim at creating a specific conda environment, with RDFlib and Jupyter-notebook packages.  
```
conda create --name edamverify python=3.7 
conda activate edamverify
conda install rdflib jupyter -c conda-forge
```

To switch to another conda environment, you can just launch `conda deactivate` and list all available cond environments `conda env list`. 

For the ones more comfortable with PIP:
```
pip install rdflib
pip install jupyter
```

Finally the jupyter notebook can be launched with: 
```
jupyter-notebook
```

