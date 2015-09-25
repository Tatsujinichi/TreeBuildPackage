'''
Created on 2015/09/20

@author: playerone
'''
import config
import dataLoader

class DBBuilder(object):

    def __init__(self, DBConnection):
        self.conneciton = DBConnection
        self.cfg = config.Config('config.ini')
        
    def CreateTables(self):
        cursor = self.conneciton.Connect()
        cursor.execute('''\
                        CREATE TABLE weapons (
                        name        varchar(32) PRIMARY KEY,
                        str            smallint NOT NULL,
                        dex            smallint NOT NULL,
                        int            smallint NOT NULL,
                        fth            smallint NOT NULL,
                        units        float NOT NULL,
                        phy            smallint NOT NULL,
                        magic        smallint NOT NULL,
                        fire        smallint NOT NULL,
                        light        smallint NOT NULL,
                        dark        smallint NOT NULL,
                        bleed        smallint NOT NULL,
                        poison        smallint NOT NULL,
                        s            varchar(32) NOT NULL,
                        dx            varchar(32) NOT NULL,
                        i            varchar(32) NOT NULL,
                        f            varchar(32) NOT NULL,
                        l            varchar(32) NOT NULL,
                        dk            varchar(32) NOT NULL,
                        weapontype    varchar(32) NOT NULL,
                        damagetype    varchar(32) NOT NULL,
                        poisedamage    smallint NOT NULL,
                        durability    smallint NOT NULL,
                        location    varchar(32)
                        );'''
                        )
        
               
        #TODO
        self.conneciton.Commit()
        self.conneciton.Disconnect()
        
    def DeleteTables(self):
        self.conneciton.Connect()
        cursor = self.conneciton.Connect()
        cursor.execute('''\
                        DROP TABLE WEAPONS
                        ;'''
                        ) 
        self.conneciton.Commit()
        self.conneciton.Disconnect()
        
    def FillTables(self):
        self.conneciton.Connect()
        weaponsFile = self.cfg.config['inputFileFolders']['weaponsFile']
        weaponObjectList = dataLoader.DataLoader.LoadFromFileToList(weaponsFile)
        #TODO
        self.conneciton.Disconnect()

