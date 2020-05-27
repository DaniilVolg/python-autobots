def test_ch61(py):
    py.visit('https://www.copart.com/')
    py.get("#input-search", timeout=10).type("Nissan", Keys.ENTER)
    py.get("input[type='search']").type("SKYLINE").click()
    try:
        assert py.contains('SKYLINE22')
    except:
        "Could not find element with the text ``SKYLINE22``"

    py.screenshot('../screenshots/test_challenge6_model_not_found.png')
