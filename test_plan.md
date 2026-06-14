# Test Plan — automationexercise.com

## Introduction
This test plan covers API and manual testing of automationexercise.com.
The goal is to verify that the API returns correct data and the website UI works as expected.

## Scope

**In scope:**
- Products API endpoint
- Brands API endpoint
- Search API endpoint
- Manual UI testing of cart functionality

**Out of scope:**
- Payment processing
- User authentication API
- Mobile version

## Test Approach
- Automated API testing using Python, pytest and requests library
- Manual UI testing to find bugs that automated tests cannot catch

## Entry Criteria
- Website is accessible
- Python 3.14 and pytest are installed
- All dependencies from requirements.txt are installed

## Exit Criteria
- All automated tests are passing
- Manual test cases are executed
- Bug reports are written for all failures

## Test Environment
- OS: Windows 11
- Browser: Chrome
- Python: 3.14
- Tools: pytest, requests, pytest-html

## Risks
- Website may be temporarily unavailable

## Deliverables
- Automated test suite (tests/test_api.py)
- Test cases (test_cases/test_cases.csv)
- Bug reports (bug_reports/)