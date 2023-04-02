# Scrapping-asessment

**make and activate environment for project using commands given:**

**1:making environment and installing dependencies**


Install python on local machine https://www.python.org/


**i: create environment and install dependencies:**

```
pip install virtualenv
```

**ii: create environment:**

```
python -m venv venv
```

**iii: To activate environemnt but to use below command you should have in the directory where venv exists.**

```
.\venv\Scripts\activate
```

**ii: installing requirements.txt:**

```
pip install -r requirements.txt
```

**2: make a superuser so you have credentials to look the scrapped data into the admin panel:**

```
python manage.py createsuperuser
```

**3: running server:**

```
python manage.py runserver
```

**commands to run: **
_a:_ server will be running on http://localhost:8000
_b:_ On http://localhost:8000 you will have an button to start scrapping.
_c:_ On http://localhost:8000/admin you can access the admin panel and use the credentials you have created earlier in step 2 to login and in vehicles you can have the vehicles scrapped data.
