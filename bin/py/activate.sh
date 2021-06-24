#!/bin/bash
# -*- coding: utf-8 -*-
#
# activate your virtualenv quickly if not using pyenv-virtualenv
#
# usage:
#
# - activate: ``$ source ./bin/py/activate.sh``
# - deactivate: ``$ deactivate``

if [ -n "${BASH_SOURCE}" ]
then
    dir_here="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
else
    dir_here="$( cd "$(dirname "$0")" ; pwd -P )"
fi
source ${dir_here}/python-env.sh
source ${bin_activate}
