'''
Created on 2015/09/12

@author: playerone
'''
import unittest
import os.path
import dataLoader
import config
import dbConnection

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

class Test(unittest.TestCase):

    def setUp(self):
        self.data = dataLoader.DataLoader.LoadFromFileToList(r'E:\Program Files (x86)\Users\playerone\Desktop\weapons.csv')  #TODO: replace with config values
        
        self.sumList = list(self.data)
        self.sumList.sort(key=lambda x: x.StatSum(), reverse=False)
        
        self.strList = list(self.data)
        self.strList.sort(key=lambda x: x.STR, reverse=False)
        
        self.dexList = list(self.data)
        self.dexList.sort(key=lambda x: x.DEX, reverse=False)  
        
        self.testDir = "testData"
        self.testIniFile = self.testDir + r"\testConfig.ini"
        if not os.path.exists(self.testDir):
            os.mkdir(self.testDir)
        pass

    def tearDown(self):
        testConfig = config.Config(self.testIniFile)
        testConfig.DeleteConfigFile()
        os.rmdir(self.testDir)
        pass

    def testFirstItem(self):
        print(self.data[0])
        if self.data[0] == ['Malformed Skull', '35', '7', '', '', '12', '520', '', '', '', '', '', '', '', '', '', '', '', '', 'Greathammer', 'Strike', '60', '100', '20', 'Add bleeding effect (1.15)']:
            pass
    
    def testSumSort(self):
        last = 0    
        for item in self.sumList:
            if last > item.StatSum():
                assert False
        pass
 
    def testSTRSort(self):
        last = 0
        for item in self.sumList:
            if last > item.STR:
                assert False
        pass
    
    def testDEXSort(self):
        last = 0
        for item in self.sumList:
            if last > item.DEX:
                assert False
        pass
    
    def testWriteNewConfig(self):
        testConfig = config.Config(self.testIniFile)
        testConfig.TryCreateNewConfigFile(False)
        pass
    
    def testOverWriteNewConfig(self):
        testConfig = config.Config(self.testIniFile)
        testConfig.TryCreateNewConfigFile(True)
        #write some new data
        testConfig.TryCreateNewConfigFile(True)
        #test it was reset to default
        pass
    
    def testDonotOverWriteConfig(self):
        testConfig = config.Config(self.testIniFile)
        testConfig.TryCreateNewConfigFile(False)
        #write some data
        testConfig.TryCreateNewConfigFile(False)
        #make sure it wasn't overwritten
        pass
    
    def testReadConfig(self):
        testConfig = config.Config(self.testIniFile)
        testConfig.TryCreateNewConfigFile(True)
        #write some data
        testConfig = config.Config(self.testIniFile)
        #check data was written
        pass
        
    def testDbConnection(self):
        dbconn = dbConnection.DBConnection('192.168.1.98', 'h', 'db', 'pw')     #remove values before commit to source control
        dbconn.Connect()
        dbconn.Disconnect()
        pass
        
    def testCreateDbTables(self):
        dbconn = dbConnection.DBConnection('192.168.1.98', 'h', 'db', 'pw')     #remove values before commit to source control
        cur = dbconn.Connect()
        dbconn.Disconnect()
        pass
    
    def testDeleteDbTables(self):
        dbconn = dbConnection.DBConnection('192.168.1.98', 'h', 'db', 'pw')     #remove values before commit to source control
        cur = dbconn.Connect()
        dbconn.Disconnect()
        pass
    
    def createBuilder(self):
        pass
    
    