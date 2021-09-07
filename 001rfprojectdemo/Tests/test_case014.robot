#Awase Khirni Syed awase008@gmail.com Elain Technologies Inc Canada
#API testing demo with robot framework
***Settings***
Documentation   API Testing in Robot Framework
Library   RequestsLibrary
Library   Collections



***Variables***

${BASE_URL}   https://jsonplaceholder.typicode.com



***Keywords***


***Test Cases***
Test API POSTS_ENDPOINT
    Create Session    GET_POSTS    ${BASE_URL}
    ${response}=    get request   Get_POSTS   /posts
    Log To Console    ${response.status_code}
    Log To Console    ${response.content}
    #validations
    ${status_code}=   Convert To String    ${response.status_code}
    Should Be Equal    ${status_code}    200
    ${body}=    Convert To String    ${response.content}
    Should contain    ${body}   sunt aut facere repellat provident occaecati excepturi optio reprehenderit


Test API COMMENTS_ENDPOINT
    Create Session    GET_COMMENTS    ${BASE_URL}
    ${response}=    get request   Get_POSTS   /comments
    Log To Console    ${response.status_code}
    Log To Console    ${response.content}


Test API ALBUMS_ENDPOINT
    Create Session    GET_ALBUMS    ${BASE_URL}
    ${response}=    get request   Get_ALBUMS   /albums
    Log To Console    ${response.status_code}
    Log To Console    ${response.content}


Test API PHOTOS_ENDPOINT
    Create Session    GET_PHOTOS    ${BASE_URL}
    ${response}=    get request   Get_PHOTOS   /photos
    Log To Console    ${response.status_code}
    Log To Console    ${response.content}


Test API TODOS_ENDPOINT
    Create Session    GET_TODOS   ${BASE_URL}
    ${response}=    get request   Get_TODOS   /todos
    Log To Console    ${response.status_code}
    Log To Console    ${response.content}



Test API USERS_ENDPOINT
    Create Session    GET_USERS    ${BASE_URL}
    ${response}=    get request   Get_USERS   /users
    Log To Console    ${response.status_code}
    Log To Console    ${response.content}
