from lettuce import step, world
from nose.tools import assert_equal, assert_true

@step('Given I navigate to the PyPi Home page')
def step_impl(step):
    world.home_page.navigate("https://pypi.python.org/pypi")
    assert_equal(world.home_page.get_page_title(), "PyPI - the Python Package Index : Python Package Index")

@step('When I search for "([^"]*)"')
def step_impl(step, search_term):
	world.home_page.search(search_term)

@step('Then I am taken to the PyPi Search Results page')
def step_impl(step):
	assert_equal(world.search_results_page.get_page_title(), "Index of Packages Matching 'lettuce' : Python Package Index")

@step('And I see a search result "([^"]*)"')
def step_impl(step, search_result):
	assert_true(world.search_results_page.find_search_result(search_result))
