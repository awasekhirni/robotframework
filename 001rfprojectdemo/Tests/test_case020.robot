#Awase Khirni Syed awase008@gmail.com Elain Technologies Inc Canada
# File Checking
***Settings***
Resource    ../Resources/Sample_resource.robot


***Variables***



***Keywords***

***Test Cases***

Check for XMLFile
    Check for file   C:\\dev\\robotframework\\001rfprojectdemo\\Data\\book_catalog.xml

Check how to write a file
    Check how to write a file     C:\\dev\\robotframework\\001rfprojectdemo\\Data\\    test_1.txt    This is a sample text    UTF-8

Check removing file
    Check how to remove a file     C:\\dev\\robotframework\\001rfprojectdemo\\Resources\\    test_1.txt
