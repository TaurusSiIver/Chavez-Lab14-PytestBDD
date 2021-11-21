from pytest_bdd import scenarios, parsers, given, when, then
import pytest
from full_ret_calc import *

EXTRA_TYPES = {
    'Number': int,
}

scenarios('../features/full_ret_calc.feature')

# test year
@given(parsers.cfparse('the year of birth is "{year:Number}"', extra_types=EXTRA_TYPES), target_fixture='year')
@given('the year of birth is "<year>"', target_fixture='year')
def year(year):
    return calculate_retirement_age(year)


@then(parsers.cfparse('the retirement age is "{ret_year:Number}" and retirement month is "{ret_month:Number}"',
                      extra_types=EXTRA_TYPES))
@then('the retirement age is "<ret_year>" and retirement month is "<ret_month>"')
def calculate_retirement_age_range(year, ret_year, ret_month):
    expected = (ret_year, ret_month)
    assert year == expected


# test all dates
@given(parsers.cfparse(
    'the "{birth_year:Number}", "{birth_month:Number}", "{age_year:Number}", and "{age_month:Number}"',
    extra_types=EXTRA_TYPES), target_fixture='all_date_months')
@given('the "<birth_year>", "<birth_month>", "<age_year>", and "<age_month>"', target_fixture='all_date_months')
def all_date_months(birth_year, birth_month, age_year, age_month):
    return calculate_retirement_date(birth_year, birth_month, age_year, age_month)


@then(parsers.cfparse('the expected result is: "{ret_year:Number}" and "{ret_month:Number}"',
                      extra_types=EXTRA_TYPES))
@then('the expected result is: "<ret_year>" and "<ret_month>"')
def assertion_month_dates(all_date_months, ret_year, ret_month):
    expected = (ret_year, ret_month)
    assert all_date_months == expected


# validate birth year: full Retirement age calculator with values less than 1900
@given(parsers.cfparse('the birth year "{year:Number}" less than', extra_types=EXTRA_TYPES), target_fixture='year_less_than')
@given('the birth year "<year>" less than', target_fixture='year_less_than')
def year_less_than(year):
    return year


@then('I should not see the error message')
def if_birth_year_less_than_1900(year_less_than):
    with pytest.raises(ValueError):
        calculate_retirement_age(year_less_than)


# validate birth year: full Retirement age calculator with values greater than or equal 2019
@given(parsers.cfparse('the birth year "{year:Number}" greater than or equals', extra_types=EXTRA_TYPES), target_fixture='year_greater_than')
@given('the birth year "<year>" greater than or equals', target_fixture='year_greater_than')
def year_greater_than(year):
    return year


@then('I should not see the other error message')
def if_birth_year_greater_than_equal_2019(year_greater_than):
    with pytest.raises(ValueError):
        calculate_retirement_age(year_greater_than)