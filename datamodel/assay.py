"""The classes for the different assay types"""

from typing import List

from datamodel.submittable import DependentSubmittable


class Assay(DependentSubmittable):
    """
    Attributes common to all assay types
    :param alias: string, unique name of the assay
    :param technology_type: string, one of: array assay, sequencing assay
    :param protocolrefs: list, protocol accessions/name used to generate assay data
    :param sampleref: string, sample accession/name
    """

    def __init__(self, **kwargs):
        DependentSubmittable.__init__(self, **kwargs)
        self.technology_type: str = kwargs.get("technology_type")
        self.sampleref: List[str] = kwargs.get("sampleref")

    def __repr__(self):
        return "{self.__class__.__name__}(alias={self.alias}, technology_type={self.technology_type}, " \
               "protocolrefs={self.protocolrefs}, sampleref={self.sampleref})".format(self=self)

    def get_assay_attributes(self):
        """A list of all attributes that are specific to the assay object (not in the general assay class)"""
        exclude = ('id', 'alias', 'accession', 'protocolrefs', 'technology_type', 'sampleref')
        return [at for at in self.get_all_attributes() if at not in exclude]

    def get_attributes_with_values(self):
        """A list of all assay attributes that have values"""
        exclude = ('id', 'alias', 'accession', 'protocolrefs', 'sampleref')
        return [at for at in self.get_all_attributes() if getattr(self, at) and at not in exclude]


class MicroarrayAssay(Assay):
    """
    Assay attributes specific to microarray assays
    :param label: string, the label type
    :param array_design: string, ArrayExpress array design format accession
    """

    def __init__(self, **kwargs):
        Assay.__init__(self, **kwargs)
        self.label: str = kwargs.get("label")
        self.array_design: str = kwargs.get("array_design")

    def __repr__(self):
        return "{self.__class__.__name__}(alias={self.alias}, technology_type={self.technology_type}, " \
               "protocolrefs={self.protocolrefs}, sampleref={self.sampleref}, " \
               "label={self.label}, array_design={self.array_design})".format(self=self)


class SeqAssay(Assay):
    """
    Assay attributes specific to sequencing assays
    :param accession: string, (not for microarray) ENA experiment accession
    :param lib_attribs: dictionary of sequencing specific attributes that are required for ENA brokering
                        keys: library attribute
                        values: values from SRA's controlled vocabulary
    """
    def __init__(self, **kwargs):
        Assay.__init__(self, **kwargs)
        self.accession: str = kwargs.get("accession")
        self.library_layout: str = kwargs.get("library_layout")
        self.library_selection: str = kwargs.get("library_selection")
        self.library_strategy: str = kwargs.get("library_strategy")
        self.library_strand: str = kwargs.get("library_strand")
        self.library_source: str = kwargs.get("library_source")
        self.orientation: str = kwargs.get("orientation")
        self.nominal_length: str = kwargs.get("nominal_length")
        self.nominal_sdev: str = kwargs.get("nominal_sdev")
        self.platform_type: str = kwargs.get("platform_type")
        self.instrument_model: str = kwargs.get("instrument_model")

    def __repr__(self):
        return "{self.__class__.__name__}(alias={self.alias}, technology_type={self.technology_type}, " \
               "protocolrefs={self.protocolrefs}, sampleref={self.sampleref} " \
               "accession={self.accession}, library_layout={self.library_layout}, " \
               "library_selection={self.library_selection}, library_strategy={self.library_strategy}, " \
               "library_strand={self.library_strand}, library_source={self.library_source}," \
               "orientation={self.orientation}, nominal_length={self.nominal_length}, " \
               "nominal_sdev={self.nominal_sdev}, platform_type={self.platform_type}, " \
               "instrument_model={self.instrument_model})".format(self=self)


class SingleCellAssay(SeqAssay):
    """Assay attributes specific to single-cell sequencing assays"""

    def __init__(self, **kwargs):
        SeqAssay.__init__(self, **kwargs)
        self.single_cell_isolation: str = kwargs.get("single_cell_isolation")
        self.library_construction: str = kwargs.get("library_construction")
        self.input_molecule: str = kwargs.get("input_molecule")
        self.end_bias: str = kwargs.get("end_bias")
        self.primer: str = kwargs.get("primer")
        self.spike_in: str = kwargs.get("spike_in")
        self.spike_in_dilution: str = kwargs.get("spike_in_dilution")
        self.umi_barcode_read: str = kwargs.get("umi_barcode_read")
        self.umi_barcode_size: str = kwargs.get("umi_barcode_size")
        self.umi_barcode_offset: str = kwargs.get("umi_barcode_offset")
        self.cell_barcode_read: str = kwargs.get("cell_barcode_read")
        self.cell_barcode_size: str = kwargs.get("cell_barcode_size")
        self.cell_barcode_offset: str = kwargs.get("cell_barcode_offset")
        self.cDNA_read: str = kwargs.get("cDNA_read")
        self.cDNA_read_size: str = kwargs.get("cDNA_read_size")
        self.cDNA_read_offset: str = kwargs.get("cDNA_read_offset")
        self.sample_barcode_read: str = kwargs.get("sample_barcode_read")
        self.sample_barcode_size: str = kwargs.get("sample_barcode_size")
        self.sample_barcode_offset: str = kwargs.get("sample_barcode_offset")
        self.hca_bundle_uuid: str = kwargs.get("hca_bundle_uuid")
        self.hca_bundle_version: str = kwargs.get("hca_bundle_version")

    def get_singlecell_attributes(self, invert=False):
        """A list of single-cell specific attributes that are not in the parent sequencing assay class,
        with invert=True returns the sequencing assay attributes."""
        dummy_assay = SeqAssay()
        exclude = dummy_assay.get_all_attributes()
        if invert:
            return dummy_assay.get_assay_attributes()
        return [at for at in self.get_all_attributes() if at not in exclude]
