### Inputs and results of codes participating in the first CHILI protocols paper

Each model has its own directory in ``inputs`` and ``outputs`` to store input files and outputs for the first protocol tests developed in the first CHILI protocol paper.
Each model should adhere to the following structure:
```
inputs/
├── model1/
│   └── <input file 1>
│   └── <input file 2>
│   └── ...
├── model2/
│   └── <input file 1>
│   └── ...
outputs/
├── model1/
│   └── model1-earth.csv
│   └── model1-trappist1b.csv
├── model2/
│   └── model2-earth.csv
│   └── model2-trappist1b.csv
```

The output files should all be named as ``<model_name>-earth.csv`` or ``<model_name>-trappist1b.csv``.
