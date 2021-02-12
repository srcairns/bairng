
export PYTHONPATH=$PYTHONPATH:$PWD
export PYTHONPATH=$PYTHONPATH:$PWD/app
export PYTHONPATH=$PYTHONPATH:$PWD/db

python3.9 app/main.py --debug
