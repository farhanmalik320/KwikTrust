# KwikTrust
Hi, i have automated the KwikTrust Web application

#CreateProject.py
This code is using Selenium to automate the creation of a project on a website. It first sets up a WebDriver object and then uses it to open a browser, navigate to a specified URL, log in, and create a project.

To create a WebDriver object, the code uses the webdriver module and specifies the path to the ChromeDriver executable file. The WebDriver object is then passed to the ChromeOptions class to create a ChromeOptions object, which is used to customize the behavior of the Chrome browser.

Once the WebDriver object is created, the setURL() function is called to open the browser, navigate to the specified URL, log in, and create a project. The createproject() function is called to create a project, which involves filling in a form with the project name and logo, and then submitting the form.

The code then closes the browser using the close() method.
