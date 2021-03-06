"""The submission class, a container for the full set of metadata"""

from typing import List, Union

from datamodel.project import Project
from datamodel.study import Study
from datamodel.protocol import Protocol
from datamodel.sample import Sample
from datamodel.assay import SeqAssay, SingleCellAssay, MicroarrayAssay
from datamodel.data import AssayData, Analysis


class Submission:
    """
    The submission class holds all objects that make up an ArrayExpress experiment.

    :param info: dictionary, information about the submission (file names, submitter details, etc.)
    :param project: object, Project class object
    :param study: object, Study class object
    :param protocol: list, Protocol class objects
    :param sample: list, Sample class objects
    :param assay: list, SeqAssay or MicroarrayAssay class objects
    :param assay_data: list, AssayData class objects
    :param analysis: list, Analysis class objects
    """

    def __init__(self, info, project, study, protocol, sample, assay, assay_data, analysis):
        self.info: dict = info
        self.project: Project = project
        self.study: Study = study
        self.protocol: List[Protocol] = protocol
        self.sample: List[Sample] = sample
        self.assay: List[Union[SeqAssay, SingleCellAssay, MicroarrayAssay]] = assay
        self.assay_data: List[AssayData] = assay_data
        self.analysis: List[Analysis] = analysis

        # Create indexes so we can return given objects based on alias
        self.sample_lookup = {s.alias: s for s in self.sample}
        self.assay_lookup = {a.alias: a for a in self.assay}
        self.protocol_lookup = {p.alias: p for p in self.protocol}
        self.data_lookup = {ad.alias: ad for ad in self.assay_data}

    def get_sample(self, sample_alias):
        """Return the sample object for a given sample alias."""
        return self.sample_lookup.get(sample_alias)

    def get_assay(self, assay_alias):
        """Return the assay object for a given assay alias."""
        return self.assay_lookup.get(assay_alias)

    def get_protocol(self, protocol_alias):
        """Return the protocol object for a given protocol alias."""
        return self.protocol_lookup.get(protocol_alias)

    def get_assay_data(self, ad_alias):
        """Return the assay data object for a given assay data alias."""
        return self.data_lookup.get(ad_alias)
