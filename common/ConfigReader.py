'''
Created on Dec 21, 2019

@author: Suchita
'''
import configparser

class ConfigReader(object):

    def initConfig(self):
        self.config = configparser.ConfigParser()
        # self.config.read('config/config.ini')
        self.config.read('../config/config.ini')

    def __init__(self):
        self.initConfig()

    def getValue(self, key):
        return self.config['common'][key]

    def getUrl(self):
        return self.config['common']['baseUrl']

    def getBrowser(self):
        return self.config['common']['browser']

    def getPlatform(self):
        return self.config['common']['platform']
    


'''c = ConfigReader()
print(c.getUrl())
print(c.getBrowser())
print(c.getPlatform())'''
