## UI and API Testing Project using the Moscow Exchange

> <a target="_blank" href="https://www.moex.com/">AutomationExercise</a>

![This is an image](images/screenshots/MOEX_site.png)

### Project features

- Project build in Jenkins
- Execution of UI tests on a remote browser in Selenoid
- Reports with video, screenshot, logs for better debugging
- Comprehensive logging of requests and responses in API tests for better debugging
- Allure reports
- Integration with Allure TestOps
- Test run notifications in Telegram

### List of tests implemented in the project

#### UI

- [x] Base operation of the site
- [x] Switch language to english
- [x] Information search
- [x] Time on site in Moscow timezone 
- [x] Pop-up menu
- [x] Open learning resources
- [x] Open page with bidding results

#### API

- [x] Get available trade system in different formats
- [x] Get available securities in different formats
- [x] Get directory of market trading modes
- [x] Save information of market list by engine item in json file
- [x] Get all trades of market by limit

### The project is implemented using the following tools:

<p  align="center">
  <code><img width="5%" title="Pycharm" src="images/icons/pycharm.png"></code>
  <code><img width="5%" title="Python" src="images/icons/python.png"></code>
  <code><img width="5%" title="Pytest" src="images/icons/pytest.png"></code>
  <code><img width="5%" title="Selene" src="images/icons/selene.png"></code>
  <code><img width="5%" title="Selenium" src="images/icons/selenium.png"></code>
  <code><img width="5%" title="GitHub" src="images/icons/github.png"></code>
  <code><img width="5%" title="Jenkins" src="images/icons/jenkins.png"></code>
  <code><img width="5%" title="Selenoid" src="images/icons/selenoid.png"></code>
  <code><img width="5%" title="Allure Report" src="images/icons/allure.png"></code>
  <code><img width="5%" title="Allure TestOps" src="images/icons/allure_testops.png"></code>
  <code><img width="5%" title="Telegram" src="images/icons/telegram.png"></code>
</p>

### Automated tests are executed on the Jenkins server
> <a target="_blank" href="https://jenkins.autotests.cloud/job/008_Legiomax_graduate_work_exp/">Link to the project in Jenkins</a>

### Build parameters

* `ENVIRONMENT` - defines the environment for testing, defaults to DEV
* `COMMENT` - comment to the build

### To execute automated tests in Jenkins:

1. Open the <a target="_blank" href="https://jenkins.autotests.cloud/job/008_Legiomax_graduate_work_exp/">project</a>
2. Select the `Build with Parameters` option
3. Enter a comment in the COMMENT field
4. Choose the environment from the ENVIRONMENT dropdown list
6. Press the `Build` button

![This is an image](images/screenshots/jenkins_dash.png)

### Viewing results in Allure Report

Viewing overall test launch results

![This is an image](images/screenshots/allure_report.png)

Viewing test cases with execution report

![This is an image](images/screenshots/allure_test_cases.png)

### Integration with Allure TestOps

Storing all test cases

![This is an image](images/screenshots/allure_testOps_cases.png)

Dashboard with statistics

![This is an image](images/screenshots/allure_testOps_dash.png)

Comprehensive information on launches with attachments

![This is an image](images/screenshots/allure_testOps_launch.png)

### Integration with Jira

Attached test cases and launches

![This is an image](images/screenshots/jira.png)

### Integration with Telegram

Sending test run reports to Telegram

![This is an image](images/screenshots/telegram_report.png)

### Video report of test execution demonstrating a product purchase

![report_gif](images/screenshots/open_new_tab.gif)