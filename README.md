# Django REST API Demo

This django project has a demo on Django REST Framework. This project is about an API for the todo app. The project uses Django REST Framework and its Serializer class.

## Setup and Usage

Clone the repository. Then type the following in your terminal in the root directory of the app:

### Creating Virtual Env and Installing Dependencies

```bash
pip install pipenv
pipenv shell
pipenv install
```

### Creating pre-run setup:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### Run the webapp on the development server:

```bash
python manage.py runserver
```

## URLs For Visiting

* API Overview: / or /api/
* API to show List of Tasks: /api/task-list/
* API for Task Creation: /api/task-create/
* API for showing Task Detail: /api/task-detail/\<id\>/
* API for Task Updation: /api/task-update/\<id\>/
* API for Task Deletion: /api/task-delete/\<id\>/

## Further Scope

The project has the rest_api app which can be used and plugged in any Django Project. I hope to modularize this rest_api app more to be used widely.
