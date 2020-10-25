*** Settings ***
Library  ../Library/WebDriverManager.py
Library  ../pages/HomePage.py
Library  ../pages/AboutPage.py


*** Variables ***
${browser}=    Chrome
${page_url}=    http://127.0.0.1:5000


*** Keywords ***
Suite Setup
    start session if not created

Suite Teardown
    close session if active