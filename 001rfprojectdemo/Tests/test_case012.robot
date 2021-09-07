#Awase Khirni Syed awase008@gmail.com Elain Technologies Inc Canada
***Settings***
Documentation   Wikipedia conditional testing
Library   SeleniumLibrary

***Variables***

***Keywords***

Click Wikivoyage
    Click Element  css:[data-jsl10n="wikivoyage.name"]

Click Wiktionary
    Click Element  css:[data-jsl10n="wiktionary.name"]

***Test Cases***
Verify wikivoyage and validate
    [documentation]  This test case verifies if we find Wikivoyage on the page, then we click on it.
    [tags]  Regression
    Open Browser  https://www.wikipedia.org/  Chrome
    ${count}=  Get Element Count  css:[data-jsl10n="wikivoyage.name"]
    Run Keyword If  ${count} > 0  Click Wikivoyage  # If the element is present we will get the value of count as 1
    ...  ELSE  Click Wiktionary
    Title Should Be  Wikivoyage  timeout=5
    Close Browser


Verify  Wiktionary demo
    [documentation]  This test case verifies if we don't find Wikivoyage on the page, then we click on Wiktionary.
    [tags]  Regression
    Open Browser  https://www.wikipedia.org/  Chrome
    ${count}=  Get Element Count  css:wrong locator  # Intentionally given wrong locator to make sure control goes to Else
    Run Keyword If  ${count} > 0  Click Wikivoyage  # If the element is not present we will get the value of count as 0
    ...  ELSE  Click Wiktionary
    Title Should Be  Wiktionary  timeout=5
    Close Browser
