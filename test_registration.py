import unittest

from registry import Registry

class TestRegistration(unittest.TestCase):

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

    def testAddIDToMissingRegistration(self):

        testRegistry = Registry()
        
        self.assertRaises(Exception, testRegistry.addIDToRegistration, "1234", "ABCD")

    def testGetIDFromMissingRegistration(self):

        testRegistry = Registry()

        self.assertRaises(Exception, testRegistry.countRegistrations, "1234")

if __name__ == "__main__":
    unittest.main()


