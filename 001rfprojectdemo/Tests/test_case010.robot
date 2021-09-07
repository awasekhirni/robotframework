#Awase Khirni Syed awase008@gmail.com Elain Technologies Inc Canada
***Settings***
Documentation   File Upload and Download demo using Robot Framewrok
Library   SeleniumLibrary
Library   Operating System

***Variables***


***Keywords***


***Test Cases***
Verify UploadingFile
    [documentation]  This test case verifies that a user can successfully upload a file
    [tags]  Regression
    Open Browser  https://the-internet.herokuapp.com/upload  Chrome
    Wait Until Element Is Visible  id:file-submit  timeout=5
    Choose File  id:file-upload  C:\\dev\\robotframework\\001rfprojectdemo\\Resources\\demo_file.txt
    Click Element  id:file-submit
    Element Text Should Be  tag:h3  File Uploaded!  timeout=5
    Element Text Should Be  id:uploaded-files  demo_file.txt  timeout=5
    Close Browser


Verify FileDownload
    [documentation]   This test case verifies that a user can successfully download a file
    [tags]    Regression
    ${chrome options}=  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys, selenium.webdriver
    ${prefs}  Create Dictionary
    ...  download.default_directory=C:\\dev\\robotframework\\001rfprojectdemo\\Resources\
    Call Method  ${chrome options}  add_experimental_option  prefs  ${prefs}
    Create Webdriver  Chrome  chrome_options=${chrome options}
    Goto  https://the-internet.herokuapp.com/download
    Click Link  xpath://a[normalize-space()='beagle1.jpeg']
    Sleep  5s
    ${files}  List Files In Directory  C:\\dev\\robotframework\\001rfprojectdemo\\Resources\
    Length Should Be  ${files}  1
    Close Browser
