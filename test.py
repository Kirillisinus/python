import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def setup(browser):
    pass

def extract_numeric_part(text):
    return ''.join(char for char in text if char.isdigit())

@pytest.fixture(params=[22200000000, 1.5 * 10**7, 5 * 10**7, 10**8, 5 * 10**8, 10**9, 1.5 * 10**9])
def min_visitors(request):
    return request.param

def test_popularity_check(browser, setup, min_visitors):
    browser.get("https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites")

    rows = browser.find_elements(By.XPATH, "//caption[contains(text(),\"Programming languages used in most popular websites*\")]/following-sibling::tbody//tr")

    errors = []
    for row in rows[1:]:
        popularity_text = row.find_element(By.XPATH, ".//td[2]").text
        popularity = extract_numeric_part(popularity_text)

        if int(popularity) < min_visitors:
            name = row.find_element(By.XPATH, ".//td[1]").text
            frontend = row.find_element(By.XPATH, ".//td[3]").text
            backend = row.find_element(By.XPATH, ".//td[4]").text

            error_message = (
                f"{name} (Frontend:{frontend}|Backend:{backend}) "
                f"has {popularity} unique visitors per month. (Expected more than {min_visitors})"
            )
            errors.append(error_message)

    assert not errors, "\n".join(errors)

def test_website_popularity_check(min_visitors):
    pass
