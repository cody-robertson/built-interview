# Built Interview
## Author: Cody Robertson

## Overview
This project meets the requirements of the exercise aside from pytest tests and fixtures.

I ran out of time and wasn't able to spin up a mock db or mock out SQLAlchemy.

## How to Run
A series of `make` commands have been provided to help with setup and teardown.

- `make start` - builds and starts the Flask API, MySQL database, and Localstack AWS instance.
- `make stop` - stops all containers for the project
- `make migrate` - execute Alembic migrations against the MySQL database
- `make init_kinesis` - create a stream in Kinesis to verify that the connection between Flask and Localstack is working

## How to Use
A Postman collection has been provided for testing the endpoints.

Our basic data models consist of a BudgetCategory which has a name and not much else and BudgetItems that relate to a BudgetCategory but contain a monetary value.

Possible extensions that I've considered are adding timestamps to the BudgetItem transactions and calculating their totals on a month-to-month basis against the provided BudgetAmount model.

1. You can list, add, get, update, and delete BudgetCategories (you'll need at least one to create a BudgetItem)
2. You can list, add, get, update, and delete BudgetItems with a category_id corresponding to a BudgetCategory
3. The root url for the API fetches streams from Localstack Kinesis.  Try it before and after running `make init_kinesis`