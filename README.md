# bluecats-testing-library
Testing Library for BlueCats Product Applications

This library involves the following forms of testing:

    1.) Functional Testing (API)
    2.) End-2-End (E2E) Testing (Frontend)

What this library does not test:

     1.) Unit Testing
     2.) Integration Testing

** Installation **

-  pip install pytest
-  pip install pytest-xdist

*Instructions*

**Testing Authorization:**

Setting Environmental Variables:

MAC CLI:

$ export SECRET_AUTH="base64(appToken:username:password)"

**Running Tests**

** Defaults: All tests in the library start off initially in the skip position (False), to turn on a test switch Skip to True **

-   Skip: False (Test of turned off)
-   Skip: True (Test is turned on)

*** Pytest allows one to mark certain tests, such marks permit certain test to run tandum and exclude others: ***

-   GET Test Commands: $ pytest -m "get"
-   POST Test Commands: $ pytest -m "post"
-   PATCH Test Command: $ pytest -m "patch"
-   Delete Test Commands: $ pytest -m "delete"

**Pytest Automation Libraries - Local Development:**

*** Please Note: Automation tools may run test in parrallel with multi-processors causing false positives & vice versa test results to occur. ***


-   Pytest-Watch: https://github.com/joeyespo/pytest-watch
-   Pytest-XDist: https://pypi.org/project/pytest-xdist/
