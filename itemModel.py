'''
Created on 2015/09/12

@author: playerone
'''

class ItemModel(object):

    def StatSum(self):
        return self.STR + self.DEX + self.INT + self.FTH

    def __init__(self, 
                 Name,
                 STR,
                 DEX,
                 INT,
                 FTH,
                 Units,
                 Phy,
                 Magic,
                 Fire,
                 Light,
                 Dark,
                 Bleed,
                 Poison,
                 S,
                 Dx,
                 I,
                 F,
                 L,
                 Dk,
                 WeaponType,
                 DamageType,
                 PoiseDamage,
                 Durability):
        self.Name = Name
        self.STR = STR
        self.DEX = DEX
        self.INT = INT
        self.FTH = FTH
        self.Units = Units
        self.Phy = Phy
        self.Magic = Magic
        self.Fire = Fire
        self.Light = Light
        self.Dark = Dark
        self.Bleed = Bleed
        self.Poison = Poison
        self.S = S
        self.Dx = Dx
        self.I = I
        self.F = F
        self.L = L
        self.Dk = Dk
        self.WeaponType = WeaponType 
        self.DamageType = DamageType
        self.PoiseDamage = PoiseDamage 
        self.Durability = Durability


        