![SIF2007: Numerical and Computational Methods](SIF2007_GitHub_Banner.png)

# SIF2007: Numerical and Computational Methods

**Department of Physics · Universiti Malaya**  
**Course lecturer: Dr Norhasliza Yusof**

Welcome to the Python resources for SIF2007. This repository contains teaching examples for exploring numerical methods, solving mathematical problems, and interpreting computational results in physics.

Use these examples together with the course lectures, manual, and tutorial instructions. Read the algorithm, predict its behaviour, run the code, and explain the result in your own words.

## Start here

1. Download the repository using **Code → Download ZIP**, then extract it. If you already use Git, you may clone the repository instead.
2. Install Python and Visual Studio Code, following the setup instructions below.
3. Practise Python basics before working through the numerical examples.
4. Open the chapter assigned in class and save a separate copy before making changes.

**Current materials:** The repository contains Python scripts (`.py`) for Chapters 2–6. These can be run directly or explored in a Jupyter notebook. Introductory Python notebooks and numerical integration examples are planned additions.

## Learning goals

Through the course activities, you will practise how to:

- Write and explain Python programs for scientific calculations.
- Translate mathematical algorithms into code.
- Work with arrays, experimental data, and plots.
- Apply numerical methods to problems in physics.
- Examine accuracy, convergence, and the limitations of a method.
- Communicate results with equations, code, figures, and written explanations.

## Course topics and available examples

| Chapter | Topic | Available materials |
| --- | --- | --- |
| 1 | Scientific computing and Python foundations | Introductory materials to be added; follow the course manual and lectures. |
| 2 | Curve fitting and interpolation | [Chapter 2](Chapter2): least-squares fitting and piecewise examples |
| 3 | Optimisation | [Chapter 3](Chapter3): Newton's method for optimisation |
| 4 | Non-linear equations | [Chapter 4](Chapter4): bisection, Newton–Raphson, and secant methods |
| 5 | Linear equations | [Chapter 5](Chapter5): Gaussian elimination, LU, Doolittle, and Cholesky examples |
| 6 | Ordinary differential equations | [Chapter 6](Chapter6): Euler, RK2, and RK4 examples |
| 7 | Numerical integration | Examples to be added; follow the course lectures. |

### Selected examples

- [Least-squares fitting](Chapter2/leastsquares1.py) and its [Excel dataset](Chapter2/lsdata1.xlsx)
- [Newton optimisation](Chapter3/newton_optimisation.py)
- [Bisection](Chapter4/bisection.py), [Newton–Raphson](Chapter4/newtonraphson.py), and [secant](Chapter4/secant.py)
- [Gaussian elimination](Chapter5/linear.py), [LU](Chapter5/lu.py), [Doolittle](Chapter5/doolittle.py), and [Cholesky](Chapter5/cholesky.py)
- [Euler](Chapter6/euler.py), [RK2](Chapter6/rk2.py), and [RK4](Chapter6/rk4.py)

## Set up Python and VS Code

Use **Visual Studio Code (VS Code)** for the notebook activities.

### 1. Install the software

- Install [Python 3](https://www.python.org/downloads/), or use your existing Anaconda installation.
- Install [Visual Studio Code](https://code.visualstudio.com/).
- In VS Code, open **Extensions** and install **Python** and **Jupyter**, both published by Microsoft.

If you already have Python through Anaconda, use that environment rather than installing a second Python unnecessarily.

### 2. Install the packages

Open a terminal for your chosen Python environment. Install the packages used by the examples and notebooks:

```bash
python -m pip install numpy scipy matplotlib pandas openpyxl jupyter ipykernel
```

On macOS or Linux, use `python3` instead of `python` if that is the command for your chosen installation. `openpyxl` supports reading the Excel dataset used in Chapter 2.

### 3. Select your environment

1. Open the extracted repository folder in VS Code using **File → Open Folder**.
2. Open the Command Palette and run **Python: Select Interpreter**.
3. Choose the Python environment in which you installed the packages.
4. When working in a notebook, use **Select Kernel** in the upper-right corner to select the same environment.

The interpreter used for scripts and the kernel used for notebooks should point to the environment containing your packages.

## Your first Jupyter notebook

Before starting numerical methods, create a notebook to check your setup:

1. Create a file named `my_first_notebook.ipynb` in VS Code.
2. Select your Python kernel.
3. Add a code cell and run:

```python
print("Welcome to SIF2007!")

mass = 2.0       # kg
speed = 3.0      # m/s
kinetic_energy = 0.5 * mass * speed**2

print(f"Kinetic energy = {kinetic_energy:.1f} J")
```

Expected output:

```text
Welcome to SIF2007!
Kinetic energy = 9.0 J
```

Add another code cell to check the main packages:

```python
import numpy as np
import scipy
import matplotlib.pyplot as plt
import pandas as pd

print("Scientific Python packages are ready.")
```

Use **Markdown cells** for headings, equations, and explanations, and **code cells** for Python. Run cells from top to bottom. Before sharing your work, restart the kernel and run all cells to check that the notebook works from a fresh session.

Beginner preparation should cover variables, arithmetic, lists, conditions, loops, functions, NumPy arrays, simple plots, and reading data. Follow the course manual for this preparation.

## Run an existing Python example

The existing examples are scripts rather than notebooks. To run one directly, open the terminal in the repository folder:

```bash
cd Chapter2
python leastsquares1.py
```

For this example, run from `Chapter2` so that the script can find `lsdata1.xlsx`. Other scripts may also expect files relative to the terminal's current folder.

To explore a script in Jupyter, create a notebook in the same chapter folder and copy the code into cells grouped by purpose: imports, inputs, calculation, and results. Keep the cells in execution order and preserve any required data-file paths.

## How to study each example

1. **Understand the problem.** Identify the equation, inputs, units, and result you need.
2. **Read the algorithm.** Connect each important code statement to the mathematical method.
3. **Predict the output.** Estimate the answer or describe the behaviour you expect.
4. **Run and inspect.** Look at the numerical output, iteration history, and plots.
5. **Change one input.** Explore an initial guess, step size, tolerance, or dataset.
6. **Check the result.** Compare with an analytical result, a residual, or another suitable method.
7. **Explain your findings.** State what changed, why it changed, and any limitations.

These are teaching examples. Use them critically: check stopping conditions, input assumptions, and numerical results before adapting them to another problem.

## Good computing habits

- Keep an unchanged copy of the original example.
- Use meaningful variable names and explain important choices in comments.
- Label plot axes and include physical units where applicable.
- Distinguish numerical error from measurement uncertainty.
- Record the parameters and package versions needed to reproduce your work.
- Read error messages carefully and investigate their causes.
- Be prepared to explain every part of the code you submit; follow the lecturer's instructions on collaboration and AI use.

## Troubleshooting

| Problem | What to check |
| --- | --- |
| `ModuleNotFoundError` | Install the missing package in the environment selected by your interpreter or notebook kernel. |
| No notebook kernel is available | Check that the Microsoft Python and Jupyter extensions are installed and that your environment contains `ipykernel`. |
| `FileNotFoundError` | Check the filename and current working folder. Keep the Chapter 2 dataset with its example. |
| A notebook works only after running cells in a particular order | Restart the kernel and run all cells from top to bottom; define variables before using them. |
| A calculation does not converge | Examine the method's assumptions, initial values, tolerance, and iteration limit. |
| A result looks incorrect | Check the equation, units, array shapes, update steps, and comparison with a known result. |

## Questions and improvements

For questions about assessment or deadlines, use the official course communication channel.

For a problem with a repository example, [open an issue](https://github.com/lizayusof/SIF2007-Numerical-and-Computational-Physics/issues). Include the filename, the relevant code, the complete error message, and what you expected to happen. Suggestions for clearer explanations and examples are welcome.

## Useful documentation

- [Python tutorial](https://docs.python.org/3/tutorial/)
- [Jupyter notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)
- [NumPy beginner's guide](https://numpy.org/doc/stable/user/absolute_beginners.html)
- [Matplotlib tutorials](https://matplotlib.org/stable/tutorials/index.html)
- [pandas getting-started tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html)
- [SciPy user guide](https://docs.scipy.org/doc/scipy/tutorial/index.html)

## Acknowledgements

These materials support teaching and learning in SIF2007 at Universiti Malaya. Contributor acknowledgements are retained in the relevant source files, including the COIL teaching collaboration with Prince of Songkla University.
