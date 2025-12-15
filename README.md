# datascipsych

[![Course Textbook](https://github.com/mortonne/datascipsych/blob/main/book/logo.png)](https://mortonne.github.io/datascipsych/intro.html)

Code repository for the Data Science for Psychology course at the University of Wisconsin-Milwaukee.

## Resources

* [Course textbook](https://mortonne.github.io/datascipsych/intro.html): online book with searchable webpage versions of the course lectures.
* [Sample project](https://github.com/mortonne/datascipsych-project): example project created using the principles taught in the course.

## Getting the source code

To use this project in Visual Studio Code, you must first *clone* it from GitHub. If you are reading this `README` file in Visual Studio Code, you are probably done with this step.

To clone the code project from GitHub, open a new window in Visual Studio Code. In the Welcome tab, you should see an option to `Clone Git Repository...`. Click that, then enter `https://github.com/mortonne/datascipsych.git`. Select a destination folder, such as your desktop. Choose to open the repository either in the current window or in a new window. When asked whether you trust the authors of the files in this folder, select "Yes". After a moment, you should see the code project files in the Explorer.

### Updating source code

If you already have a clone of the project on your computer, you may need to update it to get the latest versions of lectures and assignments. Follow these instructions to use VS Code to get the latest version of the project from GitHub.

To get the latest code from GitHub, open the Command Palette and run `Git: Pull`, or click the Synchronize Changes button in the lower left of VS Code (click on the sync symbol, which is two arrows in a circle). If this doesn't work (say, if an error message pops up or if you do not see updated code), there may be local changes that are interfering with synchronization.

You can often fix synchronization problems by discarding local changes. First, if there are any files that you have edited that you want to keep, open each one and use File > Save As to save each of them somewhere outside of the project directory. Then open the Source Control pane on the left and click "... > Changes > Discard All Changes" to discard all changes to your local copies of files in the project. Click the Synchronize Changes button again to get the latest version of all the files.

## Installation

To check whether you installed the project correctly, first open a terminal (`View > Terminal`). You should see `(datascipsych)` on the left side of the command prompt. This means that you have a local virtual environment set up for Python. Next, run `uv pip list`. If the package is installed, this should display a list of many Python packages. If not, then follow the instructions below to set up the project.

If you haven't already, install [uv](https://docs.astral.sh/uv/getting-started/installation/). After installing uv, in the terminal, type `uv sync`. This should install Python, create a virtual environment, and install a number of Python packages. Finally, open the Command Palette and run `Python: Select Interpreter` and choose the new virtual environment. It should be named `Python 3.13.6 (datascipsych)`.

## Running Jupyter Lab

### In Visual Studio Code (recommended)

Open a Jupyter file (these have a file extension of `.ipynb`) by clicking on it in the Explorer pane.  For example, you can open `chapters/chapter1/python_variables.ipynb`. You should see a button on the upper right that says `Select Kernel`. Click it to select a kernel to run the notebook. Select `Python Environments`, then select the virtual environment you set up previously. You should now see `datascipsych (Python 3.13.6)` in the upper right of the notebook.

### In a browser

Before you can run notebooks in your browser, you will have to install your Python virtual environment as a Jupyter kernel. Open a terminal in VS Code (`View > Terminal`), then run:

```bash
uv run ipython kernel install --user --env VIRTUAL_ENV $(pwd)/.venv --name=datascipsych
```

You should see `Installed kernelspec datascipsych in ...` with a path to where the kernel is installed on your computer.

To run Jupyter Lab, open the terminal and run `uv run jupyter-lab`. This should open your default browser with a tab running Jupyter Lab. When you open a notebook, there should be a kernel name in the upper right, showing `datascipsych`. It should use the correct kernel automatically.

If you need to change the kernel, click on the kernel name (this will be No Kernel if no kernel is currently selected) and select the kernel you want to use.

## Final project

To give a sense of what final projects should look like, there is a [sample project](https://github.com/mortonne/datascipsych-project) on GitHub.

Undergraduate students will complete the default project. See the [template project](https://github.com/mortonne/datascipsych-template) for details.
