# time_tracker

# create a virtual environment:
```shell
virtualenv -p python3.9 ~/.virtualenvs/time_tracker
```

# Activate Virtual environment
```shell
source ~/.virtualenvs/time_tracker/bin/activate
```

# To install dependencies: 
```shell
pip install -r requirements.txt
```

# To setup pre-commit: 
```shell
pre-commit install
```

# To run tests: 
```shell
pytest
```

# To run tests alternatively: 
```shell
python manage.py test --keepdb -v 2
```
