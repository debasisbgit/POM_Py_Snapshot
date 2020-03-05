from selenium import webdriver
from Library import ConfigReader


def startBrowser():
    bwtype = ConfigReader.readConfigData("Details", "Browser")
    App_URL =  ConfigReader.readConfigData("Details", "App_URL")
    global driver
    print("inside startbrowser",bwtype)
    if bwtype == "Firefox":

        path = ConfigReader.readConfigData("Details", "drvPath")
        driver = webdriver.Firefox(executable_path=path)
        driver.get(App_URL)
        driver.maximize_window()
    elif bwtype == "Chrome":

        path = ConfigReader.readConfigData("Details", "drvPath")
        driver = webdriver.Chrome(executable_path=path)
        driver.get(App_URL)
        driver.maximize_window()
    else:

        path = ConfigReader.readConfigData("Details", "drvPath")
        driver = webdriver.Chrome(executable_path=path)
        driver.get(App_URL)
        driver.maximize_window()

    return driver


def closeBrowser():
    print("inside close bw")
    driver.close()




