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
    :param ea_curator: list, name of Expression Atlas curator
    :param ea_experiment_type: list, Single Cell Expression Atlas analysis type
    :param ea_additional_attributes: list, attribute names to be visualised in single cell plot
    :param ea_expected_clusters: list, number of cell clusters expected in a single cell experiment
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
        self.ea_curator: List[str] = kwargs.get("ea_curator", [])
        self.ea_experiment_type: List[str] = kwargs.get("ea_experiment_type", [])
        self.ea_additional_attributes: List[str] = kwargs.get("ea_additional_attributes", [])
        self.ea_expected_clusters: List[str] = kwargs.get("ea_expected_clusters", [])
        self.comments: dict = kwargs.get("comments", {})

