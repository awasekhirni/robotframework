***Settings***
Library   RequestsLibrary
Library   Collections
Library   JSONLibrary

Suite SetUp   Create Session    jsonplaceholder    http://jsonplaceholder.typicode.com
***Variables***


***Keywords***

***Test Cases***
#POST request operation involves
#- adding a new resource
#- save response
# validate status code
# validate response content
# TestCase POSTOPERATIONS CREATING A NEW RESOURCE
#     Create Session    AddData    ${BASE_URL}    verify=true
#     &{body}=    Create Dictionary    first_name=Awase   middle_name=Sadath    last_name=Syed    date_of_birth=1/1/1999
#     ${header}=    Create Dictionary    Content-Type=application/json
#     ${response}=    Post on Session    AddData    /api/studentsDetails    data=${body}    headers=${header}
#     Log To Console    ${response.status_code}
#     Log To Console    ${response.content}
#
#     #validations
#     ${res_body}=    Convert To String    ${response.content}
#     ${code_httpstatus}=   Convert To String    ${response.status_code}
#     Should Be Equal    ${code_httpstatus}    201

#create operation code
Test Case Add a new article
    &{data}=    Create dictionary  title=Hakuna Matata What a wonderful world  body=Mike Testing 123  userId=1
    ${resp}=    POST On Session    jsonplaceholder  /posts  json=${data}  expected_status=anything
    Log To Console    ${resp.status_code}
    Log To Console    ${resp.content}
    Status Should Be                 201  ${resp}
    ${http_statuscode}=   Convert To String    ${resp.status_code}
    Should Be Equal    ${http_statuscode}    201

#get operation code
Test Case Get an existing todo
    Create Session    GET_TODOS   https://jsonplaceholder.typicode.com/todos/1
    ${todo_response}=    get request   Get_TODOS   /todos
    Log To Console    ${todo_response.status_code}
    Log To Console    ${todo_response.content}
    #validation
    ${http_stat}=   Convert To String    ${todo_response.status_code}
    Should Be Equal    ${http_stat}    200

    ${res_body}=    Convert To String    ${todo_response.content}
    Should Contain    ${res_body}    delectus aut autem


#update operation Code
Test Case Update an existing task
    &{data}=    Create dictionary  userid=1   id=1    title=sheerkhorma  completed=true
    ${header}=    Create Dictionary    Content-Type=application/json
    ${do_resp}=    PUT On Session    jsonplaceholder  /todos/1   json=${data}  headers=${header}
    Log To Console    ${do_resp.status_code}
    Log To Console    ${do_resp.content}
    Status Should Be                 200  ${do_resp}
    ${c_statuscode}=   Convert To String    ${do_resp.status_code}
    Should Be Equal    ${c_statuscode}    200
    ${cres_body}=    Convert To String    ${do_resp.content}
    Should Contain    ${cres_body}    sheerkhorma


#delete operation code
Test Case Delete a user
    Create Session  mysession   http://jsonplaceholder.typicode.com
    ${d_response}=    Delete On Session    mysession    /users/1
    #validations
    ${d_status_code}=   Convert To String    ${d_response.status_code}
    Should Be Equal    ${d_status_code}    200
