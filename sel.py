
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

path = 'geckodriver.exe'


def get_timetable(url, u, pw, c):
    Fire = webdriver.Firefox(executable_path=path)
    Fire.implicitly_wait(5)
    with Fire as driver:
        wait = WebDriverWait(driver, 10)
        driver.set_window_size(2000, 1600)
        driver.get(url)
        time.sleep(1)
        user = driver.find_element_by_id('loginuser')
        user.click()
        user.send_keys(u)
        passw = driver.find_element_by_id('loginpassword')
        passw.click()
        passw.send_keys(pw)
        sub = driver.find_element_by_css_selector('.login--school-login--login-button')
        sub.click()
        driver.get('https://intranet.tam.ch/krm/calendar/index/period/71')
        time.sleep(4)
        driver.set_window_size(2000, 1600)
        filt = driver.find_element_by_xpath('//*[@id="tta-header"]/div[2]/ul[2]')
        filt.click()
        time.sleep(1)
        me = driver.find_element_by_css_selector('#tta-scheduler-options-student_taglist > li > span.k-select')
        me.click()
        time.sleep(1)

        clas = driver.find_element_by_css_selector('#tta-scheduler-options-form > div:nth-child(2) > div > input')
        clas.click()
        time.sleep(1)
        clas.send_keys(c)
        time.sleep(1)
        clas.send_keys(u'\ue007')

        sub = driver.find_element_by_xpath('//*[@id="tta-scheduler-options-functions"]/button[2]')
        time.sleep(2)
        sub.click()
        time.sleep(4)
        driver.get_screenshot_as_file('timetable.png')


