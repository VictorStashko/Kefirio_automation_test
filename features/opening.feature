@kefirio
Feature: kefirio

  @browser.headless @kefirio1
  Scenario: User opens Kefirio site
    Given user open "https://symphonious-medovik-a6c3d8.netlify.app/" site



  @browser.headless @kefirio2
  Scenario: User gets list of users
    Given user open "https://symphonious-medovik-a6c3d8.netlify.app/" site
    When user fills url page of "GET" "list_users" request
    And user clicks on "Відправити" button
    Then user sees "100" status code


  @browser.headed @kefirio3
  Scenario: User creates new user users
    Given user open "https://symphonious-medovik-a6c3d8.netlify.app/" site
    When user fills url page of "POST" "create" request
    When user chooses "POST" type of the request in dd
    And user fills body of "POST" "create" request
    And user clicks on "Відправити" button
    Then user sees "201" status code
    And user sees response for creating user request