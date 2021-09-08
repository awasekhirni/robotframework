#Awase Khirni Syed awase008@gmail.com Elain Technologies Inc Canada
#Data validation in XML file
#http://xpather.com
***Settings***
Library   XML
Library   os
Library   Collections
Library   RequestsLibrary

***Variables***
${file_location}    C:\\dev\\robotframework\\001rfprojectdemo\\Data\\book_catalog.xml
${xml_base_url}     https://www.w3schools.com/

***Keywords***


***Test Cases***

TestCase_17001
    ${book_xml}=    Parse Xml    ${file_location}

    @{header}=    Get Elements    ${book_xml}   *
    ${elemList}=    Get Elements    ${header}[0]    *
    @{elemList}=    Convert To List    ${elemList}
    &{xmlDict}=    Create Dictionary
    FOR    ${item}    IN    @{elemList}
        Set to Dictionary    ${xmlDict}    ${item.tag}=${item.text}
    END
    Log To Console    ${xmlDict}

    #validations
    ${book_ttl}=    Get Element Text    ${book_xml}   .//book[1]/title
    Log To Console    ${book_ttl}
    Should Be Equal    ${book_ttl}    XML Developer's Guide

    #approach 2
    ${book_elem}=   Get Element    ${book_xml}    .//book[1]/title
    Should Be Equal    ${book_elem.text}    XML Developer's Guide

    #approach 3
    Element Text Should Be    ${book_xml}    XML Developer's Guide   .//book[1]/title

    #get the element count
    ${elemcount}=   Get Element Count    ${book_xml}    .//book

    Log To Console    ${elemcount}
    Should Be Equal As Integers    ${elemcount}    12

    #check element attributes
    Element Attribute Should Be    ${book_xml}    id    bk103   .//book[3]
    Element Attribute Should Be    ${book_xml}    id    bk112   .//book[12]

    #capturing the child elements of a selected parent element
    ${child_elements}=    Get Child Elements    ${book_xml}   .//book[4]
    Log To Console    ${child_elements}
    Should Not Be Empty    ${child_elements}

    #extracting elements
    ${author}=    Get Element Text    ${child_elements[0]}
    ${title}=     Get Element Text    ${child_elements[1]}
    ${genre}=     Get Element Text    ${child_elements[2]}
    ${price}=     Get Element Text    ${child_elements[3]}
    ${publish_date}=    Get Element Text    ${child_elements[4]}
    ${description}=     Get Element Text    ${child_elements[5]}
    Log To Console    ${author}
    Log To Console    ${title}
    Log To Console    ${genre}
    Log To Console    ${price}
    Log To Console    ${publish_date}
    Log To Console    ${description}

    Should Be Equal    ${author}    Corets, Eva
    Should Be Equal    ${genre}    Fantasy




TestCase_170002 XML Response Validation
    Create Session    xmlwebsession   ${xml_base_url}   verify=true
    ${xml_response}=    Get On Session    xmlwebsession    xml/cd_catalog.xml
    ${xml_string}=    Convert To String    ${xml_response.content}
    ${xml_obj}=   Parse Xml    ${xml_string}

    ${child_elements}=    Get Child Elements    ${xml_obj}
    Should Not Be Empty    ${child_elements}

    ${el_count}=  Get Element Count    ${xml_obj}   .//CD
    Log To Console    ${el_count}
    Should Be Equal As Integers    ${el_count}    26
