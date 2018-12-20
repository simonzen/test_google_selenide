import pytest

def test_google_selenide(app):
    app.open_url('https://www.google.com/ncr', 'Google')
    app.fill_search_field('Selenide')
    app.get_first_link()
    app.switch_to('Images')
    app.check_image_belog_to('selenide')
    app.switch_to('All')
    app.get_first_link()


if __name__ == '__main__':
    pytest.main()
