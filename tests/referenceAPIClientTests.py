""" referenceAPIClientTests.py

    This Python module defines unit tests for the ReferenceAPIClient class.
"""
from threetaps.api import clients
from threetaps.api import models

import unittest

#############################################################################

class ReferenceAPIClientTestCase(unittest.TestCase):
    """ This class implements various unit tests for the ReferenceAPIClient.
    """
    def setUp(self):
        """ Prepare to run our unit tests.
        """
        self._api = clients.ReferenceAPIClient()
        self._api.enableLogging()


    def tearDown(self):
        """ Clean up after our unit tests.
        """
        self._api.disableLogging()
        self._api = None


    def testGetCategories(self):
        """ Test the ReferenceClient.getCategories() API call
        """
        response = self._api.getCategories()
        assert response is not None
        assert len(response) > 0


#############################################################################

def suite():
    """ Create and return a test suite with all the tests we need to run.
    """
    loader = unittest.TestLoader()
    return loader.loadTestsFromTestCase(ReferenceAPIClientTestCase)

