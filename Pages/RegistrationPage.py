from Library import ConfigReader
from Library import ConfigReader
import time
from selenium import webdriver



class registrationclass:
    def __init__(self, obj):
        global dri
        dri = obj

    def enter_kwsearch(self):

        dri.find_element_by_css_selector\
            ("#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input").send_keys("taj mahal")
        #whereever is required to take screen shot use this line of code
        #dri.get_screenshot_as_file("./mysnap.png")






