""" searchAPIClientTests.py

    This Python module defines unit tests for the SearchAPIClient class.
"""
from threetaps.api import clients
from threetaps.api import models

import unittest

#############################################################################

class SearchAPIClientTestCase(unittest.TestCase):
    """ This class implements the various unit tests for the SearchAPIClient.
    """
    def setUp(self):
        """ Prepare to run our unit tests.
        """
        self._api = clients.SearchAPIClient()
        self._api.enableLogging()


    def tearDown(self):
        """ Clean up after our unit tests.
        """
        self._api.disableLogging()
        self._api = None


    def testSearch(self):
        """ Test the SearchClient.search() API call
        """
        query = clients.SearchQuery(source="CRAIG", text="bike")

        response = self._api.search(query)

        assert response is not None
        assert response['success'] == True
        assert len(response['results']) > 0
        assert len(response['results']) <= response['numResults']


    def testSummary(self):
        """ Test the SearchClient.summary() API call
        """
        query = clients.SearchQuery(source="CRAIG", text="bike")
        
        response = self._api.summary(query, "category")

        assert response is not None
        assert len(response['totals']) > 0


    def testCount(self):
        """ Test the SearchClient.count() API call
        """
        query = clients.SearchQuery(source="CRAIG", text="bike")
        
        total = self._api.count(query)

        assert total is not None
        assert total > 0


#############################################################################

def suite():
    """ Create and return a test suite with all the tests we need to run.
    """
    loader = unittest.TestLoader()
    return loader.loadTestsFromTestCase(SearchAPIClientTestCase)

