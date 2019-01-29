# bluecats-testing-library
Testing library for BlueCats Product Applications

This library involves the following forms of testing:

    1.) Functional Testing (API)
    2.) End-2-End (E2E) Testing (Frontend)

What this library does not test:

     1.) Unit Testing
     2.) Integration Testing

Instructions:

Testing Authorization:

Setting Environmental Variables:

MAC CLI:

$ export SECRET_AUTH="base64(appToken:username:password)"

Pytest Automation Libraries - Local Development:

** Please Note: Automation tools may run test in parrallel with multi-processors causing false positives & vice versa test results to occur. **

1.) Pytest-Watch
    - https://github.com/joeyespo/pytest-watch
2.) Pytest-XDist
    - https://pypi.org/project/pytest-xdist/
