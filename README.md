# Django Polls Application

This is a web application create with Django tutorials to create polls that can vote, keep track of the number of votes, and display a result of poll.
[source](https://docs.djangoproject.com/en/2.2/intro/)

## Requirements

 The application requires
 * Python 3.6 or newer
 * Django 2.1.2 or newer
 * Python add-on modules as in [requirements.txt](requirements.txt)

## Installation

1. Clone this repository

    ```
    git clone https://github.com/llleyelll/django-polls.git
    ```

2. Go to django-polls directory

    ```
    cd django-polls
    ```

3. Make sure you have all dependencies and then run database migrations by the following commands.

    ```
    On MacOS/Linux:

        pip3 install -r requirements.txt

        python3 manage.py migrate

    On Windows:

        pip install -r requirements.txt

        python manage.py migrate
    ```
4. In the project directory root create `.env` and configure settings value for Django.
    > `.env` should contains SECRET_KEY, DEBUG, ALLOWED_HOSTS, TIMEZONE

## Running

1. Make sure you have the right current **django-polls** directory.
2. Run server 
    >if you want to change the server's port, pass it as a command-line argument. 
    >
    >Example: `python3 manage.py runserver 8080`

    ```
    On MacOS/Linux:

        python3 manage.py runserver

    On Windows:

        python manage.py runserver
    ```
3. Navigate to the polls.
    
    `localhost:8000/polls` or `127.0.0.1:8000/polls`

## Author
 -  Chananchida Fuachai 6110545473