import unittest

from main import addNewRegistration, addIDToRegistration, countNumberOfRegistrations, getVehicleID

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

    def testCountRegistrations(self):

        exampleDict = {'AB01 CDE': {'year': '2001', 'vehicleID': '12345'}, 'FG02 HJK': {'year': '2002', 'vehicleID': '67890'}, 'L33T H4X0R': {'year': '2022'}}

        self.assertEqual(3, countNumberOfRegistrations(exampleDict))

    def testGetVehicleID(self):
        
        exampleDict = {"1234" : {'year': "2021", "vehicleID": "9876"}}

        self.assertEqual("9876", getVehicleID(exampleDict, "1234"))

    def testAddToMissingRegistration(self):

        exampleDict = {}

        self.assertRaises(Exception, addIDToRegistration, exampleDict, "1234", "9876")

if __name__ == "__main__":
    unittest.main()


