Feature: Zen Portal Login

  Scenario: Successful Login
    Given user is on login page
    When user enters valid username and password
    And clicks login button
    Then user should be logged in successfully

  Scenario: Unsuccessful Login
    Given user is on login page
    When user enters invalid username and password
    And clicks login button
    Then error message should be displayed

  Scenario: Validate input fields
    Given user is on login page
    Then username and password fields should be visible

  Scenario: Validate logout
    Given user is logged in
    When user clicks logout
    Then user should be logged out successfully