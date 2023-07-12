Feature: Check login feature

  @search
  @sanity
  Scenario: Valid credentials

    When user enters valid username and password
    Then login should be successful

  @smoke
  Scenario: Invalid credentials

    When user enters invalid username and password
    Then login should fail
