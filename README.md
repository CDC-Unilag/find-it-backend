
# Running Locally

## clone repository

ssh:
```bash
git clone git@github.com:CDC-Unilag/find-it-backend.git
```

https:
```bash
git clone https://github.com/CDC-Unilag/find-it-backend.git
```

## install required dependencies

```bash
cd find-it-backend/
pip install -r requirements.txt
```

windows:
```
    set FLASK_APP=app.py
    set FLASK_ENV=development
    flask db upgrade
    flask run
```

linux or mac:
```
    export FLASK_APP=app.py
    export FLASK_ENV=development
    flask db upgrade
    flask run
```


view demo on ```localhost:5000/```


# Running Tests

```bash
cd find-it-backend/
python -m unittest
```
