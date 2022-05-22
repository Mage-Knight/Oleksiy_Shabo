# Oleksiy_Shabo

In this branch you can find different tests of www.dropbox.com WebAPI.
Required libraries: requests, behave, allure-behave. Also, you need to install Allure comand line tool <https://github.com/allure-framework/allure2/releases/tag/2.13.5> and add its bin folder location to PATH.

## How to run tests

To run tests with the use of behave and generate allure reports you need to open windows cmd terminal, go to the directory of folder where this branch is located and run: 
```
generate_allure_report.bat
```

## Description of folders and files

- Reports folder includes allure reports generated with behave and also images of generated allure report.
- features folder includes realisation of testing Dropbox API with BDD.
- files folder includes files for use in tests.
- dropbox_methods.py includes interaction with the dropbox app folder by API realised with OOP.