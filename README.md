# Library Checking-in & Checking-out tracker

**Disclaimer:** This is a demo project.

## Requirements
- Python 3.6+
- poetry
- Django
- Django Rest Framework

## Running from source code
Clone repository, activate shell, install requirements, run migrations, run server

```bash
$ poetry shell
$ poetry install
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

## Usage

### Django Admin
Create a superuser to login to admin interface

```bash
$ python manage.py createsuperuser --email user@email.com --username user
```

Open this [localhost URL](http://localhost:8000/) (*runserver should be active*)

### API Documentation

Initial routes are listed here: [http://127.0.0.1:8000/api/v1/](http://127.0.0.1:8000/api/v1/)

```json
{
    "users": "http://127.0.0.1:8000/api/v1/users/",
    "libraries": "http://127.0.0.1:8000/api/v1/libraries/",
    "books": "http://127.0.0.1:8000/api/v1/books/",
    "library_books": "http://127.0.0.1:8000/api/v1/library_books/",
    "library_activities": "http://127.0.0.1:8000/api/v1/library_activities/"
}
```

### Endpoints
- [X] [http://127.0.0.1:8000/api/v1/users/](http://127.0.0.1:8000/api/v1/users/) - GET: List all users, POST: User creation
- [X] [http://127.0.0.1:8000/api/v1/users/1/](http://127.0.0.1:8000/api/v1/users/1/) - GET: User detail, PUT, PATCH: Edit user
- [X] [http://127.0.0.1:8000/api/v1/libraries/](http://127.0.0.1:8000/api/v1/libraries/) - GET: List all libraries, POST: Library creation
- [X] [http://127.0.0.1:8000/api/v1/libraries/1/](http://127.0.0.1:8000/api/v1/libraries/1/) - GET: Libray detail, PUT, PATCH: Edit Library
- [ ] [http://127.0.0.1:8000/api/v1/libraries/1/books/](http://127.0.0.1:8000/api/v1/libraries/1/books/) - GET: List all books of specific library
- [ ] [http://127.0.0.1:8000/api/v1/libraries/1/books/1/status](http://127.0.0.1:8000/api/v1/libraries/1/status) - GET: Current status of specific book of specific library
- [X] [http://127.0.0.1:8000/api/v1/books/](http://127.0.0.1:8000/api/v1/books/) - GET: List of all books, POST: **Create a book record (3a)**
- [X] [http://127.0.0.1:8000/api/v1/books/1/](http://127.0.0.1:8000/api/v1/books/1/) - GET: Book detail, PUT, PATCH: Edit book
- [ ] [http://127.0.0.1:8000/api/v1/books/1/libraries/](http://127.0.0.1:8000/api/v1/books/1/libraries) - GET: Book availability in Libraries
- [X] [http://127.0.0.1:8000/api/v1/library_books/](http://127.0.0.1:8000/api/v1/library_books/) - GET: List of library books, POST: **Create a library book (3b)**
- [X] [http://127.0.0.1:8000/api/v1/library_activities/](http://127.0.0.1:8000/api/v1/library_activities/) - GET: List of library activities (checking-in, checking-out), POST: **Check-out and Check-in a library book (3c and 3d)**
- [X] [http://127.0.0.1:8000/api/v1/library_activities/user/1/books/checked-out/](http://127.0.0.1:8000/api/v1/library_activities/user/1/books/checked-out/) GET: **List all library books checked-out to a user (3e)**
- [X] [http://127.0.0.1:8000/api/v1/library_activities/library/1/books/checked-out/](http://127.0.0.1:8000/api/v1/library_activities/library/1/books/checked-out/) GET: **List all library books checked-out of a library (3f)**

## Suggestions about Authentication
- Integration with Third Party providers (AWS Cognito, OpenId, OAuth2, Twiter)
- Integration with Okta
- JSON web tokens
- Token base authentication 

## Posible questions to PO in order to prevent future versions
- Is it expected a limit of requests to the application (by hour/day/month)?
- Does a library could have a different locations? What should expected about inventory in this case?
- Does a book has a limit of stock by library?
- It is expected in the future to manage a user reputation?
- What metrics are expected about books, popularity, price?
- What metrics are expected about libraries?
