"""The study class"""

from typing import List

from datamodel.submittable import AccessionedSubmittable
from datamodel.components import Attribute


class Study(AccessionedSubmittable):
    """
    Attributes of the study
    :param alias: string, unique study name (auto-generated from MAGE-TAB file name)
    :param accession: string, ArrayExpress experiment accession
    :param title: string, (optional)
    :param description: string, free-text description of study background and aim
    :param protocolrefs: list,  protocol accessions/name used in the study
    :param projectref: string, project alias or accession
    :param experimental_factor: list, Attribute class objects
    :param experimental_design: list, Attribute class objects
    :param experiment_type: list, experiment type ontology terms
    :param date_of_experiment: string, (optional) date of experiment
    :param submission_type: string, submission type (microarray, sequencing, singlecell)
    :param secondary_accession: list, accession of the same study in another archive (e.g. ENA)
    :param related_experiment: list, accession of experiments related to this study
    :param comments: dictionary, (optional) known IDF comments
                    keys: string, comment category
                    values: list, comment values
    """
    def __init__(self, **kwargs):
        AccessionedSubmittable.__init__(self, **kwargs)
        self.title: str = kwargs.get("title")
        self.protocolrefs: List[str] = kwargs.get("protocolrefs", [])
        self.projectref: str = kwargs.get("projectref")
        self.experimental_factor: List[Attribute] = kwargs.get("experimental_factor", [])
        self.experimental_design: List[Attribute] = kwargs.get("experimental_design", [])
        self.experiment_type: List[str] = kwargs.get("experiment_type", [])
        self.date_of_experiment: str = kwargs.get("date_of_experiment")
        self.submission_type: str = kwargs.get("submission_type")
        self.secondary_accession: List[str] = kwargs.get("secondary_accession", [])
        self.related_experiment: List[str] = kwargs.get("related_experiment", [])
        self.comments: dict = kwargs.get("comments", {})

    def __repr__(self):
        return "{self.__class__.__name__}(alias={self.alias}, accession={self.accession}, title={self.title}, " \
               "description={self.description}, protocolrefs={self.protocolrefs}, projectref={self.projectref}, " \
               "experimental_factor={self.experimental_factor}, experimental_design={self.experimental_design}, " \
               "experiment_type={self.experiment_type}, date_of_experiment={self.date_of_experiment}, " \
               "submission_type={self.submission_type}, secondary_accession={self.secondary_accession}, " \
               "related_experiment={self.related_experiment}, comments={self.comments})".format(self=self)
