def test_challenge3(py):
    py.visit('https://copart.com')
    popular_models = py.find("li[ng-repeat*='popularSearch']>a")
    for model in popular_models:
        print(f'{model.text()} - {model.get_attribute("href")}')
    assert popular_models.should().have_length(20)
