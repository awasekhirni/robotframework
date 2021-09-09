#Awase Khirni Syed awase008@gmail.com Elain Technologies Inc Canada
# Authentication and Validation
***Settings***
Library   RequestsLibrary
Library   Collections


***Variables***
${base_url}   http://restapi.demoqa.com


***Keywords***



***Test Cases***
TestCase19001 Basic Authentication
    ${auth}=    Create List    ToolsQA    TestPassword
    Create Session    authSession    ${base_url}    auth=${auth}
    ${response}=    Get Request    authSession    /authentication/CheckForAuthentication/
    Log To Console    ${response.content}
    Should Be Equal As Strings    ${response.status_code}    200
