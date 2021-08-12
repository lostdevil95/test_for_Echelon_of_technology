from selenium import webdriver
import pytest


link = 'https://gitea.io/en-us/'

@pytest.fixture
def browser():
    capabilities = {
        'browserName': 'chrome',
        'version': '92.0',
        'platform': 'LINUX'
    }
    browser = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=capabilities)
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestGitea:
    def test_mainpage(self, browser):
        print('Запускаем сессию')
        print('Открываем страницу gitea')
        browser.get(link)
        print('Ищем эталонный текст')
        read_text = browser.find_element_by_css_selector('.title.is-1').text
        assert 'Gitea - Git with a cup of tea' == read_text, 'Ошибочка'
        print('Ищем первый элемент')
        first = browser.find_element_by_xpath("//section[@class='hero is-primary homepage-hero']")
        assert first, 'элемент недоступен'
        print('Ищем второй элемент')
        second = browser.find_element_by_xpath("//section[@class='hero is-link feature-shoutout']")
        browser.execute_script('arguments[0].scrollIntoView(true);', second)
        assert second, 'элемент недоступен'
        print('Ищем третий элемент')
        third = browser.find_element_by_css_selector('.hero.feature-shoutout')
        browser.execute_script("return arguments[0].scrollIntoView(true);", third)
        assert third, 'элемент недоступен'
        print('Ищем футер')
        footer = browser.find_element_by_css_selector('footer')
        browser.execute_script("return arguments[0].scrollIntoView(true);", footer)
        assert footer, 'элемент недоступен'



    def test_rega(self, browser):
        browser.get('https://try.gitea.io/')

        browser.find_element_by_css_selector("a[href='/user/sign_up']").click()
        browser.find_element_by_xpath("//input[@id='user_name']").send_keys('Frodo')
        browser.find_element_by_xpath("//input[@id='email']").send_keys('g-unit_m@mail.ru')
        browser.find_element_by_xpath("//input[@id='password']").send_keys('12345678')
        browser.find_element_by_xpath("//input[@id='retype']").send_keys('12345678')
        browser.find_element_by_css_selector('.ui.green.button').click()
