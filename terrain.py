import os
from lettuce import before, world, after
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from features.pages.home_page import HomePage
from features.pages.search_results_page import SearchResultsPage

@before.all
def open_shop():
    open_drivers()
    prepare_pages(world.driver)

@after.all
def close_shop(total):
    print "Total %d of %d scenarios passed!" % (total.scenarios_passed, total.scenarios_ran)
    close_drivers()

def open_drivers():
    world.driver = get_firefox()
    world.driver.set_page_load_timeout(10)
    world.driver.implicitly_wait(10)
    world.driver.maximize_window()
    
def get_firefox():
    # Locate Firefox from the default directory otherwise use FIREFOX_BIN #
    try:
        driver = webdriver.Firefox()
    except Exception:
        my_local_firefox_bin = os.environ.get('FIREFOX_BIN')
        firefox_binary = FirefoxBinary(my_local_firefox_bin)
        driver = webdriver.Firefox(firefox_binary=firefox_binary)
    return driver

def prepare_pages(driver):
    world.home_page = HomePage(driver)
    world.search_results_page = SearchResultsPage(driver)

def close_drivers():
    if world.driver:
        world.driver.quit()