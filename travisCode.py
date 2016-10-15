# this code is normally hidden with the filename .travis.yml
# this is just a visible copy of the hidden code

language: python
python:
  - "2.6"
  - "2.7"
  - "3.0"
  - "3.2"
  - "3.3"
  - "3.4"
  - "3.5"
  # does not have headers provided, please ask https://launchpad.net/~pypy/+archive/ppa
  # maintainers to fix their pypy-dev package.
  - "pypy"
# command to install dependencies
install:
  - pip install .
  - pip install -r requirements.txt
# command to run tests
script: test_rpn.py
