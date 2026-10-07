# Agreement Between Classifiers

Software implementation accompanying the paper:

**Agreement Between Classifiers: A Metrological Interpretation**

Authors:  
Yariv N. Marmor  
Emil Bashkansky

Department of Industrial Engineering and Management,  
Braude College of Engineering, Karmiel, Israel

## Overview

This repository contains the software implementation developed for the analysis presented in the paper *Agreement Between Classifiers: A Metrological Interpretation*.

The proposed framework provides a metrological interpretation of agreement in nominal categorical measurements by decomposing disagreement into two main precision components:

- repeatability variation within classifiers;
- inter-classifier variation.

The implementation calculates category-specific agreement measures together with their repeatability and inter-classifier components.

## Main features

The software enables the user to:

- specify the number of categories;
- specify the number of classifiers;
- enter category-dependent conditional classification probabilities;
- calculate repeatability variation;
- calculate inter-classifier variation;
- calculate total variation;
- calculate the corresponding agreement value.

## Software

The software is implemented in Python and provided as a command-line application.

The main program is:

`agreement_calculator.py`

## Requirements

- Python 3
- NumPy

Install the required package with:

```bash
pip install -r requirements.txt
```

## Running the software

Download or clone this repository and run:

```bash
python agreement_calculator.py
```

The program will interactively request:

1. Number of categories (`K`)
2. Number of classifiers (`L`)
3. Conditional classification probabilities for each classifier

Each classifier's probabilities must sum to 1.

## Example

Example with 3 categories and 3 classifiers.

Input:

```text
Number of Categories (K): 3
Number of Classifiers (L): 3

Classifier 1:
0.8
0.1
0.1

Classifier 2:
0.7
0.2
0.1

Classifier 3:
0.9
0.05
0.05
```

Expected output:

```text
Agreement value = 0.4825
Repeatability = 0.4925
Inter-classifier variation = 0.0167
Total variation = 0.5092
```

## Citation

If you use the methodology presented in this repository, please cite the associated paper.

If you use the software implementation in computational work, please also cite the software release.

Software DOI:

https://doi.org/10.5281/zenodo.23224772

Citation metadata are also provided in the `CITATION.cff` file.

## License

This project is released under the MIT License.

## Contact

For questions regarding the methodology or implementation, please contact the authors through the corresponding publication.
