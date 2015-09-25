'''
Created on 2015/09/20

@author: playerone
'''
import configparser
import os.path

class Config(object):
    
    def __init__(self, configPath):
        self.__setupWorkingDir()
        self.configPath = configPath
        self.config = configparser.ConfigParser()
        #self.TryCreateNewConfigFile()
        self.config.read(self.configPath)
        
    def __setupWorkingDir(self):
        abspath = os.path.abspath(__file__)
        dname = os.path.dirname(abspath)
        os.chdir(dname)
              
    def TryCreateNewConfigFile(self, overwrite=False):
        if os.path.exists(self.configPath):
            if overwrite:
                self.__WriteDefaultConfig()
            #else:
                #print("File already exists : " + os.getcwd() + "\\" + self.configPath)
        else:
            self.__WriteDefaultConfig()
            
    def DeleteConfigFile(self):
        if os.path.exists(self.configPath):
            os.remove(self.configPath)
        self.config = configparser.ConfigParser()
            
    def __WriteDefaultConfig(self):
        self.DeleteConfigFile()
        cfgfile = open(self.configPath, 'w')
        self.config.add_section('inputFileFolders')
        self.config.set('inputFileFolders','weaponsFile', r'data\weapons.csv')
        self.config.set('inputFileFolders','armorFile', r'data\armor.csv')
        self.config.set('inputFileFolders','locationsFile', r'data\locations.csv')
        self.config.set('inputFileFolders','itemsFile', r'data\items.csv')
        self.config.add_section('dbConnection')
        self.config.set('dbConnection', 'host', '')
        self.config.set('dbConnection', 'dbName', '')
        self.config.set('dbConnection', 'userName', '')
        self.config.set('dbConnection', 'password', '')
        self.config.write(cfgfile)
        #print("Wrote new config to " + os.getcwd() + "\\" + self.configPath)
        cfgfile.close()
        

