# Selenium WebDriver Test - Nerdearla Website

A simple automated test using Selenium WebDriver to verify navigation on the Nerdearla website.

## Project Description

This project contains a Python script that automates testing of the "Agenda" button functionality on the Nerdearla conference website (https://nerdear.la/). The test verifies that clicking the Agenda button correctly navigates to the agenda page.

## Features

- **Automated Browser Testing**: Uses Selenium WebDriver to control Chrome browser
- **Element Location**: Finds elements using `By.LINK_TEXT` locator strategy
- **Navigation Verification**: Confirms successful page navigation by checking URL changes
- **Error Handling**: Includes basic try/except blocks for robust testing

## Project Structure

nerdearla-selenium-test/
├── test_nerdearla.py # Main test script
├── requirements.txt # Python dependencies
└── README.md # This file

## Future Improvements
- Implement explicit waits instead of time.sleep()
- Add Page Object Model (POM) design pattern
- Include multiple test cases
- Implement logging instead of print statements
- Add pytest framework integration

## Test Classification

**Test Type**: Functional UI Automation Test  
**Testing Level**: System Testing  
**Scope**: End-to-End (E2E) user workflow  
**Automation Level**: Fully automated

## Test Documentation

This project includes QA documentation demonstrating professional test reporting:

- (qa_test_report.md) - Detailed test execution report
- Evidence of successful test execution
