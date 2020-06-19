from pprint import pprint


MAKES_AND_MODELS = "[href*='popular/m']"
MAKES_A_MODELS = "//a[contains(@href, 'popular/make') or contains(@href, 'popular/model')]"


def test_challenge_7(py):
    py.visit('https://www.copart.com')
    cars = []

    for make_model in py.find_xpath(MAKES_A_MODELS):
        name = make_model.text()
        url = make_model.get_attribute('href')
        cars.append([name, url])
    pprint(cars)

    for car in cars:
        name, url = car
        py.visit(url)
        assert py.contains(name.lower())
