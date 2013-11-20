#!/bin/bash

syspath=$PATH
export PATH=/usr/local/bin:$syspath
export WORKON_HOME=$HOME/.virtualenvs
export PYTHONPATH=../:$PYTHONPATH
source /usr/local/bin/virtualenvwrapper.sh
workon euler