from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import getpass

email = "alexagyeman98@gmail.com"
password = getpass.getpass("Password: ")
app_dir = 'chromedriver.exe'

google_form_url = "https://docs.google.com/forms/d/e/1FAIpQLSfZ2I7CwNezQmhC0g81es8LPAhAgoeGzmqzT3ud82N8ntHjyQ/viewform?edit_requested=true"
stackoverflow_url = 'https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f'

driver = webdriver.Chrome(app_dir)

driver.get(stackoverflow_url)

#username_input = '//*[@id="identifierId"]'
#next_submit = '//*[@id="identifierNext"]/span/span'
#password_input = '//*[@id="password"]/div[1]/div/div[1]/input'
#login_submit = '//*[@id="passwordNext"]'

first_page = '//*[@id="openid-buttons"]/button[1]'
username_input = '//*[@id="identifierId"]'
next_submit = '//*[@id="identifierNext"]/span/span'
password_input = '//*[@id="password"]/div[1]/div/div[1]/input'
login_submit = '//*[@id="passwordNext"]'

alert = "/html/body/div[2]/div/div[2]/div[3]/div[2]/span/span"
edit_reponse = 'https://docs.google.com/forms/d/e/1FAIpQLSfZ2I7CwNezQmhC0g81es8LPAhAgoeGzmqzT3ud82N8ntHjyQ/viewform?edit_requested=true&pli=1&edit2=2_ABaOnufze5g1lN4PCQyPqqTzrjM9Ph6brDd3fmiPqj6fJUF78sx-jA2kuw'
name = '//*[@id="mG61Hd"]/div/div/div[2]/div[1]/div/div[2]/div/div[1]/div/div[1]/input'
gender = '//*[@id="mG61Hd"]/div/div/div[2]/div[2]/div/div[2]/div/span/div/div[1]/label/div'
form_email = '//*[@id="mG61Hd"]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/div/div[1]/input'
form_next_button = '//*[@id="mG61Hd"]/div/div/div[3]/div[1]/div/div'
form_school = '//*[@id="mG61Hd"]/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/input'
form_address = '//*[@id="mG61Hd"]/div/div/div[2]/div[3]/div/div[2]/div[1]/div[2]/textarea'
form_phone = '//*[@id="mG61Hd"]/div/div/div[2]/div[4]/div/div[2]/div/div[1]/div/div[1]/input'
form_comments = '//*[@id="mG61Hd"]/div/div/div[2]/div[5]/div/div[2]/div[1]/div[2]/textarea'
form_submit = '//*[@id="mG61Hd"]/div/div/div[3]/div[1]/div/div[2]/span'

time.sleep(5)
driver.find_element_by_xpath(first_page).click()
time.sleep(3)
driver.find_element_by_xpath(username_input).send_keys(email)
driver.find_element_by_xpath(next_submit).click()
time.sleep(3)
driver.find_element_by_xpath(password_input).send_keys(password)
driver.find_element_by_xpath(login_submit).click()
time.sleep(3)
driver.get(google_form_url)
time.sleep(5)
driver.find_element_by_xpath(name).send_keys("Alexander Agyeman-Nimako")
driver.find_element_by_xpath(gender).click()
time.sleep(3)
driver.find_element_by_xpath(form_email).send_keys(email)
driver.find_element_by_xpath(form_next_button).click()
driver.find_element_by_xpath(form_school).send_keys("Ho Technical University")
driver.find_element_by_xpath(form_address).send_keys("HB25/D Haatso-Ecomog")
driver.find_element_by_xpath(form_phone).send_keys("0559422742")
driver.find_element_by_xpath(form_comments).send_keys("Hello! Nice to meet you.")
driver.find_element_by_xpath(form_submit).click()
time.sleep(5)
driver.close()
























