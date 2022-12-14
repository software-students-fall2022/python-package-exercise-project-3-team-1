![Python arithmetic trainer](https://github.com/software-students-fall2022/python-package-exercise-project-3-team-1/actions/workflows/build.yaml/badge.svg)

# Python Package Arithmetic Trainer

This package allows users to test their basic arithmetic and mental math skills.

## Documentation

### add(a, b)
The add function takes in two numbers (a, b) and returns the sum.
```python
from team1ArithmeticTrainer import functions
functions.add(5, 10)
```
### subtract(a, b)
The subtract function takes in two numbers (a, b) and returns the difference.
```python
from team1ArithmeticTrainer import functions
functions.subtract(10, 5)
```
### multiply(a, b)
The multiply function takes in two numbers (a, b) and returns the product.
```python
from team1ArithmeticTrainer import functions
functions.multiply(10, 5)
```
### divide(a, b)
The divide function takes in two numbers (a, b) and returns the quotient.
```python
from team1ArithmeticTrainer import functions
functions.divide(10, 5)
```
### sqr_root(a)
The sqr_root function takes in one number (a) and returns the square root.
```python
from team1ArithmeticTrainer import functions
functions.sqr_root(16)
```
### cube_root(a)
The cube_root function takes in one number (a) and returns the cube root.
```python
from team1ArithmeticTrainer import functions
functions.cube_root(27)
```
### modulus(a, b)
The modulus function takes in two numbers (a, b) and returns the remainder.
```python
from team1ArithmeticTrainer import functions
functions.modulus(27, 5)
```
### checkPerfectSquare(num)
The checkPerfectSquare function takes in one number (num) and checks if it is a perfect square.
If a perfect square is found, the least value among all valid is returned. If no perfect square is found or input is negative, -1 is returned.
```python
from team1ArithmeticTrainer import functions
functions.checkPerfectSquare(16)
```
### checkPerfectCube(num)
The checkPerfectCube function takes in one number (num) and checks if it is a perfect cube.
If a perfect cube is found, the least value among all valid candidate is returned. If no perfect cube is found or input is negative, -1 is returned.
```python
from team1ArithmeticTrainer import functions
functions.checkPerfectCube(125)
```
### generate_question()
The generate_question function generates a random arithmetic question choosing either an addition, subtraction, multiplication, division, sqr root, modulus, or cube root problem.
If not specified, the function returns four values
- question: question type from 'add', 'subtract', 'multiply', 'divide', 'sqr_root', 'modulus', 'cube_root'
- a: a random integer from 1 to 100 inclusive
- b: a random integer from 1 to 100 inclusive
- ans: the correct ans of this question
#### Return values specification: 
- 'subtract'
  - value b will always be less than a
- 'multiply'
  - both a and b will be a random integer from 1 to 10 inclusive
- 'divide'
  - value b will be ensured to be a factor of a
- 'sqr_root'
  - returns only three values that contains question, a, and ans. 
    - a: random integer from 1 to 100 inclusive
- 'cube_root'
  - returns only three values that contains question, a, and ans. 
    - a: random integer from 1 to 100 inclusive
```python
from team1ArithmeticTrainer import functions
functions.generate_question()
```
### print_prompt(question, a, b)
The print_prompt function takes three parameters (question, a, b) and prompts the user to answer an arithmetic problem.
```python
from team1ArithmeticTrainer import functions
functions.print_prompt(add, 5, 10)
```
[Program utilizing all functions (Note some of the above functions are auxiliary functions)](https://github.com/software-students-fall2022/python-package-exercise-project-3-team-1/tree/main/src/team1ArithmeticTrainer/example.py)

## How to install and use this package

Try [installing and using our package](https://packaging.python.org/en/latest/tutorials/packaging-projects/#installing-your-newly-uploaded-package) in a separate Python project:

1. Create a `pipenv`-managed virtual environment and install the latest version of our package: `pipenv install -i https://pypi.org/project/arithmeticTrainer/`. (Note that if you've previously created a `pipenv` virtual environment in the same directory, you may have to delete the old one first. Find out where it is located with the `pipenv --venv` command.)
2. Activate the virtual environment: `pipenv shell`.
3. Navigate to the team1ArithmeticTrainer directory `cd team1ArithmeticTrainer` and run the program from the command line: `python3 __main__.py`.
4. Exit the virtual environment: `exit`.

Try running the package directly:

1. Create and activate up the `pipenv` virtual environment as before.
2. Navigate to the src directory `cd src` and run the package directly from the command line: `python3 -m team1ArithmeticTrainer`. This should run the code in the `__main__.py` file.
3. Exit the virtual environment.

## How to run unit tests

Simple example unit tests are included within the `tests` directory. To run these tests...

1. Install pytest in a virtual environment.
1. Run the tests from the main project directory: `python3 -m pytest`.
1.  Tests should never fail. Any failed tests indicate that the production code is behaving differently from the behavior the tests expect.

## Pro tip

While working on the package code, and verifying it behaves as expected, it can be helpful to install the package in "_editable_" mode so that changes to the package are immediately updated in the virtual environment.

- To do this, run `pipenv install -e .` from the main project directory.

## Team Members

[Kevin Gong](https://github.com/kxg202)

[Dixit Timilsina](https://github.com/dt1930)

[James Liu](https://github.com/liushuchen2025)

## Link to Package on PyPi

[Arithmetic Trainer](https://pypi.org/project/arithmeticTrainer/)