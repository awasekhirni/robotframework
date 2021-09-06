#Awase Khirni Syed awase008@gmail.com Elain Technologies Inc Canada 
*** Settings ***
Documentation    RobotFramework Simple Testcase0002
Library          SeleniumLibrary

*** Variables ***
${browser}    Chrome
${url}        https://demo.nopcommerce.com
*** Keywords ***



*** Test Cases ***

TestingInputBox
    Open Browser    ${url}  ${browser}
    Maximize Browser Window
    Title Should Be    nopCommerce demo store
    Click Link    xpath://a[normalize-space()='Log in']
    ${"email_txt"}  Set Variable    xpath://input[@id='Email']
    Element Should Be Visible    ${"email_txt"}
    Element Should Be Enabled    ${"email_txt"}
    Input Text    ${"email_txt"}    awase008@gmail.com

    ${"pwd_txt"}  Set Variable    xpath://input[@id='Password']
    Input Text    ${"pwd_txt"}    mypassword

    Click Button    xpath://button[normalize-space()='Log in']
    Sleep    5
    Clear Element Text    ${"email_txt"}
    Sleep    3

    Close Browser
