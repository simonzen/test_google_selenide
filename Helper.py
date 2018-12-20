from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Application:

    def __init__(self):
        self.wd = webdriver.Chrome('/home/simon/PycharmProjects/web_drivers/chromedriver')
        self.wait = WebDriverWait(self.wd, 100)

    def open_url(self, URL, title):
        wd = self.wd
        wait = self.wait

        wd.get(URL)
        wait.until(EC.title_is, title)

    def destroy(self):
        wd = self.wd
        wd.quit()

    def switch_to(self, value):
        wd = self.wd
        wait = self.wait
        button = wd.find_element_by_xpath(f'//a[contains(text(),"{value}")]')
        button.click()
        wait.until(EC.title_is)

    def fill_search_field(self, value):
        wd = self.wd
        box = wd.find_element_by_name('q')
        box.clear()
        box.send_keys(value)
        box.submit()

    def get_first_link(self):
        wd = self.wd
        element = wd.find_element_by_xpath('//div[@class="r"]/a')
        link = element.get_attribute("href")
        assert (link == 'https://selenide.org/'), 'Первая ссылка на selenide.org'
        return link

    def check_image_belog_to(self, ethalon):
        wd = self.wd
        image_text = wd.find_elements_by_xpath(f'//div[@data-ri="0"]//a[position() mod 2 = 0]//div')
        image_text = [i.text.lower() for i in image_text]
        for text in image_text:
            if ethalon in text:
                fl = True
        assert (fl is True), 'Первое изображение не относится к запросу'
