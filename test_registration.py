import unittest

from main import addNewRegistration, addIDToRegistration

class TestRegistration(unittest.TestCase):

    def testAddVehicleIDToRegistration(self):

        exampleDict = {"1234" : {"vehicleID" : "9876"}}
        testDict = {"1234" : {}}

        addIDToRegistration(testDict, "1234", "9876")

        self.assertDictEqual(exampleDict, testDict)

    def testAddRegistrationWithYear(self):

        exampleDict = {"1234" : {"year" : "2021"}}
        testDict = {}

        addNewRegistration(testDict, "1234", "2021")

        self.assertDictEqual(exampleDict, testDict)

if __name__ == "__main__":
    unittest.main()


