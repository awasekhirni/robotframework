#Awase Khirni Syed awase008@gmail.com Elain Technologies Inc Canada 
*** Settings ***
Documentation    RobotFramework Simple Testcase01
Library          SeleniumLibrary

*** Variables ***
${browser}      Chrome
${url}          http://www.saucedemo.com/

*** Test Cases ***
loginTest
    Open Browser         ${url}          ${browser}
    LoginToApplication
    close browser


*** Keywords ***
LoginToApplication
    INPUT TEXT  id:user-name    standard-user
    INPUT TEXT  id:password     secret_sauce
    click button    id:login-button
