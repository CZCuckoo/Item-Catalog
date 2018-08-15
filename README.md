# Item Catalog

## Overview

The Item Catalog hosted here is an application developed for the Udacity Full Stack Web Developer Nanodegree Program.
It provides a list of items within a set category, as well as the ability to modify that list in various ways.
It is a RESTful application using the Python framework Flask, as well as implementing third-party authentication via Google OAuth.
All data is kept in an sqlite database.

## Dependencies

This app as several dependencies, listed in the file requirements.txt. To install, please type pip install -r requirements.txt.

## Running the apps

In order to run this app, please follow these steps, further described below.
* Download or clone this repository
* Generate a database for the app to used
* Create the proper Google credentials for use in application.py and login.html
* Run application.py, accessing on localhost:8000

### Generating a Database

This application requires a database to function. It is created by running database_setup.py, which will create a file called itemcatalog.dp. This database is populated by running PopulateCatalog.py. SQLAlchemy will be used to access this database, and is referred to within application.py.

### Google Credentials

This application requires an OAuth 2.0 client ID from the Google dashboard. In order to generate your own, please follow these steps.
* Log in to Google
* Navigate to the Google Cloud Platform credentials page (https://console.cloud.google.com/apis/credentials).
* Click "Create credentials," selecting "OAuth Client ID"
* Choose "Web application"
* Select a name for the apps
* Add http://localhost:8000 to the Authorized JavaScript origins and Redirects.
* Download JSON credentials, and save it in the application directory as "google_client_secrets.json"
