# bluecats-python-dman-api-testing

Testing Library for BlueCats Device Management (DMAN) API

This library involves the following forms of testing:

    1.) Functional Testing (API)

What this library does not test:

     1.) Unit Testing
     2.) Integration Testing
     3.) Front-end Testing

** Installation **

-  pip install pytest
-  pip install tavern
-  pip install pytest-xdist

*Instructions*

**Environment Settings**

1.) pipenv install
2.) pipenv shell

**Testing Authorization:**

Setting Environmental Variables:

MAC CLI:

$ export SECRET_AUTH="base64(appToken:username:password)"

**Running Tests**

** Defaults: All tests in the library start off initially in the skip position (False), to turn on a test switch Skip to True **

-   Skip: False (Test is turned on)
-   Skip: True (Test is turned off)

*** Pytest allows one to mark certain tests, such marks permit certain test to run tandum and exclude others: ***

-   GET Test Commands: $ pytest -m "get"
-   POST Test Commands: $ pytest -m "post"
-   PATCH Test Command: $ pytest -m "patch"
-   Delete Test Commands: $ pytest -m "delete"
-   CRUD Test Commands: $ pytest -m "crud"

**Pytest Automation Libraries - Local Development:**

*** Please Note: Automation & Report tools may run test in parrallel with multi-processors causing false positives & vice versa test results to occur. ***


-   Pytest-Watch:    https://github.com/joeyespo/pytest-watch
-   Pytest-XDist:    https://pypi.org/project/pytest-xdist/
-   pystest-testmon: https://pypi.org/project/pytest-testmon/
-   pytest-cov:      https://pypi.org/project/pytest-cov/
