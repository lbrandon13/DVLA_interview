import unittest

from main import addNewRegistration, addIDToRegistration, countNumberOfRegistrations, getVehicleID
from registry import Registry

class TestRegistration(unittest.TestCase):

    # def testAddVehicleIDToRegistration(self):

    #     exampleDict = {"1234" : {"vehicleID" : "9876"}}
    #     testDict = {"1234" : {}}

    #     addIDToRegistration(testDict, "1234", "9876")

    #     self.assertDictEqual(exampleDict, testDict)

    # def testAddRegistrationWithYear(self):

    #     exampleDict = {"1234" : {"year" : "2021"}}
    #     testDict = {}

    #     addNewRegistration(testDict, "1234", "2021")

    #     self.assertDictEqual(exampleDict, testDict)

    # def testCountRegistrations(self):

    #     exampleDict = {'AB01 CDE': {'year': '2001', 'vehicleID': '12345'}, 'FG02 HJK': {'year': '2002', 'vehicleID': '67890'}, 'L33T H4X0R': {'year': '2022'}}

    #     self.assertEqual(3, countNumberOfRegistrations(exampleDict))

    # def testGetVehicleID(self):
        
    #     exampleDict = {"1234" : {'year': "2021", "vehicleID": "9876"}}

    #     self.assertEqual("9876", getVehicleID(exampleDict, "1234"))

    # def testAddToMissingRegistration(self):

    #     exampleDict = {}

    #     self.assertRaises(Exception, addIDToRegistration, exampleDict, "1234", "9876")

    # def testGetMissingRegistration(self):

    #     exampleDict = {}

    #     self.assertRaises(Exception, getVehicleID, exampleDict, "1234")

    def testCreateRegistryObject(self):

        exampleRegistry = Registry()

    def testAddNewRegistrationWithYear(self):
        
        exampleDict = {"1234" : {"year" : "9876"}}

        testRegistry = Registry()
        testRegistry.addNewRegistration("1234", "9876")

        self.assertEqual(exampleDict, testRegistry.registry)

    def testAddIDToRegistration(self):

        exampleDict = {"1234" : {"year" : "9876", "vehicleID" : "ABCD"}}

        testRegistry = Registry()
        testRegistry.addNewRegistration("1234", "9876")
        testRegistry.addIDToRegistration("1234", "ABCD")

        self.assertEqual(exampleDict, testRegistry.registry)

    def testGetVehicleID(self):

        testRegistry = Registry()
        testRegistry.addNewRegistration("1234", "9876")
        testRegistry.addIDToRegistration("1234", "ABCD")

        self.assertEqual(testRegistry.getVehicleID("1234"), "ABCD")

    def testCountRegistrations(self):

        testRegistry = Registry()
        testRegistry.addNewRegistration("12", "98")
        testRegistry.addNewRegistration("123", "987")
        testRegistry.addNewRegistration("1234", "9876")

        self.assertEqual(testRegistry.countRegistrations(), 3)


if __name__ == "__main__":
    unittest.main()


