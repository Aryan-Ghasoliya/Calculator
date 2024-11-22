# Calculator

# The Simple Calculator Application 
It is a graphical user interface (GUI) calculator built using Python's tkinter library. It allows users to perform basic arithmetic operations such as addition, subtraction, multiplication, and division. The application also supports clearing the input and evaluating mathematical expressions.

## Features
#### 1. Basic Arithmetic Operations:

- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)
#### 2.Expression Evaluation:

- Users can input complex expressions, and the calculator evaluates them.
#### 3.Clear Input:

- A "C" button clears the current input.
#### 4.Error Handling:

- Displays "Error" for invalid inputs or operations.
## Requirements
- Python 3.6 or higher
- tkinter library (pre-installed with Python)
## How to Run the Application
1. Save the code to a file named simple_calculator.py.
2. Open a terminal or command prompt in the directory where the file is saved.
3. Run the script using the command:
```
python simple_calculator.py
```
## Usage
1. Launch the Application:

   - Run the script to open the calculator window.
2. Input Numbers and Operations:

   - Use the number buttons (0 to 9) and operator buttons (+, -, *, /) to form expressions.
3. Evaluate Expression:

   - Press the = button to calculate the result.
4. Clear Input:

    - Press the C button to reset the input field.
## Interface Description
#### 1. Input Field:

- Displays the current expression and results.
- Supports editing via button inputs.
#### 2. Buttons:

- Numbers (0-9): Input digits.
- Operators (+, -, *, /): Perform arithmetic operations.
- Equals (=): Evaluate the expression.
- Clear (C): Reset the input.
## Example Walkthrough
#### 1. Simple Addition:

- Input: 2 + 3 → Press = → Output: 5
#### 2. Complex Expression:

- Input: 7 * (8 - 3) → Press = → Output: 35
#### 3. Error Handling:

- Input: 7 / 0 → Press = → Output: Error
## Code Description
#### 1. GUI Creation:

- Uses tk.Tk to create the main window.
- Arranges buttons using a grid layout.
#### 2. Input Handling:

- entry widget: Displays the current input or result.
- Button Clicks:
  - "C": Clears the input.
  - "=": Evaluates the expression using Python's eval function.
  - Other buttons append values to the input field.
#### 3. Error Handling:

- Catches exceptions (e.g., division by zero) and displays "Error".
## Example Screenshot
![Calculator](https://github.com/user-attachments/assets/3e635f83-3976-44b0-a582-8120cc7cec84)


Enjoy using the Simple Calculator! 😊
