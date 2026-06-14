# Test Plan — automationexercise.com

## What I am testing
The API of automationexercise.com - a practice website for QA learning.

## What I will test
- Does the API respond correctly
- Does the products list return data
- Does each product have a name
- Does the brands list return data
- Negative quantity in cart (manual)
- Special characters in search (manual)

## How I will test
Using Python with pytest and requests library to send requests to the API and check the responses.

Manual testing of the website UI to find bugs that automated tests cannot catch.

## When to start testing
- The website is online
- Python and pytest are installed

## When to stop testing
- All tests are passing
- Bug reports are written for any failures
