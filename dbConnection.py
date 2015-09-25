'''
Created on 2015/09/20

@author: playerone
'''
import psycopg2
 
class DBConnection(object):

    def __init__(self, host, dbName, user, password):
        self.host = host
        self.dbName = dbName
        self.user = user
        self.password = password
        
    def Connect(self):     
        self.conn = psycopg2.connect(database='postgres', host=self.host, dbname=self.dbName, user=self.user, password=self.password)
        return self.conn.cursor()
    
    def Commit(self):
        self.conn.commit()

    def Disconnect(self):
        #self.conn.cursor.close()
        self.conn.close()
        
        #I should probably wrap the cursor in the future, so it doesn't work, or returns an error, after disconnecting.  
        #And return that on connect.