
export PYTHONPATH=$PYTHONPATH:$PWD
export PYTHONPATH=$PYTHONPATH:$PWD/app
export PYTHONPATH=$PYTHONPATH:$PWD/db

export BAIRNG_SECRET_KEY=dev
python3.9 app/main.py --debug
