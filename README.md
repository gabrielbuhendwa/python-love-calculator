# Python Love Calculator

A command-line application built with Python that calculates a compatibility score between two people based on the occurrence of specific letters in their names.

## Overview

This project is part of my Python learning journey and focuses on string manipulation, character counting, arithmetic operations, type conversion, and conditional logic.

The Love Calculator takes two names as input and combines them into a single string. It converts the combined string to lowercase to ensure that letter counting is case-insensitive.

The program then counts the occurrences of each letter in the words `TRUE` and `LOVE`. These counts are added separately to produce two numerical values, which are concatenated and converted into an integer to generate the final compatibility score.

Based on the resulting score, the application evaluates predefined conditions and displays the corresponding message in the console.

The compatibility calculation follows a playful, entertainment-based concept. It is designed as a programming exercise rather than a scientific assessment of relationships.

## Features

* Accept two names through command-line input.
* Combine both names into a single string for processing.
* Normalize text to lowercase for consistent character counting.
* Count the occurrences of letters associated with `TRUE` and `LOVE`.
* Calculate separate totals for both groups of letters.
* Combine the calculated totals to generate a compatibility score.
* Evaluate the score using conditional statements.
* Display a result message based on the defined scoring rules.

## How It Works

The application follows a sequence of operations to calculate and interpret the compatibility score.

### 1. User Input

The program prompts the user to enter two names. These inputs serve as the basis for the entire calculation.

### 2. String Combination and Normalization

Both names are concatenated into a single string. The resulting string is converted to lowercase so that uppercase and lowercase letters are counted consistently.

### 3. Letter Counting

The program counts the occurrences of the individual letters in `TRUE` and `LOVE` using Python's string counting method.

The counts for the letters in `TRUE` are added together to form the first total. The counts for the letters in `LOVE` are added together to form the second total.

### 4. Score Generation

The two calculated totals are converted to strings and concatenated to form the final score. The combined value is then converted back into an integer so that it can be evaluated numerically.

### 5. Conditional Evaluation

The program uses conditional statements to compare the resulting score against predefined ranges. Depending on the condition met, it displays a corresponding compatibility message.

## Technologies

* **Language:** Python 3
* **Interface:** Command-line (CLI)
* **Dependencies:** None; the program uses Python's built-in functionality.

## Getting Started

### Prerequisites

* Python 3 installed on your system.
* A terminal or command-line application.

### Installation

Clone the repository:

```bash
git clone https://github.com/gabrielbuhendwa/python-love-calculator.git
```

Navigate to the project directory:

```bash
cd python-love-calculator
```

### Running the Application

Execute the main Python file:

```bash
python main.py
```

Depending on your system configuration, you may need to use `python3 main.py` instead.

Follow the prompts in the terminal to enter the two names and receive the calculated result.

## Concepts Practiced

* Variables and string data types
* User input with `input()`
* String concatenation
* Case normalization with `lower()`
* Character counting with `count()`
* Arithmetic operations and aggregation
* Type conversion between strings and integers
* Conditional statements using `if`, `elif`, and `else`
* Logical operators for combining conditions
* Formatted strings (f-strings)
* Sequential program execution and basic control flow

## Project Structure

```text
python-love-calculator/
├── main.py
├── .gitignore
└── README.md
```

## Project Status

Completed as a Python learning challenge. The project provides practical experience with string processing, numerical score generation, and conditional logic in a command-line application.

## License

This project is intended for learning and personal development.
