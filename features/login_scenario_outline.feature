Feature: Check different Login combinations

  @outline
  Scenario Outline: Check Login with different Credentials

    When user enters "<username>" and "<password>"
    Then login activities should take place


    Examples: Credentials
   | username          | password   |
   | gvigne22@ford.com | Ford@2023! |
   | gvigne22@ford.com | Ford@2022  |

