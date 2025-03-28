# Django Web Template
This is a Django Web Template meant to provide a springboard for creating a django web application with desired functionalities.

Uses best web development practices for 2024 to my knowledge.

## Features

- Obfuscation of pertenant data for the web application (see settings.py and environment_template.py).
- Customized settings to fit a user-centric web application with a sqlite3 database for the development environment and PostgreSQL database for the production environment.
- User Registration, Login, and Logout views with endpoints.

### Packages Included:
- Django==5.0.6 # Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.
- psycopg2==2.9.9 # Psycopg is the most popular PostgreSQL database adapter for the Python programming language.
- django-ratelimit=4.1.0 # Django Ratelimit provides a decorator to rate-limit views. 

### Deployment

#### Visual Studio
1. Clone the Repository
2. Open in Visual Studio
3. Create a Python Virutal Environment <br />
    `CTRL+SHIFT+P` <br />
    `Type: "Environment"` <br />
    `Select: "Create Python Environment."` <br />
    `Select: "venv"` <br />
    `Choose your interpreter.` <br />
      *If you don't see an interpreter available, install python [here](https://www.python.org/downloads/)*
4. Activate your new virtual environment
5. Install required packages from requirements.txt <br />
`pip install -r requirements.txt` <br />
6. Run the python migrations to create the database <br />
`python manage.py migrate`
7. Explore the files, especially settings.py and environment_template.py and configure as you see fit.





