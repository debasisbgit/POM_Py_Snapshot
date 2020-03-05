import configparser


def readConfigData(section, key):
    config = configparser.ConfigParser()
    config.read("F:/_PytestPOM_Selenium/ConfigurationFiles/Config.cfg")
    print(config.get(section, key))
    return config.get(section, key)


def fetchElementLocators(section, key):
    config = configparser.ConfigParser()
    config.read("F:/_PytestPOM_Selenium/ConfigurationFiles/Elements.cfg")
    return config.get(section, key)



