import exceptiongroup
from Tools.scripts.fixcid import err
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import *

import time

HOST = "https://demoqa.com/automation-practice-form"
try:
    # created the object for chromedriver that talks to Chrome Browser
    chr_options = Options()
    chr_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chr_options)
    print('maximizing the browser window')
    driver.maximize_window()
    driver.implicitly_wait(20)

    print("Starting test with various locator to use in find_element() method.")
    driver.get(HOST)
    time.sleep(5)

    # webdriver Properties
    print("This is my current URL", driver.current_url)
    print("driver.name:", driver.name)
    print("driver.title: ", driver.title)
    print("driver.current_windows_handle:", driver.current_window_handle)
    print("driver.window_handles:", driver.window_handles)
    time.sleep(5)
    print("# WebDriver Methods:--------------")
    next_page = "https://www.google.com/"
    driver.get(next_page)
    driver.back()
    print("we are here now: (qa tools)", driver.current_url)
    driver.forward()
    print("we are here now(google):", driver.current_url)
    driver.refresh()
    print("we are here to refresh:(google)", driver.current_url)
    print("#switching between browser windows or tabs")
    # we are on /browser-windows page, get current window handle
    driver.get(HOST)
    first_window_handle = driver.current_window_handle
    print("Id of the first page opened", first_window_handle)
    # click on new tab button
    driver.find_element(By.ID, "tabButton").click()
    # now we have two tabs,switch to the second, get window handles(list),
    handles = driver.window_handles
    print("Ids of all tabs/windows open", handles)
    print("current browser windows id", driver.current_window_handle)
    # tabs are in order handles=[idoffirsttab,idofsecondtab]
    # switch to the second , switch to handles
    print("switching to the new window or tab")
    driver.switch_to.windows_handles(handles[1])
    print("current url", driver.current_url)
    driver.switch_to.window(handles[0])

    # All locators
    # enter FirstName, enter LastName, enter Email = 'jdoe@email.com'
    fn_input = 'firstName'
    ln_input = 'lastName'
    Email_input = 'userEmail'
    # select Gender=Male
    gender_male = 'gender-radio-1'

    # mobileNumber= 9876543210
    mobile_number_input = 'userNumber'
    # enter date_of_birth = 27 nov 2000
    # optional
    # enter subjects = "selenium form testing'
    # select checkboxes, select Sports, reading
    hobbies_sp = "hobbies-checkbox-1"
    hobbies_reading = "hobbies-checkbox-2"
    # select (optional) upload picture
    # enter message in text area = "2906 Shell road, 12224"
    address_textarea = "currentAddress"
    # check is city list is enabled
    upload_pic_input = 'uploadPicture'
    city_list = "react_select_3_input"
    # select state =NCR
    state_list = "react_select_4_input"
    submit_button = 'submit'
    confirmation_msg = 'example-modal-sizes-title-lg'
    # select city = Delhi
    date_of_birth = "dateOfBirthInput"
    # check if Male gender is selected
    # check if sports hobbies are selected
    # click submit
    # verify the message:= "Thanks for submitting the form"
    close_cm_button = "closeLargeModal"



except Exception as err:

    print(err)
    print("Python: Test failed with above exception")
except NoSuchElementException as err:
    print(err)
    print("Selenium: Test failed with above exception")
finally:
    # close all the tabs
    driver.quit()
    # pass
