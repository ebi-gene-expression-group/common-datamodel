"""Definitions of the base classes"""


class Submittable:
    """Base class for all main object types"""
    def __init__(self, **kwargs):
        self.alias = kwargs.get("alias")
        self.id = kwargs.get("id")

    def get_all_attributes(self):
        """Return a list of all attributes"""
        return [k for k, v in self.__dict__.items() if not callable(v)]

    def __repr__(self):
        """Generate a printable string with class name and attributes"""
        return "{}({})".format(self.__class__.__name__,
                               ", ".join(["{}={!r}".format(k, getattr(self, k)) for k in self.get_all_attributes()]))


class AccessionedSubmittable(Submittable):
    """An accessioned submittable contains an accession and description attribute."""
    def __init__(self, **kwargs):
        Submittable.__init__(self, **kwargs)
        self.accession = kwargs.get("accession")
        self.description = kwargs.get("description")


class DependentSubmittable(Submittable):
    """Any submittable that is linked to another submittable and is therefore expected to be using
    protocolrefs to describe the process of derivation."""
    def __init__(self, **kwargs):
        Submittable.__init__(self, **kwargs)
        self.protocolrefs = kwargs.get("protocolrefs", [])
