
# run it as 
# $ . ./setup.sh 
# to persist the env var PYTHONPATH

PROJECT="pcdb"
echo "project: $PROJECT"
VENV_PATH="./.venv"

# create .venv if does not exist
if [ ! -d $VENV_PATH ]; then
    # create venv
    echo "setting up virtualenv..."
    python -m venv .venv
else
    echo "virtualenv already exists:"
    ls -alh $VENV_PATH/bin/activate
fi

# TODO: enable only if pip -V returns the prefix
source $VENV_PATH/bin/activate

echo "installing pip packages"
pip install -r ./setup/requirements.txt

# set PYTHONPATH if not set already
if [ -z $PYTHONPATH ]; then
    echo "setting PYTHONPATH..."
    export PYTHONPATH="$(pwd):$PYTHONPATH"
else
    echo "PYTHONPATH already set to $PYTHONPATH"
fi

# prevent export of local vars too by zsh (lame)
unset PROJECT
unset VENV_PATH
echo "project env and paths setup successfully"

