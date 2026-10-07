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
- variation between classifiers.

The implementation calculates category-specific agreement measures together with their repeatability and inter-classifier components.

## Main features

The software enables the user to:

- specify an arbitrary number of categories;
- specify multiple classifiers;
- enter category-dependent conditional classification probabilities;
- calculate repeatability variation;
- calculate inter-classifier variation;
- calculate total precision variation;
- calculate the corresponding agreement score.

## Software

The software is implemented in Python and provided as a command-line application.

The main program is:

`agreement_calculator.py`

The program allows the user to specify the number of categories and classifiers, enter the conditional classification probabilities for each classifier, and calculate:

- Agreement value
- Repeatability variation
- Inter-classifier variation
- Total variation

## Requirements

- Python 3
- NumPy

Install the required Python package with:

```bash
pip install -r requirements.txt

## Citation

If you use the methodology presented in this repository, please cite the associated paper.

If you use the software implementation in computational work, please also cite the software release.

A formal citation file and DOI will be added with the first archived release.

## License

This project is released under the MIT License.

## Contact

For questions regarding the methodology or implementation, please contact the authors through the corresponding publication.
