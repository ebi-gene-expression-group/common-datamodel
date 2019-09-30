"""The protocol class"""

from datamodel.submittable import AccessionedSubmittable
from datamodel.components import Attribute


class Protocol(AccessionedSubmittable):
    """
    Attributes of a protocol
    :param alias: string, protocol accession or unique name in experiment
    :param accession: string, ArrayExpress protocol accession
    :param description: string, free-text description of protocol
    :param protocol_type: object, Attribute class object, experiment type ontology term
    :param hardware: string, free-text hardware description, sequencer model for sequencing experiments
    :param software: string, free-text software description
    :param performer: string, protocol performer
    """
    def __init__(self, **kwargs):
        AccessionedSubmittable.__init__(self, **kwargs)
        self.name: str = kwargs.get("name")
        self.protocol_type: Attribute = kwargs.get("protocol_type")
        self.hardware: str = kwargs.get("hardware")
        self.software: str = kwargs.get("software")
        self.performer: str = kwargs.get("performer")

    def __repr__(self):
        return "{self.__class__.__name__}(alias={self.alias}, accession={self.accession}, " \
               "description={self.description}, protocol_type={self.protocol_type}, " \
               "hardware={self.hardware}, software={self.software}, performer={self.performer})".format(self=self)

    def get_ae_attributes(self):
        """Return a list of all AE attributes that have values."""
        all_attributes = self.__dict__.keys()
        all_values = self.__dict__
        ae_attributes = ("protocol_type", "hardware", "software")
        found_attributes = list()
        for a in all_attributes:
            if a in ae_attributes and all_values[a]:
                found_attributes.append(a)
        return found_attributes
