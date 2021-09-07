#Awase Khirni Syed awase008@gmail.com Elain Technologies Inc Canada
***Settings***
Documentation   Testing the login functionality using keywords
Library   SeleniumLibrary

***Variables***


***Keywords***
SetUp Test
    Open Browser  https://opensource-demo.orangehrmlive.com/  Chrome
    Maximize Browser Window


Login
    Wait Until Element Is Visible     id:txtUsername    timeout=5
    Input Text    id:txtUsername    Admin
    Input Password    id:txtPassword    admin123
    Click Element    id:btnLogin
    Element Should Be Visible    id:welcome   timeout=5


tearDown
    Close Browser


***Test Cases***

Verify SuccessfulLogin to OrangeHRM
    [documentation]  This test case verifies that the user is able to successfully log in to OrangeHRM
    [tags]  Smoke
    SetUp Test
    Login
    tearDown
