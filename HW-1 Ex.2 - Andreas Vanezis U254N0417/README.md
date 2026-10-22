# COMP-548DL Homework 1 - Exercise 2

## Files

- `HW-1 Ex.2 - Andreas Vanezis U254N0417.ipynb` - main notebook
- `external_sorting.py` - external sorting script, runs inside each container
- `results.csv` - measured results

## Requirements

- Docker Desktop (running)
- Python 3 (tested with 3.11) with: `pip install docker pandas matplotlib`

## How to run

Open the notebook in this folder and run all cells in order. The notebook:

1. Generates the datasets `dataset_exp_1.csv` to `dataset_exp_8.csv` (10^1 to 10^8 records).
2. Runs `external_sorting.py` in a `python:3.11` container with 1, 2, 4 and 8 GB of RAM.
3. Saves the results to `results.csv` and plots them.

The full run takes about one hour!!
