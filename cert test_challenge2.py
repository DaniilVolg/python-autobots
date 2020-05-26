from selenium.webdriver.common.keys import Keys


def test_challenge2(py):
    py.visit('https://copart.com')
    py.get('#input-search').type('exotics', Keys.ENTER)
    assert py.contains('PORSCHE')
