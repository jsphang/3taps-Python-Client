""" threetaps.api.models.posting

    This Python module implements the Posting model object.
"""
#############################################################################

class Posting:
    """ The Posting class represents a posting within the 3taps client APIs.

        A Posting object has attributes per the documentation available at:

            http://auth.3taps.com/docs

        You can retrieve and change these attributes directly as required.
    """
    def __init__(self, **kwargs):
        """ Standard initializer.

            The initial attributes for the Posting object can be passed as
            keyword arguments if desired.
        """
        self.accountId = kwargs.get("accountId")
        self.annotations = kwargs.get("annotations", {})
        self.body = kwargs.get("body")
        self.category = kwargs.get("category")
        self.categoryClass = kwargs.get("categoryClass")
        self.categoryClassName = kwargs.get("categoryClassName")
        self.categoryName = kwargs.get("categoryName")
        self.currency = kwargs.get("currency")
        self.expirationTimestamp = kwargs.get("expirationTimestamp")
        self.flags = kwargs.get("flags")
        self.hasImage = kwargs.get("hasImage", False)
        self.heading = kwargs.get("heading")
        self.html = kwargs.get("html")
        self.id = kwargs.get("id") ## 3taps' unique identifier
        self.images = kwargs.get("images", [])
        self.immortal = kwargs.get("immortal")
        self.indexed = kwargs.get("indexed")
        self.language = kwargs.get("language")
        self.location = kwargs.get("location")
        self.postingTimestamp = kwargs.get("postingTimestamp")
        self.price = kwargs.get("price")
        self.source = kwargs.get("source")
        self.sourceId = kwargs.get("source")
        self.sourceUrl = kwargs.get("sourceUrl")

