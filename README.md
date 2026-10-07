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
- inter-classifier variation between classifiers.

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
