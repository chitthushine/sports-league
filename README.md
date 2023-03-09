# Sport League Ranking System
# Requirement
* django==3.2
* python==3.9.11
* docker (Optional)

# Clone Project 
```
git clone https://github.com/chitthushine/sports-league.git
```

# Local Setup
* Create Virtual Environment and install requirements (First Time Only)
```
python -m venv env
source env/bin/activate
pip install -r django/requirements.txt
```

* Database Setup (First Time Only)
```
cd django && python manage.py migrate
```

* Run Django
```
source env/bin/activate
cd django && python manage.py runserver
```

* Run Unit Test
```
cd django && python manage.py test apps.match.tests
```

* Create superuser to access admin page (optional)
```
cd django && python manage.py setupuser
```

# Running with Docker

* Up Django Container
```
docker compose up -d
```

* Database Setup (First Time Only)
```
docker exec -u root -it "$(docker-compose ps -q django)" python manage.py migrate
```

* Run Unit Test
```
docker exec -u root -it "$(docker-compose ps -q django)" python manage.py test apps.match.tests
```

* Create superuser to access admin page (optional)
```
docker exec -u root -it "$(docker-compose ps -q django)" python manage.py setupuser
```

# Accounts

* default url 
  * site : `http://localhost:8000` or `http://127.0.0.1:8000`
  * for admin page, 
    - username: admin
    - password: bh>R4!S]


# Usage
## Authentication

- To manage system (upload, create, update, or delete matches), users must be authenticated. 
- Users can create an account by clicking the `Sign Up` button on the login page, or by navigating to http://localhost:8000/auth/signup/ or it can be created by admin site (http://localhost:8000/admin). 
- Once authenticated, users can access the match list dashboard.


## Uploading Matches Data

- To upload matches data, click the `Upload Match CSV Data` button on the header.
- Choose the file that you want to upload and click `Upload` buttton. 
- Sample upload file can be seen in `django/apps/match/misc` folder.

## Creating Matches

- To create a new match, click the `Add New Match` button on the match list dashboard. 
- Enter the details of the match, including the names of the teams and the score, and click the `Save` button.

## Viewing Matches

- To view existing matches, navigate to the match list dashboard at http://localhost:8000/match/. 
- The dashboard displays a list of all matches data.

## Updating Matches

- To update a match, click the `Edit` button in match data table. 
- Update the details of the match, including the names of the teams and the score, and click the `Save` button.

## Deleting Matches

- To delete a match, click the "Delete" button in match data table. 
- Confirm that you want to delete the match by confirming in `Are you sure you want to delete this match?` alert box.

## Generating Rankings

- To generate rankings, navigate to the rankings page at http://localhost:8000/match/ranking/. 
- The rankings page displays a table of all teams, ranked by their scores. 
- The table will show the team's rank, name, and number of points.

