'''
Created on Dec 21, 2019

@author: Suchita
'''
import configparser

class ConfigReader(object):

    def getUrl(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        return self.config['common']['baseUrl']



c = ConfigReader()
print(c.getUrl())
