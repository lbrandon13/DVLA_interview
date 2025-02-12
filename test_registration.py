import unittest

from registry import Registry

class TestRegistration(unittest.TestCase):

    def setUp(self):
        self.testRegistry = Registry()

    def testAddNewRegistrationWithYear(self):
        
        exampleDict = {"1234" : {"year" : "9876"}}

        self.testRegistry.addNewRegistration("1234", "9876")

        self.assertEqual(exampleDict, self.testRegistry.registry)

    def testAddIDToRegistration(self):

        exampleDict = {"1234" : {"year" : "9876", "vehicleID" : "ABCD"}}

        self.testRegistry.addNewRegistration("1234", "9876")
        self.testRegistry.addIDToRegistration("1234", "ABCD")

        self.assertEqual(exampleDict, self.testRegistry.registry)

    def testGetVehicleID(self):

        self.testRegistry.addNewRegistration("1234", "9876")
        self.testRegistry.addIDToRegistration("1234", "ABCD")

        self.assertEqual(self.testRegistry.getVehicleID("1234"), "ABCD")

    def testCountRegistrations(self):

        self.testRegistry.addNewRegistration("12", "98")
        self.testRegistry.addNewRegistration("123", "987")
        self.testRegistry.addNewRegistration("1234", "9876")

        self.assertEqual(self.testRegistry.countRegistrations(), 3)

    def testAddIDToMissingRegistration(self):

        self.assertRaises(Exception, self.testRegistry.addIDToRegistration, "1234", "ABCD")

    def testGetIDFromMissingRegistration(self):

        self.assertRaises(Exception, self.testRegistry.countRegistrations, "1234")

if __name__ == "__main__":
    unittest.main()


