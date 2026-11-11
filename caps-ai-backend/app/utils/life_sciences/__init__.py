# Life Sciences Generator Suite
from .genetics_generator import generate as generate_genetics
from .ls11_animal_nutrition_generator import generate as generate_animal_nutrition
from .ls11_gaseous_exchange_generator import generate as generate_gaseous_exchange
from .ls11_excretion_humans_generator import generate as generate_excretion_humans
from .ls10_transport_systems_animals_generator import generate as generate_transport_systems_animals
from .ls10_plant_and_animal_cells_generator import generate as generate_plant_and_animal_cells
from .ls10_cell_division_mitosis_generator import generate as generate_cell_division_mitosis
from .ls12_meiosis_generator import generate as generate_meiosis
from .ls10_support_transport_plants_generator import generate as generate_support_transport_plants
from .ls11_photosynthesis_generator import generate as generate_photosynthesis
from .ls11_cellular_respiration_generator import generate as generate_cellular_respiration
from .ls10_biospheres_to_ecosystems_generator import generate as generate_biospheres_ecosystems
from .ls11_population_ecology_generator import generate as generate_population_ecology
from .ls12_plant_responses_environment_generator import generate as generate_plant_responses_environment
from .heart_generator import generate_heart_question

__all__ = [
    "generate_genetics",
    "generate_animal_nutrition",
    "generate_gaseous_exchange",
    "generate_excretion_humans",
    "generate_transport_systems_animals",
    "generate_plant_and_animal_cells",
    "generate_cell_division_mitosis",
    "generate_meiosis",
    "generate_support_transport_plants",
    "generate_photosynthesis",
    "generate_cellular_respiration",
    "generate_biospheres_ecosystems",
    "generate_population_ecology",
    "generate_plant_responses_environment",
    "generate_heart_question",
]
