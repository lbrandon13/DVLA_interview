import unittest

from main import addNewRegistration, addIDToRegistration

class TestRegistration(unittest.TestCase):

    def testAddNewRegistration(self):

        exampleDict = {"1234" : {}}
        testDict = {}

        addNewRegistration(testDict, "1234")

        self.assertDictEqual(exampleDict, testDict)

    def testAddVehicleIDToRegistration(self):

        exampleDict = {"1234" : {"vehicleID" : "9876"}}
        testDict = {"1234" : {}}

        addIDToRegistration(testDict, "9876")

        self.assertDictEqual(exampleDict, testDict)


if __name__ == "__main__":
    unittest.main()


