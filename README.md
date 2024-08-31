# Phone Book

## Introduction

Hello and Welcome to my Django Rest Framework (DRF) Phone Book project.

## API Endpoints

The following API endpoints are supported in the Django project.

| Endpoint                             | Description                                             |
| :----------------------------------- | :------------------------------------------------------ |
| `users/`                             | Displays all users in the app.                          |
| `users/name/?name=x`                 | Displays all users in the app having 'x' in their name. |
| `users/phone_number/?phone_number=x` | Displays all users having phone_number 'x'.             |

## Pre-requisites

1. Enter into the virtual environment using:

```bash
pipenv shell
```

2. Install all the dependencies present in the Pipfile using:

```bash
pipenv sync
```

## Run Locally

1. Select a cloud provider postgres database of your choice or execute one locally.

2. Create a .env file using the .env.example file and replace the necessary credentials with your own.

3. Populate the database with user accounts and sample data using the following commmand:

```bash
python populate.py
```

4. Execute the web server using:

```bash
python manage.py runserver
```

5. Incase of any changes made to the application, make sure to register those changes using:

```bash
python manage.py makemigrations myapp
python manage.py migrate
```

## Testing

Before performing the testing, make sure to create a dummy user through the admin interface or programatically.

To manually test the API endpoints and their functionalities use the following:

```bash
curl -u <username>:<password> http://127.0.0.1:8000/users/
```

```bash
curl -u <username>:<password> http://127.0.0.1:8000/users/name/
```

```bash
curl -u <username>:<password> http://127.0.0.1:8000/users/name/?name=Alice
```

```bash
curl -u <username>:<password> http://127.0.0.1:8000/users/phone_number/
```

```bash
curl -u <username>:<password> http://127.0.0.1:8000/users/phone_number/?phone_number=%2B1234567890
```

```bash
curl -u <username>:<password> http://127.0.0.1:8000/users/phone_number/?phone_number=%2B1239447565
```
