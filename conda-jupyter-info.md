# Conda and Jupyter Command Line Setup

De nodige software stack en hoe die te verkrijgen wordt in detail uitlegd elders in de repo, cf. <./docs/prerequisites.pdf>

Dit document legt uit hoe je de conda setup kan verkrijgen via je terminal. Deze wijze is enkel getest op linux, en komt zonder garanties. Gezien dit voor mensen die reeds ervaring met conda hebben een meerwaarde kan betekenen, wordt het bijgevoegd.

## Conda Environment

The `dependencies.yaml` file lists all that is needed. To create an environment out of this, do;

```bash
conda env create -f dependencies.yaml -n db-2020
```

## Jupyter

By default, a conda environment may or may not pop up as an available "kernel" in your Jupyter environment. For guaranteed success, run the following command.

```bash
conda activate db-2020
python -m ipykernel install --user --name db-2020 --display-name "db-2020"
```

..and, for as far the python part of the setup is concerned, you are done.
