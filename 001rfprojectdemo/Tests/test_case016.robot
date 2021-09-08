#Awase Khirni Syed awase008@gmail.com Elain Technologies Inc Canada
#Data validation in JSON file
#https://jsonpathfinder.com/
#https://jsonpath.com/

***Settings***
Library   JSONLibrary
Library   os
Library   Collections
Library   RequestsLibrary
#Library         REST    https://jsonplaceholder.typicode.com


*** Variables ***
${base_url}    https://restcountries.eu/
#${json_path}    C:\\dev\\robotframework\\001rfprojectdemo\\Data\\

***Keywords***


*** Test Cases ***


TestCase16001 JSON Validation Local
    ${json_obj}=    load json from file     C:\\dev\\robotframework\\001rfprojectdemo\\Data\\profile.json

    ${name_value}=    get value from json   ${json_obj}   $.firstName
    Should Be Equal    ${name_value[0]}    Awase

    ${street_value}=    get value from json   ${json_obj}   $.address.streetAddress
    Should Be Equal    ${street_value[0]}    lakeshore road



TestCase16002 JSON Response Validation
    Create Session    websession    ${base_url}
    ${response}=    Get Request    websession    rest/v2/alpha/IN
    ${cntry_json}=    To Json    ${response.content}
    #singledata validation
    ${cntry_name}=    get value from json   ${cntry_json}   $.name
    Log To Console    ${cntry_name[0]}
    #verifying
    Should Be Equal    ${cntry_name[0]}    India
    #single data validation in array
    ${cntry_brdr}=    get value from json   ${cntry_json}   $.borders[0]
    Log To Console    ${cntry_brdr[0]}
    Should Be Equal    ${cntry_brdr[0]}    AFG
    #multiple data validation

    ${m_cntry_brds}=    get value from json   ${cntry_json}   $.borders
    Log To Console    ${cntry_brdr[0]}
    Should Contain Any    ${cntry_brdr[0]}    AFG   BGD   BTN   MMR   CHN   NPL   PAK   LKA
