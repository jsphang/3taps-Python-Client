""" threetaps.api.clients.referenceAPIClient

    This Python module implements the 3taps Reference API client object.
"""
from threetaps.api.base   import APIClient
from threetaps.api.models import Category
from threetaps.api.models import Location

import simplejson as json

#############################################################################

class ReferenceAPIClient(APIClient):
    """ A client for the 3taps Reference API.
    """
    def getCategories(self):
        """ Return the master list of all known 3taps categories.

            We download and return a list of Category objects corresponding to
            the master list of all known 3taps categories.  If
            'includeAnnotations' is True (the default), the annotation details
            will also be downloaded.

            If the list of categories cannot be downloaded for some reason, we
            return None.
        """
        request = "reference/categories"

        response = self.sendRequest(request)

        if (response is None) or (response['status'] != 200):
            return None # An error occurred.

        results = json.loads(response['contents'])

        categories = []
        for cat in results:
            category = self._parseCategory(cat)
            categories.append(category)

        return categories


    # =====================
    # == PRIVATE METHODS ==
    # =====================

    def _parseCategory(self, data):
        """ Convert the JSON-format category data into a Category object.

            'data' should be a dictionary with one or more of the following
            entries:

                "group"
                "category"
                "code"
                "annotations"

            If it exists, the "annotations" entry should be a list of
            annotations for this category, where each list item is itself a
            dictionary with one or more of the following entries:

                "name"
                "type"
                "options"

            'options' should be a list of annotation options, where each item
            in this list is a dictionary with one or more of the following
            entries:

                "value"
                "subannotation"

            Note that 'data' will be in the format received from the 3taps
            server after decoding the JSON-format data.

            We convert 'data' into a Category object, which we then return to
            the caller.
        """
        category = Category(**data)
        return category


    def _parseLocation(self, data):
        """ Convert the JSON-format location data into a Location object.

            'data' should be a dictionary with one or more of the following
            entries:

                "latitude"
                "longitude"
                "accuracy"
                "countryCode"
                "regionCode"
                "stateCode"
                "metroCode"
                "countyCode"
                "cityCode"
                "localityCode"
                "zipCode"

            Note that this is the format received from the 3taps server after
            decoding the JSON-format data.

            We convert 'data' into a Location object, which we then return to
            the caller.
        """
        location = Location()
        if "latitude"     in data: location.latitude     = data['latitude']
        if "longitude"    in data: location.longitude    = data['longitude']
        if "accuracy"     in data: location.accuracy     = data['accuracy']
        if "countryCode"  in data: location.countryCode  = data['countryCode']
        if "regionCode"   in data: location.regionCode   = data['regionCode']
        if "stateCode"    in data: location.stateCode    = data['stateCode']
        if "metroCode"    in data: location.stateCode    = data['metroCode']
        if "countyCode"   in data: location.stateCode    = data['countyCode']
        if "cityCode"     in data: location.stateCode    = data['cityCode']
        if "localityCode" in data: location.localityCode = data['localityCode']
        if "zipCode"      in data: location.zipCode      = data['zipCode']
        return location
