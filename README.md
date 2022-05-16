# Oleksiy_Shabo

In this branch you can find different tests of www.demoblaze.com WebUI.
Required libraries: selenium, pytest, pytest-html, behave, allure-behave. Also, you need to install Allure comand line tool <https://github.com/allure-framework/allure2/releases/tag/2.13.5> and add its bin folder location to PATH.
User, which will be used to test the website:
login: selenium_test
password: test123

## How to run tests

To run tests with the use of behave and generate allure reports you need to open windows cmd terminal, go to the directory of folder where this branch is located and run: 
```
generate_allure_reports.bat
```

Additionaly, I added possibility to run tests with the use of pytest and generate html reports. To do this you need to open windows cmd terminal, go to the directory of folder where this branch is located and run: 
```
generate_pytest_reports.bat
```

## Description of folders

- Folder POM includes page object model realisation with OOP.
- Reports folder includes allure reports generated with behave, html reports generated with pytest and also images of generated allure report.
- Tests folder includes pytest test of this website.
- features folder includes realisation of testing website with BDD.
