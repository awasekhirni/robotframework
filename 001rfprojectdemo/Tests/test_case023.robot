##Awase Khirni Syed awase008@gmail.com Elain Technologies Inc Canada
#html table extraction demo

***Settings***
Library   SeleniumLibrary

***Variables***
${url}    https://testautomationpractice.blogspot.com

***Keywords***
Fetch HtmlTable Data
    
    ${rows}=    Get Element Count    xpath://table[@name='BookTable']/tbody/tr

***Test Cases***
TestCase0023 HTMLTable Extraction
    Open Browser    ${url}    Chrome
    Maximize Browser Window
    Fetch HtmlTable Data
    ${cols}=    Get Element Count    xpath://th[normalize-space()='BookName']

    Log To Console    ${rows}
    Log To Console    ${cols}

    ${tbl_data}=    Get Text    xpath://table[@name='BookTable']/tbody/tr[5]/td[1]
    Log To Console    ${tbl_data}

    Table Column Should Contain    xpath://table[@name='BookTable']    2    Author
    Table Row Should Contain    xpath://table[@name='BookTable']    4    Learn JS

    Close Browser


    Input Text    locator: WebElement | str    text: str
