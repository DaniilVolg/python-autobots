from pprint import pprint


def test_copart_porsche_model_count(py):
    py.visit('https://copart.com')
    py.get('#input-search').type('Porsche')
    py.get('[type="submit"]').click()
    py.get('[name="serverSideDataTable_length"]').select('100').click()
    #py.wait(5)
    assert py.find('[data-uname="lotsearchLotnumber"]').should().have_length(100)
    lotsearchLotmodel = dict()
    for maker in py.find('[data-uname="lotsearchLotmodel"]'):
        if maker.text() in lotsearchLotmodel:
            lotsearchLotmodel[maker.text()] += 1
        else:
            lotsearchLotmodel[maker.text()] = 1
    pprint(lotsearchLotmodel)


    lotdetailPrimarydamage = dict()
    for damage in py.find("[data-uname='lotsearchLotdamagedescription']"):
        if damage.text() in lotdetailPrimarydamage:
            lotdetailPrimarydamage[damage.text()] += 1
        else:
            lotdetailPrimarydamage[damage.text()] = 1

    pprint(lotdetailPrimarydamage)
