Feature: Full Retirement Calculator
  retirement age calculator to find out when you are
  eligible for unreduced retirement benefits based on
  your birth year.

  Scenario Outline: Calculate Retirement Age
    Given the year of birth is "<year>"
    Then the retirement age is "<ret_year>" and retirement month is "<ret_month>"
    Examples:
      | year | ret_year | ret_month |
      | 1937 | 65       | 0         |
      | 1941 | 65       | 8         |
      | 1960 | 67       | 0         |
      | 1947 | 66       | 0         |

  Scenario Outline: Calculate Retirement Date All Months
    Given the "<birth_year>", "<birth_month>", "<age_year>", and "<age_month>"
    Then the expected result is: "<ret_year>" and "<ret_month>"
    Examples:
      | birth_year | birth_month | age_year | age_month | ret_year | ret_month |
      | 1937       | 1           | 65       | 2         | 2002     | 3         |
      | 1939       | 1           | 65       | 4         | 2004     | 5         |
      | 1940       | 1           | 65       | 6         | 2005     | 7         |
      | 1941       | 1           | 65       | 8         | 2006     | 9         |
      | 1942       | 1           | 65       | 10        | 2007     | 11        |
      | 1943       | 1           | 66       | 0         | 2009     | 1         |

  Scenario Outline: Full Retirement Age Calculator With Values Less Than 1900
    Given the birth year "<year>" less than
    Then I should not see the error message
    Examples:
      |  year |
      | -1980 |
      |  1899 |
      |  1800 |

  Scenario Outline: Full Retirement Age Calculator With Values Greater Than or Equals 2019
    Given the birth year "<year>" greater than or equals
    Then I should not see the other error message
    Examples:
      |  year |
      |  2019 |
      |  2020 |
      |  2021 |
