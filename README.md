# Hyperschedule API with GraphQL

## Setup Instructions
* Clone the repo `git clone REPO_URL`
* `cd hyperschedule-api`
* Install pipenv if you don't already have it with `pip install pipenv`
* Set up a python 3 venv with `pipenv --python 3.6`
* Activate the virtualenv with `pipenv shell`
* Install dependencies with `pipenv install`
* run the server with `python app.py`

## Testing
download the courses json file to `data.json` in the main directory
access the api at `localhost:5000/graphql`

## Queries
currently supported queries are 

`query{allClasses{edges{node{name}}}}`

`query{allProfessors{edges{node{name}}}}`

Play around with what values you return for each Class or Professor


