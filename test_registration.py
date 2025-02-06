import unittest

from main import addNewRegistration

class TestRegistration(unittest.TestCase):

    def testAddNewRegistration(self):

        exampleDict = {"1234" : {}}
        testDict = {}

        addNewRegistration(testDict, "1234")

        self.assertDictEqual(exampleDict, testDict)


if __name__ == "__main__":
    unittest.main()


