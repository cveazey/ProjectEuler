#!/bin/bash

syspath=$PATH
export PATH=/usr/local/bin:$syspath
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
workon euler