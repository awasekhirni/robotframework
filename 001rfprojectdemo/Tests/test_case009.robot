#Awase Khirni Syed awase008@gmail.com Elain Technologies Inc Canada
***Settings***
Documentation   Switching between browser windows using robotframework
Library   SeleniumLibrary

***Variables***


***Keywords***

***Test Cases***
Testing browserswitch using "browser title"
    [documentation]    this test case verifies that the user is able to switch between multiple browser windows
    ...   we check using browser title and verify the text
    [tags]    Smoke
    Open Browser    https://the-internet.herokuapp.com/windows    Chrome
    Wait Until Element Is Visible    tag:h3   timeout=5
    Click Element    css:[href="/windows/new"]
    Switch Window    title:New Window
    Element Text Should Be    tag:h3    New Window    timeout=5
    Close Browser


Testing SwitchingBrowserWindow using 'Get Window Handles' and Verifying the text
    [documentation]  This test case verifies that the user is able to switch between browser
    ...  windows using window handles and verify the text.
    [tags]  Smoke
    Open Browser  https://the-internet.herokuapp.com/windows  chrome
    Wait Until Element Is Visible  tag:h3  timeout=5
    Click Element  css:[href="/windows/new"]
    ${handles}=  Get Window Handles
    Switch Window   ${handles}[0]
    Element Text Should Be  tag:h3  Opening a new window  timeout=5
    Switch Window  ${handles}[1]
    Element Text Should Be  tag:h3  New Window  timeout=5
    Close Browser
