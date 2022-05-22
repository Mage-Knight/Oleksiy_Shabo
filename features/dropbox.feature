Feature: Dropbox WebAPI test

  Scenario Outline: Test uploading file to Dropbox
    Given I have a file named "<file>"
    When I upload "<file>" to Dropbox
    Then I should see "<file>" uploaded

    Examples:
      | file             |
      | cat.jpg          |
      | calculations.txt |
      | lorem_ipsum.pdf  |
      | birds.mp3        |

  Scenario Outline: Getting file metadata from Dropbox
    Given I have a file named "<file>" uploaded
    When I send request to get "<file>" metadata from Dropbox
    Then I should see "<file>" metadata

    Examples:
      | file             |
      | cat.jpg          |
      | calculations.txt |
      | lorem_ipsum.pdf  |
      | birds.mp3        |
      
  Scenario Outline: Deleting file from Dropbox
    Given I have a file named "<file>" uploaded
    When I send request to delete "<file>" from Dropbox
    Then "<file>" should be deleted

    Examples:
      | file             |
      | cat.jpg          |
      | calculations.txt |
      | lorem_ipsum.pdf  |
      | birds.mp3        |