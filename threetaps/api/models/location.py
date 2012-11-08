""" threetaps.api.models.location

    This Python module implements the Location model object.
"""
#############################################################################

class Location:
    """ The Location class represents a location within the 3taps client APIs.

        A Location object currently has attributes per the "location" object
        of the post data structure as documented at:

            http://auth.3taps.com/docs/post-data-structure

        You can retrieve and change these attributes directly as required.
    """
    def __init__(self, **kwargs):
        """ Standard initializer.

            The initial attributes for the Location object can be passed as
            keyword arguments if desired.
        """
        self.longitude = kwargs.get("longitude")
        self.latitude = kwargs.get("latitude")
        self.accuracy = kwargs.get("accuracy")
        self.countryCode = kwargs.get("countryCode")
        self.regionCode = kwargs.get("regionCode")
        self.stateCode = kwargs.get("stateCode")
        self.metroCode = kwargs.get("metroCode")
        self.countyCode = kwargs.get("countyCode")
        self.cityCode = kwargs.get("cityCode")
        self.localityCode = kwargs.get("localityCode")
        self.zipCode = kwargs.get("zipCode")

