'''
Created on 2015/09/12

@author: playerone
'''
import csv
import itemModel

def mk_int(s):
    s = s.strip()
    return int(s) if s else 0

def mk_float(s):
    s = s.strip()
    return float(s) if s else 0.0

class DataLoader(object):

    @staticmethod
    def LoadFromFileToList(CSVFile):
        #read file
        allItems = []
        with open(CSVFile, mode='r', buffering=1, encoding=None, errors=None, newline=None, closefd=True, opener=None) as file:
            reader = csv.reader(file)  
            content = list(reader)
        for item in content:
            newModel = itemModel.ItemModel(item[0],              #name
                                mk_int(item[1]),       #str
                                mk_int(item[2]),       #dex
                                mk_int(item[3]),       #int
                                mk_int(item[4]),       #fth
                                mk_float(item[5]),     #units
                                mk_int(item[6]),       #phy
                                mk_int(item[7]),       #magic
                                mk_int(item[8]),       #fire
                                mk_int(item[9]),       #light
                                mk_int(item[10]),      #dark
                                mk_int(item[11]),      #bleed
                                mk_int(item[12]),      #poison
                                item[13],              #s
                                item[14],              #dx
                                item[15],              #i
                                item[16],              #f
                                item[17],              #l
                                item[18],              #dk
                                item[19],              #weapontype
                                item[20],              #damagetype
                                mk_int(item[21]),      #poisedamage
                                mk_int(item[22]))      #durability
            allItems.append(newModel)
        
        return allItems
