#Awase Khirni Syed awase008@gmail.com Elain Technologies Inc Canada 
***Settings***

Documentation   Looping in RobotFramework
Library   SeleniumLibrary
Library   Collections

***Variables***
@{quickLaunchList}  Assign Leave  Leave List  Timesheets  Apply Leave  My Leave  My Timesheet


***Keywords***


***Test Cases***
Testing MenuQuick Launch Texts using text list
    [documentation]  This test case verifies that the quick launch texts from the webpage matches our Text list.
    [tags]  Smoke
    Open Browser  https://opensource-demo.orangehrmlive.com/  Chrome
    Wait Until Element Is Visible  id:txtUsername  timeout=5
    Input Text  id:txtUsername  Admin
    Input Password  id:txtPassword  admin123
    Click Element  id:btnLogin
    Element Should Be Visible  id:welcome  timeout=5
    @{elementList}=  Get WebElements  css:div.quickLaunge
    @{textList}=    Create List
    FOR  ${element}  IN  @{elementList}
         ${text}=  Get Text  ${element}
         Append To List  ${textList}  ${text}
    END
    Log To Console  \n List from WebPage:
    Log To Console  ${textList}
    Log To Console  Our List:
    Log To Console  ${quickLaunchList}
    Lists Should Be Equal  ${textList}  ${quickLaunchList}
    Close Browser
