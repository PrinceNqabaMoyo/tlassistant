"""
Comprehensive Metric System Integration
Implements South African metric system with proper conversions and contexts
"""

from typing import Dict, List, Tuple, Any
from enum import Enum
import random


class MetricUnit(Enum):
    """Metric units used in South African education"""
    # Length units
    MILLIMETER = "mm"
    CENTIMETER = "cm"
    METER = "m"
    KILOMETER = "km"
    
    # Area units
    SQUARE_MILLIMETER = "mm²"
    SQUARE_CENTIMETER = "cm²"
    SQUARE_METER = "m²"
    SQUARE_KILOMETER = "km²"
    HECTARE = "ha"
    
    # Volume units
    CUBIC_CENTIMETER = "cm³"
    CUBIC_METER = "m³"
    LITER = "L"
    MILLILITER = "mL"
    
    # Weight units
    GRAM = "g"
    KILOGRAM = "kg"
    TON = "t"


class ConversionType(Enum):
    """Types of metric conversions"""
    LENGTH_MM_CM = "mm_cm"
    LENGTH_CM_MM = "cm_mm"
    LENGTH_CM_M = "cm_m"
    LENGTH_M_CM = "m_cm"
    LENGTH_M_KM = "m_km"
    LENGTH_KM_M = "km_m"
    
    AREA_MM2_CM2 = "mm²_cm²"
    AREA_CM2_MM2 = "cm²_mm²"
    AREA_CM2_M2 = "cm²_m²"
    AREA_M2_CM2 = "m²_cm²"
    AREA_M2_HA = "m²_ha"
    AREA_HA_M2 = "ha_m²"
    
    VOLUME_ML_L = "mL_L"
    VOLUME_L_ML = "L_mL"
    VOLUME_CM3_ML = "cm³_mL"
    VOLUME_ML_CM3 = "mL_cm³"
    
    WEIGHT_G_KG = "g_kg"
    WEIGHT_KG_G = "kg_g"
    WEIGHT_KG_T = "kg_t"
    WEIGHT_T_KG = "t_kg"


class SouthAfricanContext(Enum):
    """South African real-world contexts for geometry problems"""
    # Educational contexts
    SCHOOL_CLASSROOM = "school_classroom"
    SCHOOL_PLAYGROUND = "school_playground"
    SCHOOL_LIBRARY = "school_library"
    SCHOOL_HALL = "school_hall"
    
    # Home contexts
    HOME_GARDEN = "home_garden"
    HOME_ROOM = "home_room"
    HOME_PATIO = "home_patio"
    HOME_KITCHEN = "home_kitchen"
    
    # Community contexts
    COMMUNITY_PARK = "community_park"
    COMMUNITY_SPORTS_FIELD = "community_sports_field"
    COMMUNITY_MARKET = "community_market"
    COMMUNITY_CHURCH = "community_church"
    
    # Construction contexts
    CONSTRUCTION_SITE = "construction_site"
    CONSTRUCTION_ROOF = "construction_roof"
    CONSTRUCTION_FOUNDATION = "construction_foundation"
    CONSTRUCTION_WALL = "construction_wall"
    
    # Agricultural contexts
    FARM_FIELD = "farm_field"
    FARM_PADDOCK = "farm_paddock"
    FARM_DAM = "farm_dam"
    FARM_SILO = "farm_silo"
    
    # Urban contexts
    CITY_STREET = "city_street"
    CITY_BUILDING = "city_building"
    CITY_PARKING = "city_parking"
    CITY_SQUARE = "city_square"


class MetricSystemIntegration:
    """
    Comprehensive metric system integration for South African contexts
    Implements proper conversions and real-world applications
    """
    
    def __init__(self):
        self.conversion_factors = self._initialize_conversion_factors()
        self.context_descriptions = self._initialize_context_descriptions()
        self.typical_dimensions = self._initialize_typical_dimensions()
    
    def _initialize_conversion_factors(self) -> Dict[ConversionType, float]:
        """Initialize conversion factors for all metric units"""
        return {
            # Length conversions
            ConversionType.LENGTH_MM_CM: 0.1,
            ConversionType.LENGTH_CM_MM: 10.0,
            ConversionType.LENGTH_CM_M: 0.01,
            ConversionType.LENGTH_M_CM: 100.0,
            ConversionType.LENGTH_M_KM: 0.001,
            ConversionType.LENGTH_KM_M: 1000.0,
            
            # Area conversions
            ConversionType.AREA_MM2_CM2: 0.01,
            ConversionType.AREA_CM2_MM2: 100.0,
            ConversionType.AREA_CM2_M2: 0.0001,
            ConversionType.AREA_M2_CM2: 10000.0,
            ConversionType.AREA_M2_HA: 0.0001,
            ConversionType.AREA_HA_M2: 10000.0,
            
            # Volume conversions
            ConversionType.VOLUME_ML_L: 0.001,
            ConversionType.VOLUME_L_ML: 1000.0,
            ConversionType.VOLUME_CM3_ML: 1.0,
            ConversionType.VOLUME_ML_CM3: 1.0,
            
            # Weight conversions
            ConversionType.WEIGHT_G_KG: 0.001,
            ConversionType.WEIGHT_KG_G: 1000.0,
            ConversionType.WEIGHT_KG_T: 0.001,
            ConversionType.WEIGHT_T_KG: 1000.0,
        }
    
    def _initialize_context_descriptions(self) -> Dict[SouthAfricanContext, str]:
        """Initialize descriptions for South African contexts"""
        return {
            SouthAfricanContext.SCHOOL_CLASSROOM: "a classroom in a South African school",
            SouthAfricanContext.SCHOOL_PLAYGROUND: "a school playground in South Africa",
            SouthAfricanContext.SCHOOL_LIBRARY: "a school library in South Africa",
            SouthAfricanContext.SCHOOL_HALL: "a school hall in South Africa",
            SouthAfricanContext.HOME_GARDEN: "a home garden in South Africa",
            SouthAfricanContext.HOME_ROOM: "a room in a South African home",
            SouthAfricanContext.HOME_PATIO: "a patio in a South African home",
            SouthAfricanContext.HOME_KITCHEN: "a kitchen in a South African home",
            SouthAfricanContext.COMMUNITY_PARK: "a community park in South Africa",
            SouthAfricanContext.COMMUNITY_SPORTS_FIELD: "a sports field in South Africa",
            SouthAfricanContext.COMMUNITY_MARKET: "a community market in South Africa",
            SouthAfricanContext.COMMUNITY_CHURCH: "a church in South Africa",
            SouthAfricanContext.CONSTRUCTION_SITE: "a construction site in South Africa",
            SouthAfricanContext.CONSTRUCTION_ROOF: "a roof construction in South Africa",
            SouthAfricanContext.CONSTRUCTION_FOUNDATION: "a foundation construction in South Africa",
            SouthAfricanContext.CONSTRUCTION_WALL: "a wall construction in South Africa",
            SouthAfricanContext.FARM_FIELD: "a farm field in South Africa",
            SouthAfricanContext.FARM_PADDOCK: "a farm paddock in South Africa",
            SouthAfricanContext.FARM_DAM: "a farm dam in South Africa",
            SouthAfricanContext.FARM_SILO: "a farm silo in South Africa",
            SouthAfricanContext.CITY_STREET: "a city street in South Africa",
            SouthAfricanContext.CITY_BUILDING: "a city building in South Africa",
            SouthAfricanContext.CITY_PARKING: "a parking area in South Africa",
            SouthAfricanContext.CITY_SQUARE: "a city square in South Africa",
        }
    
    def _initialize_typical_dimensions(self) -> Dict[SouthAfricanContext, Dict[str, Tuple[float, float]]]:
        """Initialize typical dimensions for South African contexts"""
        return {
            SouthAfricanContext.SCHOOL_CLASSROOM: {
                'length': (8.0, 12.0),  # meters
                'width': (6.0, 8.0),    # meters
                'height': (2.5, 3.5)    # meters
            },
            SouthAfricanContext.SCHOOL_PLAYGROUND: {
                'length': (50.0, 100.0),  # meters
                'width': (30.0, 60.0),    # meters
            },
            SouthAfricanContext.HOME_GARDEN: {
                'length': (10.0, 30.0),   # meters
                'width': (8.0, 20.0),     # meters
            },
            SouthAfricanContext.HOME_ROOM: {
                'length': (4.0, 8.0),     # meters
                'width': (3.0, 6.0),      # meters
            },
            SouthAfricanContext.COMMUNITY_PARK: {
                'length': (100.0, 500.0), # meters
                'width': (80.0, 300.0),   # meters
            },
            SouthAfricanContext.CONSTRUCTION_SITE: {
                'length': (20.0, 100.0),  # meters
                'width': (15.0, 80.0),    # meters
            },
            SouthAfricanContext.FARM_FIELD: {
                'length': (100.0, 1000.0), # meters
                'width': (50.0, 500.0),    # meters
            },
        }
    
    def convert_value(self, value: float, conversion_type: ConversionType) -> float:
        """Convert a value using the specified conversion type"""
        factor = self.conversion_factors.get(conversion_type, 1.0)
        return round(value * factor, 2)
    
    def get_conversion_question(self, conversion_type: ConversionType, difficulty: str) -> Dict[str, Any]:
        """Generate a conversion question for the specified type and difficulty"""
        # Generate appropriate value based on difficulty
        if difficulty == 'easy':
            base_value = random.uniform(1, 20)
        elif difficulty == 'medium':
            base_value = random.uniform(10, 100)
        else:  # hard
            base_value = random.uniform(50, 500)
        
        # Convert the value
        converted_value = self.convert_value(base_value, conversion_type)
        
        # Get unit information
        from_unit, to_unit = self._get_units_from_conversion_type(conversion_type)
        
        return {
            'base_value': base_value,
            'converted_value': converted_value,
            'from_unit': from_unit,
            'to_unit': to_unit,
            'conversion_type': conversion_type
        }
    
    def _get_units_from_conversion_type(self, conversion_type: ConversionType) -> Tuple[str, str]:
        """Get from and to units from conversion type"""
        unit_mapping = {
            ConversionType.LENGTH_MM_CM: (MetricUnit.MILLIMETER.value, MetricUnit.CENTIMETER.value),
            ConversionType.LENGTH_CM_MM: (MetricUnit.CENTIMETER.value, MetricUnit.MILLIMETER.value),
            ConversionType.LENGTH_CM_M: (MetricUnit.CENTIMETER.value, MetricUnit.METER.value),
            ConversionType.LENGTH_M_CM: (MetricUnit.METER.value, MetricUnit.CENTIMETER.value),
            ConversionType.LENGTH_M_KM: (MetricUnit.METER.value, MetricUnit.KILOMETER.value),
            ConversionType.LENGTH_KM_M: (MetricUnit.KILOMETER.value, MetricUnit.METER.value),
            ConversionType.AREA_MM2_CM2: (MetricUnit.SQUARE_MILLIMETER.value, MetricUnit.SQUARE_CENTIMETER.value),
            ConversionType.AREA_CM2_MM2: (MetricUnit.SQUARE_CENTIMETER.value, MetricUnit.SQUARE_MILLIMETER.value),
            ConversionType.AREA_CM2_M2: (MetricUnit.SQUARE_CENTIMETER.value, MetricUnit.SQUARE_METER.value),
            ConversionType.AREA_M2_CM2: (MetricUnit.SQUARE_METER.value, MetricUnit.SQUARE_CENTIMETER.value),
            ConversionType.AREA_M2_HA: (MetricUnit.SQUARE_METER.value, MetricUnit.HECTARE.value),
            ConversionType.AREA_HA_M2: (MetricUnit.HECTARE.value, MetricUnit.SQUARE_METER.value),
        }
        return unit_mapping.get(conversion_type, ("unit", "unit"))
    
    def get_south_african_context(self, context_type: SouthAfricanContext) -> str:
        """Get description for South African context"""
        return self.context_descriptions.get(context_type, "a South African location")
    
    def get_typical_dimensions(self, context_type: SouthAfricanContext, dimension: str) -> Tuple[float, float]:
        """Get typical dimension range for a context"""
        context_dims = self.typical_dimensions.get(context_type, {})
        return context_dims.get(dimension, (1.0, 10.0))
    
    def generate_contextual_question(self, context_type: SouthAfricanContext, shape_type: str, difficulty: str) -> Dict[str, Any]:
        """Generate a contextual question for South African setting"""
        context_desc = self.get_south_african_context(context_type)
        
        # Get appropriate dimensions for the context
        if shape_type.startswith('triangle'):
            base_range = self.get_typical_dimensions(context_type, 'width')
            height_range = self.get_typical_dimensions(context_type, 'height')
            
            base = random.uniform(base_range[0], base_range[1])
            height = random.uniform(height_range[0], height_range[1])
            
            return {
                'context': context_desc,
                'shape': 'triangle',
                'base': round(base, 1),
                'height': round(height, 1),
                'area': round(0.5 * base * height, 1),
                'unit': 'm'
            }
        
        elif shape_type in ['rectangle', 'square']:
            length_range = self.get_typical_dimensions(context_type, 'length')
            width_range = self.get_typical_dimensions(context_type, 'width')
            
            length = random.uniform(length_range[0], length_range[1])
            width = random.uniform(width_range[0], width_range[1])
            
            return {
                'context': context_desc,
                'shape': shape_type,
                'length': round(length, 1),
                'width': round(width, 1),
                'area': round(length * width, 1),
                'unit': 'm'
            }
        
        elif shape_type.startswith('circle'):
            # For circles, use a reasonable radius based on context
            if context_type in [SouthAfricanContext.SCHOOL_CLASSROOM, SouthAfricanContext.HOME_ROOM]:
                radius_range = (1.0, 3.0)
            elif context_type in [SouthAfricanContext.SCHOOL_PLAYGROUND, SouthAfricanContext.COMMUNITY_PARK]:
                radius_range = (10.0, 50.0)
            else:
                radius_range = (5.0, 20.0)
            
            radius = random.uniform(radius_range[0], radius_range[1])
            
            return {
                'context': context_desc,
                'shape': 'circle',
                'radius': round(radius, 1),
                'area': round(3.14159 * radius * radius, 1),
                'unit': 'm'
            }
        
        return {
            'context': context_desc,
            'shape': shape_type,
            'error': 'Unsupported shape type'
        }
    
    def get_available_conversions(self, difficulty: str) -> List[ConversionType]:
        """Get available conversions for a difficulty level"""
        if difficulty == 'easy':
            return [
                ConversionType.LENGTH_MM_CM,
                ConversionType.LENGTH_CM_MM,
                ConversionType.AREA_CM2_MM2,
                ConversionType.AREA_MM2_CM2,
            ]
        elif difficulty == 'medium':
            return [
                ConversionType.LENGTH_CM_M,
                ConversionType.LENGTH_M_CM,
                ConversionType.AREA_CM2_M2,
                ConversionType.AREA_M2_CM2,
                ConversionType.VOLUME_ML_L,
                ConversionType.VOLUME_L_ML,
            ]
        else:  # hard
            return [
                ConversionType.LENGTH_M_KM,
                ConversionType.LENGTH_KM_M,
                ConversionType.AREA_M2_HA,
                ConversionType.AREA_HA_M2,
                ConversionType.WEIGHT_G_KG,
                ConversionType.WEIGHT_KG_G,
                ConversionType.WEIGHT_KG_T,
                ConversionType.WEIGHT_T_KG,
            ]
    
    def get_south_african_contexts(self, difficulty: str) -> List[SouthAfricanContext]:
        """Get appropriate South African contexts for difficulty level"""
        if difficulty == 'easy':
            return [
                SouthAfricanContext.SCHOOL_CLASSROOM,
                SouthAfricanContext.HOME_ROOM,
                SouthAfricanContext.HOME_GARDEN,
            ]
        elif difficulty == 'medium':
            return [
                SouthAfricanContext.SCHOOL_PLAYGROUND,
                SouthAfricanContext.COMMUNITY_PARK,
                SouthAfricanContext.CONSTRUCTION_SITE,
                SouthAfricanContext.HOME_PATIO,
            ]
        else:  # hard
            return [
                SouthAfricanContext.FARM_FIELD,
                SouthAfricanContext.CITY_STREET,
                SouthAfricanContext.COMMUNITY_SPORTS_FIELD,
                SouthAfricanContext.CONSTRUCTION_SITE,
            ]
