# FileParser

## Description

This Django Project consists of a file parser that parses .xlsx and .csv files. It parses each record and after proper validation, inputs the entries to a postgres database.

## Getting Started

### Requirements

* Python 2.7+

### Installation

* Clone this project from github
```
git clone https://github.com/kavisha1411/FileParser.git
```
* Download and install python
* Install Django
```
pip install django
```
* Install postgres for connection with database
```
pip install psycopg2
```
* Install pandas
```
pip install pandas
```
* Install rest_framework
```
pip install djangorestframework
```
* Install openpyxl
```
pip install openpyxl
```
* Login to postgresql Command Line interface as root user
* Create a user with password
(Omit <> brackets and replace values in <> with your values)
```
postgres=# CREATE USER <user_name> WITH encrypted password '<mypassword>';
```
* Create a database that will hold all parsed records
```
postgres=# CREATE DATABASE <db_name>;
```
* Grant user all privileges on that database
```
postgres=# GRANT ALL privileges ON DATABASE <db_name> TO <user_name>;
```
* Install pgAdmin and create a server,
<br><br>In General tab,
<br>Name - Any relevant name you'd like for your server
<br><br>In Connection tab,
<br>Host name/address - localhost
<br>Port - 5432
<br>Username - (user_name created above in psql CLI)
<br>Password - (password for user_name created above)

#### Modification in code

In fileParser/settings.py modify DATABASES dictionary:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '<db_name>',
        'USER': '<user_name>',
        'PASSWORD': '<mypassword>',
        'HOST': 'localhost',
        'PORT': '5432',
    },
}
```

### Executing
  
In terminal, within the project directory, run
```
python manage.py migrate
```
```
python manage.py runserver
```

<br>On a local browser like Edge or Chrome,
<br>go to
<br>http://127.0.0.1:8000/fileapp/upload/
<br>to upload an Excel or CSV file
<br><br>http://127.0.0.1:8000/fileapp/upload/update-file/
<br>to upload the updated Excel or CSV file
  
### Additional Information

To view entries in Postgres database, go to <br>Servers -> <your_server> -> Databases -> <db_name> -> Schemas -> public -> Tables
<br><br>Right-click on booking_data -> View/Edit Data -> All Rows <br>to view all booking entries
<br><br>Right-click on upload_data -> View/Edit Data -> All Rows <br>to view name, upload time of all uploaded files
  
Check fileapp.log to get a log of record insertions/updations, errors and warnings.
  
To run tests,
```
make test
```

View htmlcov -> index.html to get code coverage information of tests in browser.
