# Simple Calculator

This is a simple calculator program written in Python. It allows the user to perform basic arithmetic operations such as addition, subtraction, multiplication, and division.

## Features

- Addition: Adds two numbers and displays the result.
- Subtraction: Subtracts the second number from the first number and displays the result.
- Multiplication: Multiplies two numbers and displays the result.
- Division: Divides the first number by the second number and displays the result.
  - Note: Division by zero is not allowed.

## Getting Started

To use this calculator, follow the steps below:

1. Ensure you have Python installed on your computer. If not, you can download and install it from the official Python website: https://www.python.org/downloads/

2. Install the `termcolor` package by running the following command in your terminal:
   ```
   pip install termcolor
   ```

3. Download the `calculator.py` file from this repository.

4. Open a terminal or command prompt and navigate to the directory where the `calculator.py` file is located.

5. Run the following command to execute the program:
   ```
   python calculator.py
   ```

## Usage

1. Upon running the program, a welcome message will be displayed.

2. Enter the first number when prompted.

3. Enter the second number when prompted.

4. Select the desired operation by entering the corresponding number:
   - 1: Addition
   - 2: Subtraction
   - 3: Multiplication
   - 4: Division
   - 5: Exit

5. The result of the selected operation will be displayed.

6. Repeat the steps to perform additional calculations or choose "5" to exit the program.

## Example

```
Welcome to the Simple Calculator!

Please enter the first number: 10
Please enter the second number: 5
Please select the operation:
1: Addition
2: Subtraction
3: Multiplication
4: Division
5: Exit 3

Multiplication of Numbers = 50
```

## Error Handling

- If the user selects the division operation (4) and the second number is zero, an error message will be displayed, and the program will exit.