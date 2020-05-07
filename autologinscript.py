from selenium import webdriver
import webbrowser
import time
import subprocess

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("path")

driver.get("https://www.facebook.com")

username = "xyz"
password = "xyz"
time.sleep(4)
username_textbox = driver.find_element_by_id('gwt-uid-1')
username_textbox.send_keys(username)
password_textbox = driver.find_element_by_id('gwt-uid-2')
password_textbox.send_keys(password)
time.sleep(2)

submit = driver.find_element_by_css_selector('button.btn.btn-primary.btn-block')
submit.click()
time.sleep(5)

model_button = driver.find_element_by_id('automationButton1')
if (model_button):
    model_button.click()
time.sleep(10)

option = driver.find_element_by_id('gwt-uid-10')
option.click()
time.sleep(3)

select = driver.find_element_by_xpath('//*[@id="gwt-uid-10"]/select/option[2]')
select.click()
time.sleep(2)


nextbtn = driver.find_element_by_id('automationTestingIdSaveCamapignLink')
nextbtn.click()
time.sleep(3)

extension = driver.find_element_by_id('gwt-uid-35')
extension.click()
time.sleep(3)

tata = driver.find_element_by_xpath('//*[@id="gwt-uid-35"]/select/option[4]')
tata.click()
time.sleep(1)

number = driver.find_element_by_id('gwt-uid-37')
number.send_keys('xyz')
time.sleep(3)

final_submit=driver.find_element_by_id('automationTestingIdSaveExtension')
final_submit.click()
time.sleep(3)

status=driver.find_element_by_id('automationTestingIdUserAvalability')
status.click()
time.sleep(3)

available = driver.find_element_by_css_selector('#statusDropdown > li > a > span')
available.click()
time.sleep(2)


call_panner = driver.find_element_by_id('automationTestingIdCallPanelIcon')
call_panner.click()
time.sleep(2)

dialler = driver.find_element_by_id('gwt-uid-86')
dialler.send_keys("xyz", Keys.ENTER)
time.sleep(2)

