"""
Agreement Between Classifiers
=============================

Software implementation accompanying the paper:
"Agreement Between Classifiers: A Metrological Interpretation"

This module calculates:
- Agreement value
- Repeatability variation
- Inter-classifier variation
- Total variation

The mathematical formulas are preserved from the original implementation.
"""

from __future__ import annotations

import numpy as np


def calculate_metrics(
    probability_table: np.ndarray,
    num_categories: int,
    num_classifiers: int,
) -> dict[str, float]:
    """
    Calculate agreement and its variation components.

    Parameters
    ----------
    probability_table : np.ndarray
        Matrix of shape (num_classifiers, num_categories), where each row
        contains the conditional classification probabilities for one classifier.
        Each row must sum to 1.

    num_categories : int
        Number of categories (K). Must be at least 2.

    num_classifiers : int
        Number of classifiers (L). Must be at least 2.

    Returns
    -------
    dict[str, float]
        Dictionary containing:
        - "agreement"
        - "repeatability"
        - "inter_classifier_variation"
        - "total_variation"

    Notes
    -----
    The formulas used here are mathematically identical to those in the
    original implementation.
    """
    k = num_categories
    l = num_classifiers
    proportions = probability_table

    # Repeatability variation
    repeatability = (
        k
        / (k - 1)
        / l
        * np.sum(np.sum(proportions * (1 - proportions), axis=1))
    )

    # Mean conditional probabilities across classifiers
    column_averages = np.mean(proportions, axis=0)

    # Inter-classifier variation
    sum_p = np.zeros(k)
    inter_classifier_variation = 0.0

    for category_index in range(k):
        for classifier_index in range(l):
            sum_p[category_index] += (
                proportions[classifier_index, category_index] / l
            )
            inter_classifier_variation += (
                proportions[classifier_index, category_index]
                - column_averages[category_index]
            ) ** 2

    inter_classifier_variation = (
        k / (k - 1) * inter_classifier_variation / l
    )

    # Total variation
    total_variation = k / (k - 1) * (1 - np.sum(sum_p**2))

    # Agreement
    agreement = 1 - (
        repeatability
        + l / (l - 1) * inter_classifier_variation
    )

    return {
        "agreement": float(agreement),
        "repeatability": float(repeatability),
        "inter_classifier_variation": float(inter_classifier_variation),
        "total_variation": float(total_variation),
    }


def print_results(results: dict[str, float]) -> None:
    """Print the calculated results in a readable format."""
    print("\n--- Results ---")
    print(f"Agreement value = {results['agreement']:.4f}")
    print(f"Repeatability = {results['repeatability']:.4f}")
    print(
        "Inter-classifier variation = "
        f"{results['inter_classifier_variation']:.4f}"
    )
    print(f"Total variation = {results['total_variation']:.4f}")


def read_integer(prompt: str, minimum: int) -> int:
    """Read and validate an integer value from the user."""
    while True:
        try:
            value = int(input(prompt))
            if value >= minimum:
                return value
            print(
                f"Error: The value must be greater than or equal to {minimum}. "
                "Please try again."
            )
        except ValueError:
            print("Error: Invalid input. Please enter an integer.")


def read_probability_row(
    classifier_number: int,
    num_categories: int,
) -> np.ndarray:
    """
    Read one classifier's probability vector.

    The values must be between 0 and 1 and must sum to 1
    within a tolerance of 1e-6.
    """
    while True:
        print(f"\nEnter probabilities for Classifier number {classifier_number}:")

        row_sum = 0.0
        probability_row = np.zeros(num_categories)

        for category_index in range(num_categories):
            while True:
                try:
                    probability = float(
                        input(
                            f"Enter probability for Category "
                            f"{category_index + 1}: "
                        )
                    )

                    if 0.0 <= probability <= 1.0:
                        probability_row[category_index] = probability
                        row_sum += probability
                        break

                    print(
                        "Error: The probability must be between 0 and 1. "
                        "Please try again."
                    )

                except ValueError:
                    print("Error: Invalid input. Please enter a number.")

        if abs(row_sum - 1.0) < 1e-6:
            print(
                f"Probabilities for Classifier {classifier_number} "
                "entered successfully."
            )
            return probability_row

        print(
            f"Error: The sum of probabilities for Classifier "
            f"{classifier_number} is {row_sum:.2f}, and is not equal to 1. "
            "Please re-enter the row."
        )


def run_probability_calculator() -> None:
    """Run the interactive command-line probability calculator."""
    num_categories = read_integer(
        "Enter the number of Categories (K): ",
        minimum=2,
    )

    num_classifiers = read_integer(
        "Enter the number of Classifiers (L): ",
        minimum=2,
    )

    probability_table = np.zeros((num_classifiers, num_categories))

    for classifier_index in range(num_classifiers):
        probability_table[classifier_index, :] = read_probability_row(
            classifier_number=classifier_index + 1,
            num_categories=num_categories,
        )

    print("\nEntered probability table:")
    print(probability_table)

    results = calculate_metrics(
        probability_table=probability_table,
        num_categories=num_categories,
        num_classifiers=num_classifiers,
    )
    print_results(results)


if __name__ == "__main__":
    run_probability_calculator()
    input("\nPress Enter to exit...")
