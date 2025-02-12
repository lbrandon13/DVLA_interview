# shift registry into being an attribute of an registry object, and the various getting and updating functions as being methods of the registry class
# 
# initially implement a barebones registry class and then add each method, again through TDD
# 
# then deprecate each test for the old functions and then their appropriate code sections 

class Registry:

    def __init__(self):
        self.registry = {}

    def addNewRegistration(self, registrationNumber, year):

        self.registry[registrationNumber] = {"year" : year}

    def addIDToRegistration(self, registrationNumber, vehicleID):

        if registrationNumber in self.registry:
            self.registry[registrationNumber]['vehicleID'] = vehicleID
        else:
            raise Exception("Registry is missing registrationNumber " + registrationNumber)

    def getVehicleID(self, registrationNumber):

        return self.registry[registrationNumber]['vehicleID']
    
    def countRegistrations(self):

        return len(self.registry)
