"""
File that defines the main RNA sequence data
"""

from attrs import define, field
from typing import List
from collections import namedtuple
from serena.utilities.ensemble_structures import Sara2SecondaryStructure, Sara2StructureList



@define
class Energy():
    kcal: float = 0

@define
class PrimaryStructure():
    strand: str = ''

@define
class SecondaryStructure():
    dot_parens: str
    free_energy: Energy = Energy()
    stack_energy: Energy = Energy()

@define
class EnergyGroup():
    min_energy:Energy = Energy()
    max_energy:Energy = Energy()
    structure_list: List[SecondaryStructure] = []
    mfe_structure:SecondaryStructure = SecondaryStructure()
    mea_structure:SecondaryStructure = SecondaryStructure()

class EnsembleGroup(namedtuple):
    start_energy: float
    group:EnergyGroup

@define
class Ensemble():
    min_energy:Energy = Energy()
    max_energy:Energy = Energy()
    energy_groups:List[EnsembleGroup] = []
    mfe_structure:SecondaryStructure = SecondaryStructure()
    mea_structure:SecondaryStructure = SecondaryStructure()
    
    def add_structure(self ):
        """
        Add a structure to the ensemble 
        """
        self.energy_groups
        

@define
class RNAStrand():
    primary_structure: PrimaryStructure
    ensemble: Ensemble = Ensemble()
