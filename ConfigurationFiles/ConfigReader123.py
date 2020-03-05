import configparser


config = configparser.ConfigParser()
config.read("F:/_PytestPOM_Selenium/ConfigurationFiles/Config.cfg")
print(config.get('h1', 'Browser'))

