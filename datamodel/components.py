"""Helper classes describing the objects that are not a 'submittable' in the USI model"""

from typing import List


class DataFile:
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

    def __repr__(self):
        return "{self.__class__.__name__}(name={self.name}, checksum={self.checksum}, " \
               "checksum_method={self.checksum_method}, ftp_location={self.ftp_location}, " \
               "read={self.read_type})".format(self=self)


class Contact:
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

    def __repr__(self):
        return "{self.__class__.__name__}(firstName={self.firstName}, lastName={self.lastName}, email{self.email}, " \
               "affiliation={self.affiliation}, address={self.address}, phone={self.phone}, roles={self.roles}, " \
               "middleInitials={self.middleInitials}, fax={self.fax}, orcidId={self.orcidId})".format(self=self)


class Publication:
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

    def __repr__(self):
        return "{self.__class__.__name__}(articleTitle={self.articleTitle}, authors={self.authors}, " \
               "pubmedId={self.pubmedId}, doi={self.doi}, status={self.publicationStatus})".format(self=self)


class Attribute:
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

    def __repr__(self):
        return "{self.__class__.__name__}(value={self.value}, unit={self.unit}, " \
               "term_accession={self.term_accession}, term_source={self.term_source})".format(self=self)


class Unit:
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

    def __repr__(self):
        return "{self.__class__.__name__}(value={self.value}, unit_type={self.unit_type}, " \
               "term_source={self.term_source}, term_accession={self.term_accession})".format(self=self)

