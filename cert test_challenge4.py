def test_challenge44_copart(py):
    py.visit('https://copart.com')
    popular_models = py.find("li[ng-repeat*='popularSearch in popularSearches'] > a")
    for model in popular_models:
        print(f'{model.text} - {model.get_attribute("href")}')
    assert py.should('popular_models.length == 20')
