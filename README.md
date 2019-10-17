# memoprop

Basic memoized properties (properties which cache the result of their getter) for *Python*.

## Quickstart/Installation

```shell
pip install memoprop
```


## Developing

Create the conda environment:

```shell
conda env create -f envs/dev.yml
conda activate memoprop-dev
```


Format code by running the pre-commit tasks:

```shell
pre-commit run --all
```

Run the tests with pytest:

```shell
pytest
```
