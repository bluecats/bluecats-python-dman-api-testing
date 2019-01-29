# bluecats-testing-library
Testing library for BlueCats Product Applications

This library involves the following forms of testing:

    1.) Functional Testing (API)
    2.) End-2-End (E2E) Testing (Frontend)

What this library does not test:

     1.) Unit Testing
     2.) Integration Testing

*Instructions*

**Testing Authorization:**

Setting Environmental Variables:

MAC CLI:

$ export SECRET_AUTH="base64(appToken:username:password)"

**Running Tests**

** Defaults: All tests in the library start off initially in the skip position (False), to turn on a test switch Skip to True **

1.) Skip: False - Test of turned off
2.) Skip: True - Test is turned on

*** Pytest allows one to mark certain tests, such marks permit certain test to run tandum and exclude others: ***

1.) GET Test Commands
2.) POST Test Commands
3.) PATCH Test Commanfd
4.) Delete Test Commands

**Pytest Automation Libraries - Local Development:**

*** Please Note: Automation tools may run test in parrallel with multi-processors causing false positives & vice versa test results to occur. ***

1.) Pytest-Watch
    - https://github.com/joeyespo/pytest-watch
2.) Pytest-XDist
    - https://pypi.org/project/pytest-xdist/
    
