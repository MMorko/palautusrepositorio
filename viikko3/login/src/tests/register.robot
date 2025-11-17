*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  kalle123
    Set Password  kalle123
    Click Button  Register
    Welcome Page Should Be Open

Register With Too Short Username And Valid Password
    Set Username  a
    Set Password  kalle123
    Click Button  Register
    Register Should Fail With Message  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username  kalle
    Set Password  123
    Click Button  Register
    Register Should Fail With Message  Password must be at least 8 characters long and not be entirely letters

Register With Valid Username And Invalid Password
    Set Username  kalle
    Set Password  **
    Click Button  Register
    Register Should Fail With Message  Password must be at least 8 characters long and not be entirely letters

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Input Password  password  kalle123
    Input Password  password  kalle1234
    Click Button  Register
    Register Should Fail With Message  Password and password confirmation do not match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle123
    Click Button  Register
    Register Should Fail With message  User with username kalle already exists

*** Keywords ***
Register Should Succeed
    Main Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}
    Input Password  password_confirmation  ${password}

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page