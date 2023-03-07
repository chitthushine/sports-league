# Setup Project (First Time Only)

* Clone Project
```
git clone https://github.com/chitthushine/sports-league.git
```
* Create Virtual Environment and install requirements
```
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

# Run Project
```
source env/bin/activate
cd django && python manage.py runserver
```

# Database (Migration and Migrate)
```
cd django
python manage.py makemigrations
python manage.py migrate
```

# Run Unit Test
```
cd django && python manage.py test apps.match.tests
```

# Start App
```
cd django/apps && django-admin startapp app_name
```

# Create Superuser
```
cd django && python manage.py createsuperuser
```

# Accounts

* default url 
  * site : `http://127.0.0.1:8000`
* Initial User
  * Admin
    * username: `admin`
    * password: `@%'h2LKifQ]~z>p`


# Usage
## Authentication

- To manage system (upload, create, update, or delete matches), users must be authenticated. 
- Users can create an account by clicking the `Sign Up` button on the login page, or by navigating to http://127.0.0.1:8000/auth/signup/ or it can be created by admin site (http://127.0.0.1:8000/admin). 
- Once authenticated, users can access the match list dashboard.


## Uploading Matches Data

- To upload matches data, click the `Upload Match CSV Data` button on the header.
- Choose the file that you want to upload and click `Upload` buttton. 
- Sample upload file can be seen in `django/apps/match/misc` folder.

## Creating Matches

- To create a new match, click the `Add New Match` button on the match list dashboard. 
- Enter the details of the match, including the names of the teams and the score, and click the `Save` button.

## Viewing Matches

- To view existing matches, navigate to the match list dashboard at http://127.0.0.1:8000/match/. 
- The dashboard displays a list of all matches data.

## Updating Matches

- To update a match, click the `Edit` button in match data table. 
- Update the details of the match, including the names of the teams and the score, and click the `Save` button.

## Deleting Matches

- To delete a match, click the "Delete" button in match data table. 
- Confirm that you want to delete the match by confirming in `Are you sure you want to delete this match?` alert box.


## Generating Rankings

- To generate rankings, navigate to the rankings page at http://127.0.0.1:8000/match/rankings/. 
- The rankings page displays a table of all teams, ranked by their scores. 
- The table will show the team's rank, name, and number of points.

