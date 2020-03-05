from Base import InitiateDriver
from Pages import RegistrationPage
from selenium import webdriver
from TestCases import takescshot

import time

def test_ValidateRegistration():
    print("inside validate method")
    drv = InitiateDriver.startBrowser()
    print(drv)
    reg = RegistrationPage.registrationclass(drv)
    #reg.enter_kwsearch()
    takescshot.take_page_screenshot(drv, "mysnap3.png")


#test_ValidateRegistration()


