"""The classes for data objects"""

from typing import List

from datamodel.submittable import DependentSubmittable
from datamodel.components import DataFile


class DataSubmittable(DependentSubmittable):
    """The base class for all data objects
    :param files: list, DataFile class objects
    :param data_type, the type of data (raw, processed, matrix)
    """

    def __init__(self, **kwargs):
        DependentSubmittable.__init__(self, **kwargs)
        self.files: List[DataFile] = [DataFile(**d) for d in kwargs.get("files", [])]
        self.data_type: str = kwargs.get("data_type")


class AssayData(DataSubmittable):
    """
    Attributes of the assay data (raw data object)
    :param alias: string, unique name in the experiment (auto-generated from Assay Name in SDRF)
    :param files: list, DataFile class objects
    :param data_type: string, raw or raw matrix
    :param assayrefs: list, assay name/accessions
    :param protocolrefs: list, protocol name/accessions used to generate data file
    :param accession: string, (not for microarray) ENA run accession
    """

    def __init__(self, **kwargs):
        DataSubmittable.__init__(self, **kwargs)
        self.assayrefs: List[str] = kwargs.get("assayrefs", [])
        self.accession: str = kwargs.get("accession")


class Analysis(DataSubmittable):
    """
    Attributes for the analysis (processed data object)
    :param alias: string, unique name in the experiment (auto-generated from processed file name in SDRF)
    :param files: list, DataFile class objects
    :param data_type: string, processed or processed matrix
    :param protocolrefs: list, protocol name/accessions used to generate data file
    :param assaydatarefs: list, assay data name/accessions
    :param samplerefs: list, sample names (to assign files in case there is no raw/assay data)
    """

    def __init__(self, **kwargs):
        DataSubmittable.__init__(self, **kwargs)
        self.samplerefs: List[str] = kwargs.get("sampleref")
        self.assayrefs: List[str] = kwargs.get("assayrefs", [])
        self.assaydatarefs: List[str] = kwargs.get("assaydatarefs", [])
