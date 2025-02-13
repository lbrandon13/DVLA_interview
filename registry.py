# shift registry into being an attribute of an registry object, and the various getting and updating functions as being methods of the registry class
# 
# initially implement a barebones registry class and then add each method, again through TDD
# 
# then deprecate each test for the old functions and then their appropriate code sections 

# *Registry - A class to contain registrationNumbers and their associated properties
#
# * RegistrationNumber (str) - The registration number and the primary key value
# * Year (str) - The year that the registration number was first created
class Registry:

    def __init__(self):
        self.registry = {}

    def addNewRegistration(self, registrationNumber, year, cost=None):

        if cost:
            print("Adding new registration with registration number " + registrationNumber + " and year " + year + " and cost " + str(cost))
        else:
            print("Adding new registration with registration number " + registrationNumber + " and year " + year + " and no cost")
        self.registry[registrationNumber] = {"year" : year, "cost" : cost}

    def addIDToRegistration(self, registrationNumber, vehicleID):

        if registrationNumber in self.registry:
            print("Adding vehicleID " + vehicleID + " to registration number " + registrationNumber)
            self.registry[registrationNumber]['vehicleID'] = vehicleID
        else:
            raise Exception("Registry is missing registrationNumber " + registrationNumber)

    def getVehicleID(self, registrationNumber):

        try:
        # if registrationNumber in self.registry:
            print("Getting vehicleID for registration number " + registrationNumber)
            return self.registry[registrationNumber]['vehicleID']
        except Exception as e:
        # else:
            raise Exception("Registry is missing registrationNumber " + registrationNumber)
    
    def countRegistrations(self):

        print("Counting number of registrations")
        return len(self.registry)

    def countAssignedRegistrationNumbers(self):

        numberOfAssignedRegistrationNumbers = 0

        for registration in self.registry:
            if "vehicleID" in self.registry[registration]:
                numberOfAssignedRegistrationNumbers += 1

        return numberOfAssignedRegistrationNumbers
    
    def countTotalCostOfRegistrationNumbers(self):

        totalCost = 0

        for registration in self.registry:
            if self.registry[registration]['cost']:
                totalCost += self.registry[registration]['cost']

        return totalCost