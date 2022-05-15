call behave -f allure_behave.formatter:AllureFormatter -o ./Reports/Allure_reports features
call allure serve ./Reports/Allure_reports