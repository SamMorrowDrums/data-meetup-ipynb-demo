# data-meetup-ipynb-demo
Test out scanning ipynb Jupyter notebooks with Code Scanning

## Setup

To enable the git hooks for this repo, run the following in the command line:

```bash
script/create-hook-symlinks.sh
```

To run the notebook locally you'll need:

- jupyter installed
- a virtual env or other python environment
- install the ipython kernel, and any other imported dependencies (TODO, make a requirements.txt)
- load up the notebook in VSCode, or a local jupyter server
