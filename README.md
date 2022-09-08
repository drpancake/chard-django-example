# chard-django-example

An example Django project using Chard. It defines a simple background async
task that grabs the latest podcast chart rankings from Apple Podcasts.

## Quickstart

```sh
pip install -r requirements.txt
python manage.py migrate
```

Run the worker:

```sh
python manage.py chardworker
```

Run the server:

```sh
python manage.py runserver
```

Then visit http://localhost:8000/ and press the button to load the latest
rankings.

## Running dev version locally

Create a virtual environment:

    $ arch -x86_64 bash
    $ source ~/.bash_profile
    $ mkvirtualenv --python=`which python3.10` chard
    $ pip install --upgrade pip
    $ pip install -r requirements.txt
    $ (ctrl-d to close bash)

TODO.
