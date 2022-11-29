# Steps to run the project:

Install initial system requirements

```bash
sudo apt update
sudo apt install python3-venv python3-dev libpq-dev postgresql postgresql-contrib
```

Open terminal and clone the project

```bash
git clone git@github.comFaridLU/event-manager.git
```

Move to project directory

```bash
cd event-manager/
```

Create virtual environment

```bash
python3 -m venv venv
```

Activate the virtual environment

```bash
source venv/bin/activate
```

Install all dependencies of this project

```bash
pip install -r requirements.txt
```

Now create .env file by using following command

```
cp .env.example .env
```

Now setup database by using following command
```bash
sudo -u postgres psql
CREATE DATABASE eventdb;
CREATE USER admin WITH PASSWORD 'admin';
ALTER ROLE admin SET client_encoding TO 'utf8';
ALTER ROLE admin SET default_transaction_isolation TO 'read committed';
ALTER ROLE admin SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE eventdb TO admin;
\q
```

Now migrate the database

```bash
python manage.py migrate
```

Now collect all staticfiles

```bash
python manage.py collectstatic
```

Now simply run the project

```bash
python manage.py runserver
```

Finally, go to the following [link](http://127.0.0.1:8000) and play with the project. :)