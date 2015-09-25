'''
Created on 2015/09/20

@author: playerone
'''
import configparser
import os.path

class Config(object):
    
    def __init__(self, configPath):
        self.configPath = configPath
        self.config = configparser.ConfigParser()
        self.TryCreateNewConfigFile()
        self.config.read(self.configPath)
              
    def TryCreateNewConfigFile(self, overwrite=False):
        if os.path.exists(self.configPath):
            if overwrite:
                self.__WriteDefaultConfig()
        else:
            self.__WriteDefaultConfig()
            
    def DeleteConfigFile(self):
        if os.path.exists(self.configPath):
            os.remove(self.configPath)
        self.config = configparser.ConfigParser()
            
    def __WriteDefaultConfig(self):
        self.DeleteConfigFile()
        cfgfile = open(self.configPath, 'w')
        self.config.add_section('InputFileFolders')
        self.config.set('InputFileFolders','WeaponsFile', r'data\weapons.csv')
        self.config.set('InputFileFolders','ArmorFile', r'data\armor.csv')
        self.config.set('InputFileFolders','LocationsFile', r'data\locations.csv')
        self.config.set('InputFileFolders','ItemsFile', r'data\items.csv')
        self.config.add_section('DbConnection')
        self.config.set('DbConnection', 'host', '')
        self.config.set('DbConnection', 'dbName', '')
        self.config.set('DbConnection', 'userName', '')
        self.config.set('DbConnection', 'password', '')
        self.config.write(cfgfile)
        cfgfile.close()
        

