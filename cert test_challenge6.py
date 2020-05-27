
from selenium.webdriver.common.keys import Keys

from copart_com.pages.home import HomePage




def test_challenge6(py):
    
    py.visit('https://www.copart.com/')
    py.get("#input-search", timeout=10).type("Nissan", Keys.ENTER)
    py.get("input[type='search']").type("SKYLINE").click()
    try:
        assert py.contains('SKYLINE22')
    except:
        "Could not find element with the text ``SKYLINE22``"

    py.screenshot('../screenshots/test_challenge6_model_not_found.png')
    
    
    def test_challenge6_POM(py):
    results_page = HomePage(py).visit().search('nissan')
    results_page.filter_search("SKYLINE")
    try:
        assert py.contains('SKYLINE22')
    except:
        "Could not find element with the text ``SKYLINE22``"
    py.screenshot('../screenshots/test_challenge6_model_not_found.png')
