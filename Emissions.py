class Emission :
    def __init__(self, co, no2, so2):
        self.co = co
        self.no2 = no2
        self.so2 = so2

    def changingLogs(fx):
        def mfx(*args, **kwargs):
            print("Changing Values...")
            fx(*args, **kwargs)
            print("Emission Feeds Changed!")
        
        return mfx

    def getSum(self):
        return self.co+self.no2+self.so2
    
    def changeCO(self, newAmt):
        self.co = newAmt

    def changeNO2(self, newAmt):
        self.no2 = newAmt

    def changeSO2(self, newAmt):
        self.so2 = newAmt
    
    @changingLogs
    def changeAll(self, co, no2, so2):
        self.co = co
        self.no2 = no2
        self.so2 = so2
    
    def getValues(self):
        return [self.co, self.no2, self.so2]

emm = Emission(25, 35, 45)
print(emm.getValues())
emm.changeAll(5, 4, 2)
print(emm.getValues())