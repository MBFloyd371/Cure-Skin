Feature: Test Main Page

  Scenario: Check if there are mismatch numbers
    Given Open Main Page
    Then Verify phone number in correct order


  Scenario: Check for Grammar Errors on headline
    Given Open Main Page
    Then Verify the word favorites is spelled correctly


  Scenario: Check for any cross-outs
    Given Open Main Page
    Then Verify the word fair is deleted