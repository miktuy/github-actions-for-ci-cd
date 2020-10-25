*** Settings ***
Resource  ../Resources/Resource.robot

Suite Setup  Suite Setup
Suite Teardown  Suite Teardown


*** Test Cases ***
Open Home Page
    load web page  ${page_url}
    check home page is opened

Open About Page
    load web page  ${page_url}/about
    check about page is opened