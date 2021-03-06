"""The sample class"""

from datamodel.submittable import AccessionedSubmittable


class Sample(AccessionedSubmittable):
    """
       :param alias: string, unique sample name in the experiment
       :param accession: string, BioSamples accession
       :param taxon: string, latin species name
       :param taxonId: str, NCBI taxonomy identifier for the species
       :param attributes: dictionary of attribute categories as keys and Attribute class object as value
       :param material_type: string, (optional) one of: whole organism, organism part, cell, RNA, DNA
       :param description: string, (optional) free-text description of sample
       """
    def __init__(self, **kwargs):
        AccessionedSubmittable.__init__(self, **kwargs)
        self.taxon: str = kwargs.get("taxon")
        self.taxonId: str = kwargs.get("taxonId")
        self.material_type: str = kwargs.get("material_type")
        self.attributes: dict = kwargs.get("attributes", {})

        # Remove material type from attributes if already defined in main attribute
        if self.material_type and "material_type" in self.attributes:
            del self.attributes["material_type"]
