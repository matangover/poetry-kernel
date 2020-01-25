# Poetry Kernel

This is a Jupyter kernel that runs Python notebooks using [Poetry](https://python-poetry.org). With this kernel, every notebook (or group of notebooks) has its own virtual environment that is automatically created and managed by Poetry. Poetry makes it easy to manage project dependencies in a reproducible manner.

Without this kernel, you would have to create a virtual environment and [install a separate kernel](https://ipython.readthedocs.io/en/stable/install/kernel_install.html#kernels-for-different-environments) for each notebook, which is more cumbersome.

## Installation

First, make sure you have [Jupyter](https://jupyter.org/) and [Poetry](https://python-poetry.org) installed. Then, clone and install the kernel:

```shell
git clone https://github.com/matangover/poetry-kernel
jupyter kernelspec install --user poetry-kernel/python-poetry
```

The above command installs the kernel into the current user's [kernel directory](https://jupyter.readthedocs.io/en/latest/projects/jupyter-directories.html#data-files). It will be displayed in Jupyter as 'Python (Poetry)'.

## Usage

### Create a project

To create a new 'notebook project', run the script `new-notebook-project.py` contained in this repository:

```shell
python poetry-kernel/new-notebook-project.py <project-directory>
```
`<project-directory>` can be a name or a full path to the newly created project directory.

A 'notebook project' is just a normal Python project created by Poetry, which can contain one or more notebooks (and any other code or resources). All of a project's notebooks are run in one virtual environment and their dependencies are managed together.

### Create notebooks

The script `new-notebook-project.py` creates an empty notebook you can start from, which is already configured to use the `Python (Poetry)` kernel. Any additional notebooks created in the project directory (or its subdirectories) will share the same virtual environment as long as they use the `Python (Poetry)` kernel.

You can only use the `Python (Poetry)` kernel for notebooks that reside in the same directory as a `pyproject.toml` file (or any subdirectory). Otherwise, the kernel will fail to start.

### Manage dependencies

To add project dependencies, run `poetry add <package>` in the project directory, or directly from inside a notebook: `!poetry add <package>`. See [Poetry documentation](https://python-poetry.org/docs/cli/#add).

Dependencies are tracked in `<project-directory>/pyproject.toml`. When running the notebook on another machine, first ensure all dependencies are installed by running `poetry install`.

## Specify a non-default path to `poetry`

The kernel relies on having the `poetry` program installed in the user's PATH. This should work for most users. If you have `poetry` installed in another location, specify the full path in `kernel.json` after installing the kernel. To see where the kernel is installed, run ```jupyter kernelspec list``` .

## How it works

This kernel does not contain any code. It simply launches the standard IPython kernel inside the virtual environment that is associated with the notebook. It does this by replacing `python` with `poetry run python` in the kernel configuration. When a notebook is launched by Jupyter, the current directory is set to the directory containing the notebook. This way, `poetry` finds `pyproject.toml` and determines the correct virtual environment to use.
