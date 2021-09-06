#Awase Khirni Syed awase008@gmail.com Elain Technologies Inc Canada 
***Settings***
Documentation    shadow DOM in RobotFramework
Library    SeleniumLibrary

***Variables***
${JSPath}=  document.querySelector('shop-app').shadowRoot  #1
    ...  .querySelector('iron-pages')  #2
    ...  .querySelector('shop-list').shadowRoot  #3
    ...  .querySelector('ul > li:nth-child(1)')  #4
    ...  .querySelector('shop-list-item').shadowRoot  #5
    ...  .querySelector('.title')  #6

***Keywords***

***Test Cases***

Testing ShadowDOM traversal by item title
  [documentation]   This test case verifies the item title by traversing through the shadow DOM elements
  [tags]    Smoke
  Open Browser    https://shop.polymer-project.org/list/mens_outerwear    Chrome
  Element Text Should Be    dom:${JSPath}    Men\'s Tech Shell Full-Zip  timeout=5
  Close Browser
