"""Senior Phase Natural Sciences (Grades 7–9) deterministic 6-pillar question generators."""
from __future__ import annotations

from app.utils.natural_sciences.chemical_reactions_generator import (
    generate as generate_chemical_reactions,
)
from app.utils.natural_sciences.electric_circuits_generator import (
    generate as generate_electric_circuits,
)
from app.utils.natural_sciences.senior_phase_astronomy_generator import (
    generate as generate_astronomy,
)
from app.utils.natural_sciences.term1_life_and_living_generator import (
    generate as generate_life_and_living,
)
from app.utils.natural_sciences.term2_matter_materials_generator import (
    generate as generate_matter_and_materials,
)
from app.utils.natural_sciences.term3_energy_change_forces_generator import (
    generate as generate_energy_and_forces,
)
from app.utils.natural_sciences.term4_planet_earth_beyond_generator import (
    generate as generate_planet_earth_beyond,
)

__all__ = [
    "generate_chemical_reactions",
    "generate_electric_circuits",
    "generate_astronomy",
    "generate_life_and_living",
    "generate_matter_and_materials",
    "generate_energy_and_forces",
    "generate_planet_earth_beyond",
]
