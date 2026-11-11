"""Grade 9 Natural Sciences Dedicated Topic Generators (Terms 1 to 4).

All 24 curriculum topics are implemented as discrete, unbundled generators
complying with the 6-pillar contract and the dual-surface visual mould.
"""

# Term 1 Generators (Life & Living)
from app.utils.natural_sciences.grade9 import cells_generator
from app.utils.natural_sciences.grade9 import human_systems_generator
from app.utils.natural_sciences.grade9 import human_reproduction_gen
from app.utils.natural_sciences.grade9 import circulatory_respiratory
from app.utils.natural_sciences.grade9 import digestive_system_gen

# Term 2 Generators (Matter & Materials)
from app.utils.natural_sciences.grade9 import compounds_generator
from app.utils.natural_sciences.grade9 import chemical_reactions_gen
from app.utils.natural_sciences.grade9 import reactions_metals_oxygen
from app.utils.natural_sciences.grade9 import reactions_nonmetals_ox
from app.utils.natural_sciences.grade9 import acids_bases_ph_gen
from app.utils.natural_sciences.grade9 import reactions_acids_bases
from app.utils.natural_sciences.grade9 import reactions_acids_metals

# Term 3 Generators (Energy & Change)
from app.utils.natural_sciences.grade9 import forces_generator
from app.utils.natural_sciences.grade9 import electric_cells_gen
from app.utils.natural_sciences.grade9 import resistance_generator
from app.utils.natural_sciences.grade9 import series_parallel_circuits
from app.utils.natural_sciences.grade9 import safety_electricity_gen
from app.utils.natural_sciences.grade9 import national_grid_generator
from app.utils.natural_sciences.grade9 import cost_electrical_energy

# Term 4 Generators (Planet Earth & Beyond)
from app.utils.natural_sciences.grade9 import earth_system_generator
from app.utils.natural_sciences.grade9 import lithosphere_generator
from app.utils.natural_sciences.grade9 import mining_resources_gen
from app.utils.natural_sciences.grade9 import atmosphere_generator
from app.utils.natural_sciences.grade9 import stellar_evolution_gen

__all__ = [
    # Term 1 (5 topics)
    "cells_generator",
    "human_systems_generator",
    "human_reproduction_gen",
    "circulatory_respiratory",
    "digestive_system_gen",
    # Term 2 (7 topics)
    "compounds_generator",
    "chemical_reactions_gen",
    "reactions_metals_oxygen",
    "reactions_nonmetals_ox",
    "acids_bases_ph_gen",
    "reactions_acids_bases",
    "reactions_acids_metals",
    # Term 3 (7 topics)
    "forces_generator",
    "electric_cells_gen",
    "resistance_generator",
    "series_parallel_circuits",
    "safety_electricity_gen",
    "national_grid_generator",
    "cost_electrical_energy",
    # Term 4 (5 topics)
    "earth_system_generator",
    "lithosphere_generator",
    "mining_resources_gen",
    "atmosphere_generator",
    "stellar_evolution_gen",
]
