# autoinsurance

## Requirements
* python
* [pipenv](https://pipenv.kennethreitz.org/en/latest/install/#installing-pipenv)
Run `pipenv install`

## Run Application
```pipenv run python app.py```

## Run Tests
```pipenv run pytest -q test.py```

## Assignment
Assume a new business rule is added: 

It has been noticed that the previous rules do not have a case for clients above the age of 85, which is a problem, as some people live to be over 85.

Adjust the application to reflect the following:
Client's above 85 should see 
- a $5 premium increase, no warning letter, and no policy cancellation at 0 claims
- a $25 premium increase, no warning letter, and no cancellation at 1 claim
- a $100 premium increase, warning letter type 4, and no cancellation at 2-4 claims
- a $0 premium increase, no warning letter, and policy cancellation at 5+ claims

Do this by first adding new, failing unit tests for these conditions, then adjusting the application to make them pass
