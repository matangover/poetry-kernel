# poetry-kernel

This is a Jupyter kernel that runs Python using [Poetry](https://python-poetry.org). With this kernel, every notebook (or group of notebooks) has its own virtual environment that is automatically created and managed by Poetry. Poetry makes it easy to manage project dependencies in a reproducible manner.

This kernel makes it easy to use Poetry and Jupyter together. Without this kernel, you would have to [install a separate kernel](https://ipython.readthedocs.io/en/stable/install/kernel_install.html#kernels-for-different-environments) for each virtual environment you create, which is more cumbersome.

## Installation

First, make sure you have [Jupyter](https://jupyter.org/) and [Poetry](https://python-poetry.org) installed. Then, clone and install the kernel:

```shell
git clone https://github.com/matangover/poetry-kernel
jupyter kernelspec install --user poetry-kernel/python-poetry
```

The above commands install the kernel into the current user's [kernel directory](https://jupyter.readthedocs.io/en/latest/projects/jupyter-directories.html#data-files).

## Usage

### Create a Project

To create a new 'notebook project', run the script `new-notebook-project.py` contained in this repository:

```shell
python poetry-kernel/new-notebook-project.py <project-path>
```

A 'notebook project' is just a normal Python project created by Poetry, which can contain one or more notebooks (and any other code or resources). All of a project's notebooks are run in one virtual environment and their dependencies are managed together.

### Create Notebooks

The script `new-notebook-project.py` creates an empty notebook to start from, which is already configured to use the `Python (Poetry)` kernel. Any additional notebooks created in the project directory (or its subdirectories) will share the same virtual environment as long as they use the `Python (Poetry)` kernel.


### Manage Dependencies

To add project dependencies, run `poetry add <package>` in the project directory, or directly from inside a notebook: `!poetry add <package>`. See [Poetry documentation](https://python-poetry.org/docs/cli/#add).


Dependencies are tracked in `<project-directory>/pyproject.toml`. When running the notebook on another machine, first ensure all dependencies are installed by running `poetry install`.

## Specify a Non-default Path to `poetry`

The kernel relies on having the `poetry` program installed in the user's PATH. This should work for most users. If you have `poetry` installed in another location, specify the full path in `kernel.json` after installing the kernel. To see where the kernel is installed, run ```jupyter kernelspec list``` .

## Notes

This kernel does not contain any code. It simply makes sure that the Python kernel is launched in the current notebook's virtual environment.  the Python interpreter belonging to the current notebook's project.

This takes advantage of the fact that Jupyter Notebook and Jupyter Lab set the kernel's current working directory to be the directory in which the notebook file is situated.
