## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/WannaBe2D/WannaShop-django-API.git
$ cd WannaShop-django-API
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ pipenv install --ignore-pipfile
$ pipenv shell
```


Once `pipenv` has finished downloading the dependencies:
```sh
(env)$ cd wannaProject
(env)$ python manage.py migrate
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/swagger/`.
