# Django Waggle Cloud

This is a prototype of consolidating a backend for Waggle into a set of modular Django apps.

## Usage

_I highly recommend creating a virtual environment._

### 1. Install requirements (One time)

```sh
pip3 install -r requirements.txt
```

### 2. Collect static content (One time)

```sh
python3 manage.py collectstatic
```

### 3. Create a superuser for yourself (One time)

```sh
python3 manage.py createsuperuser
```

### 4. Run server

```sh
python3 manage.py runserver
```

You should now be able to visit the [admin site](http://localhost:8000).
