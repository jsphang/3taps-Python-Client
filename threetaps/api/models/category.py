""" threetaps.api.models.category

    This Python module implements the Category model object.
"""
#############################################################################

class Category:
    """ The Category class represents a category within the 3taps client APIs.

        The following snippet illustrates part of the reference API categories
        response; the top-level Category classes (in this case, Animals) are
        represented by the 3taps Python client library as Category instances
        with Category "children" (i.e., Pets, Supplies, and Other each a child
        of the Animals Category):

            [
              {
                "categoryClassName": "Animals",
                "categoryClass": "AAAA",
                "categories":
                [
                  {
                    "category": "APET",
                    "categoryName": "Pets"
                  },
                  {
                    "category": "ASUP",
                    "categoryName": "Supplies"
                  },
                  {
                    "category": "AOTH",
                    "categoryName": "Other"
                  }
                ]
              },

        You can retrieve and change these attributes directly as required.
    """
    def __init__(self, **kwargs):
        """ Standard initializer.

            The initial attributes for the Category object can be passed as
            keyword arguments if desired.
        """
        self.code = kwargs.get("categoryClass")
        if self.code is None:
            self.isCategoryClass = False

            self.code = kwargs.get("category")
            self.name = kwargs.get("categoryName")
        else:
            ## top-level category class
            self.isCategoryClass = True
            self.children = []

            self.code = kwargs.get("categoryClass")
            self.name = kwargs.get("categoryClassName")

            children = kwargs.get("categories")
            for child in children:
                self.children.append(Category(**child))

