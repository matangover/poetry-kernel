from __future__ import print_function
import os
import shutil
import sys
from subprocess import check_call

if len(sys.argv) != 2 or sys.argv[1] in ('--help', '-h'):
    print('Usage: %s <project-directory>' % sys.argv[0])
    sys.exit(1)

project_path = sys.argv[1]
project_name = os.path.basename(project_path)
print('Creating project: ' + project_name)
os.mkdir(project_path)
# Force poetry to ignore any active venv by removing the VIRTUAL_ENV and CONDA_PREFIX env vars.
# See:
# https://github.com/python-poetry/poetry/issues/281#issuecomment-403102022
# https://github.com/python-poetry/poetry/blob/e0bc7f3fc06a6f1caca694432c9f8bd8c0af30db/src/poetry/utils/env.py#L679
# https://github.com/python-poetry/poetry/issues/4622
env = os.environ.copy()
env.pop('VIRTUAL_ENV', None)
env.pop('CONDA_PREFIX', None)
check_call(['poetry', 'init', '-q', '-n'], cwd=project_path, env=env)
check_call(['poetry', 'add', 'ipykernel'], cwd=project_path, env=env)

notebook_template = os.path.join(os.path.dirname(__file__), 'python-poetry.ipynb.template')
notebook = os.path.join(project_path, project_name + '.ipynb')
shutil.copyfile(notebook_template, notebook)

print('''
Done. Notebook created: {0}

Open this notebook in Jupyter to start working. Additional notebooks created
inside the project directory will run in the same virtual environment, as long
as you use the Python (Poetry) kernel.

To add dependencies, run `poetry add <package>` in the project directory or
directly from a notebook: `!poetry add <package>`.\
'''.format(notebook)
)
