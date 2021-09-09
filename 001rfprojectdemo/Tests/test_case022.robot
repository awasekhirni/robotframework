##Awase Khirni Syed awase008@gmail.com Elain Technologies Inc Canada
#File Processing Operations using robot framework

***Settings***
Library   OperatingSystem
Library   String
Library   Collections

***Variables***
${file_path}    C:\\dev\\robotframework\\001rfprojectdemo\\Data\\sample.csv

***Test Cases***
Process Data File
    [Tags]  file-reading
    ${File_Content}=    Get File    ${file_path}
    Log File    Content:${File_Content}
    @{Lines}=   Split To Lines and Remove Header    ${File_Content}
    Log To Console    ${Lines}

***Keywords***
Split to Lines and Remove Header
    [Arguments]    ${File_Content}
    @{Lines}=    Split To Lines    ${File_Content}
    Remove From List    ${Lines}    0
    [Return]    @{Lines}
