from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    chrome_driver = webdriver.Chrome()

    chrome_driver.get("https://www.payoneer.com/ru/")
    chrome_driver.maximize_window()

    locale_dropdown = chrome_driver.find_element(by=By.XPATH, value='''//*[@id="mm-1"]/div[1]/div/header/div/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div/ul/li/a''')
    locale_dropdown.click()
    ukrainian_locale_button = chrome_driver.find_element(by=By.XPATH, value='''//*[@id="mm-1"]/div[1]/div/header/div/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div/ul/li/ul/li[8]/a''')
    ukrainian_locale_button.click()

    login_button = chrome_driver.find_element(by=By.XPATH, value='''//*[@id="menu-item-125129"]/a''')
    if login_button:
        print('success')
    else:
        print('test failed')


if __name__ == '__main__':
    main()