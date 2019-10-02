"""Helper classes describing the objects that are not a 'submittable' in the USI model"""

from typing import List


class Component:
    """The base component class, with the main purpose of adding a __repr__ function to all components"""

    def __repr__(self):
        """Generate a printable string with class name and attributes"""
        return "{}({})".format(self.__class__.__name__,
                               ", ".join(["{}={!r}".format(k, getattr(self, k)) for k in self.__dict__]))


class DataFile(Component):
    """Attributes of a DataFile object
    :param name, string, file name
    :param checksum, string, checksum hash of the file
    :param checksum_method, string, the method used to calculate the checksum
    :param ftp_location, string, the FTP path to download the file
    :param read_type, string, the type of sequencing read, e.g. read1/read2/index1
    """
    def __init__(self, **kwargs):
        self.name: str = kwargs.get("name")
        self.checksum: str = kwargs.get("checksum")
        self.checksum_method: str = kwargs.get("checksum_method")
        self.ftp_location: str = kwargs.get("ftp_location")
        self.read_type: str = kwargs.get("read_type")


class Contact(Component):
    """Attributes of a contact
    :param firstName, string, person first name
    :param lastName, string, person last name
    :param middleInitials, string, person middle initials
    :param email, string, email address
    :param affiliation, string, affiliated institute
    :param address, string, address of the institute
    :param phone, string, phone number
    :param roles, list of role terms
    :param fax, string, fax number
    :param orcidId, string, ORCID number
    """
    def __init__(self, **kwargs):
        self.firstName: str = kwargs.get("firstName")
        self.lastName: str = kwargs.get("lastName")
        self.email: str = kwargs.get("email")
        self.affiliation: str = kwargs.get("affiliation")
        self.address: str = kwargs.get("address")
        self.phone: str = kwargs.get("phone")
        self.roles: List[str] = kwargs.get("roles", [])
        self.middleInitials: str = kwargs.get("middleInitials")
        self.fax: str = kwargs.get("fax")
        self.orcidId: str = kwargs.get("orcidId")


class Publication(Component):
    """Attributes of a publication
    :param articleTitle, string, title of the publication
    :param authors, string, list of the author names
    :param pubmedId, string, PubMed ID of the publication
    :param doi, string, DOI of the publication
    :param publicationStatus, string, status term of the publication
    """
    def __init__(self, **kwargs):
        self.articleTitle: str = kwargs.get("articleTitle")
        self.authors: str = kwargs.get("authors")
        self.pubmedId: str = kwargs.get("pubmedId")
        self.doi: str = kwargs.get("doi")
        self.publicationStatus: str = kwargs.get("publicationStatus")


class Attribute(Component):
    """Attributes of an attribute
    :param value, string, the attribute value, e.g. ontology label
    :param unit, Unit class object describing the unit of the value
    :param term_source, string, the source ontology of the term
    :param term_accession, string, the ontology ID of the term
    """
    def __init__(self, **kwargs):
        self.value: str = kwargs.get("value")
        self.unit: Unit = kwargs.get("unit")
        self.term_source: str = kwargs.get("term_source")
        self.term_accession: str = kwargs.get("term_accession")


class Unit(Component):
    """Attributes of a unit
    :param value, string, the unit term, e.g. hour
    :param unit_type, string, the type of unit, e.g. time unit
    :param term_source, string, the source ontology of the unit term
    :param term_accession, string, the ontology ID of the unit term
    """
    def __init__(self, **kwargs):
        self.value: str = kwargs.get("value")
        self.unit_type: str = kwargs.get("unit_type")
        self.term_source: str = kwargs.get("term_source")
        self.term_accession: str = kwargs.get("term_accession")
