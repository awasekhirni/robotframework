#Awase Khirni Syed awase008@gmail.com Elain Technologies Inc Canada
# validating headers and cookies of REST API
***Settings***
Library   RequestsLibrary
Library   Collections

***Variables***

${base_url}   http://jsonplaceholder.typicode.com

***Keywords***


***Test Cases***
TestCase_18001 Validating Headers from RESTAPI
    Create Session    restSession    ${base_url}
    ${myresponse}=    Get On Session    restSession    /photos
    Log To Console    ${myresponse.headers}

    ${header_dict_val_ct}=   Get From Dictionary    ${myresponse.headers}    Content-Type
    Should Be Equal    ${header_dict_val_ct}    application/json; charset=utf-8

    ${header_dict_val_ce}=    Get From Dictionary    ${myresponse.headers}    Content-Encoding
    Should Be Equal    ${header_dict_val_ce}    gzip



TestCase_18002 Extracting and Validating Cookies from RESTAPI
    Create Session    cSession    ${base_url}
    ${c_response}=    get On Session   cSession    /photos
    #displaying all the cookies associated with the url
    Log To Console    ${c_response.cookies}

    # to capture the cookie value
    ${cookie_jar_dict}=   Get From Dictionary    ${c_response.cookies}    _cfduid
    Log To Console    ${cookie_jar_dict}
