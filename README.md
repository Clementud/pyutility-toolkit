# PyUtility Toolkit

## Project Overview

PyUtility Toolkit is a beginner-friendly Python command-line application that provides several useful calculation tools through an interactive menu.

The project demonstrates fundamental Python programming concepts, including functions, user input, conditional statements, loops, data types, exception handling, and automated testing.

## Features

The toolkit provides the following features:

1. **Simple Interest Calculator:** Calculates simple interest and the total amount.
2. **Temperature Converter:** Converts temperatures between Celsius and Fahrenheit.
3. **Receipt Calculator:** Calculates the cost of multiple items based on their prices and quantities.
4. **Age Calculator:** Estimates age using a person's birth year and the current year.
5. **Interactive Menu:** Allows users to select tools and return to the menu until they exit.

## Technologies Used

* Python 3
* PyCharm
* Python unittest framework
* Git and GitHub

## Project Structure

```text
pyutility-toolkit/
├── main.py
├── test_main.py
├── pseudocode.txt
├── README.md
└── .gitignore
```

## Requirements

* Python 3.10 or later
* PyCharm or another Python editor
* A terminal or command prompt

No third-party Python packages are required.

## Installation and Setup

### 1. Clone the repository


```bash
git clone https://github.com/clementud/pyutility-toolkit.git
```

### 2. Navigate to the project directory

```bash
cd pyutility-toolkit
```

### 3. Run the application

```bash
python main.py
```

On some Windows installations, you may need to use:

```bash
py main.py
```

### 4. Select an option

Follow the menu displayed in the terminal and enter the requested information.

## Example

For a simple interest calculation, enter:

* Principal: 10000
* Annual interest rate: 5
* Time: 2 years

Expected output:

```text
Simple interest: 1000.00
Total amount: 11000.00
```

## Running the Tests

Run the automated tests using:

```bash
python -m unittest -v
```

The test suite checks the calculation logic for simple interest, temperature conversion, receipt totals, and age calculations.

## Input Validation

The application includes basic validation to handle invalid numerical inputs, negative amounts where inappropriate, invalid menu choices, and invalid birth years.

## Limitations

* The age calculator estimates age from the birth year and does not account for the exact birthday.
* The application does not save calculations to a file or database.
* Receipt totals do not currently include taxes or discounts.
* The program is designed as a local command-line application rather than a web service.

## Future Improvements

Potential improvements include:

* Adding currency conversion.
* Saving receipts to a file.
* Adding tax and discount calculations.
* Creating more automated tests.
* Improving the interface and reporting features.

## Author

Created as a Python programming project to practise command-line application development, input validation, testing, and technical documentation.
