#!/bin/bash
set -eu

NOTEBOOK_DIR=$(git rev-parse --show-toplevel)/src
find $NOTEBOOK_DIR  -name '*.ipynb' \
  -exec jupyter nbconvert --to script {} --output {} \; \
  -exec git add {}.py \; || echo "No .ipynb files to convert"