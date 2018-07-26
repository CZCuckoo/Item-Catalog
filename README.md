# Item Catalog

## Description

The Item Catalog hosted here is an application developed for the Udacity Full Stack Web Developer Nanodegree Program.
It provides a list of items within a set category, as well as the ability to modify that list in various ways.
It is a RESTful application using the Python framework Flask, as well as implementing third-party OAuth authentication.

## Instructions

### Dependencies

This project requires the following
* Python 3
* Flask
* SQLAlchemy
* oauth2client

### Google Credentials

This application requires an OAuth 2.0 client ID from the Google dashboard. In order to generate your own, please follow these steps.
* Log in to Google
* Navigate to the Google Cloud Platform credentials page (https://console.cloud.google.com/apis/credentials).
* Click "Create credentials," selecting "OAuth Client ID"
* Choose "Web application"
* Select a name for the apps
* Add http://localhost:8000 to the Authorized JavaScript origins and Redirects.
* Download JSON credentials, and save it in the application directory as "google_client_secrets.json"
