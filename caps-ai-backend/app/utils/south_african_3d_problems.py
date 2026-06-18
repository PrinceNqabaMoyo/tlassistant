"""
South African Context 3D Geometry Problems
Culturally relevant 3D geometry problems for Grade 7 students in South Africa
"""

import random
from typing import Dict, List, Any, Tuple
from dataclasses import dataclass
from enum import Enum

class ProblemCategory(Enum):
    HOUSING = "housing"
    WATER_STORAGE = "water_storage"
    MINING = "mining"
    AGRICULTURE = "agriculture"
    TRANSPORT = "transport"
    PACKAGING = "packaging"

@dataclass
class SouthAfrican3DProblem:
    """South African context 3D geometry problem"""
    id: str
    title: str
    description: str
    category: ProblemCategory
    shape_type: str
    given_values: Dict[str, float]
    question: str
    solution_steps: List[str]
    answer: float
    units: str
    cultural_context: str
    difficulty: str  # easy, medium, hard

class SouthAfrican3DProblemGenerator:
    """Generates culturally relevant 3D geometry problems for South African students"""
    
    def __init__(self):
        self.problems = self._initialize_problems()
    
    def _initialize_problems(self) -> List[SouthAfrican3DProblem]:
        """Initialize a collection of South African context 3D problems"""
        return [
            # HOUSING PROBLEMS
            SouthAfrican3DProblem(
                id="rdp_house_volume",
                title="RDP House Water Tank",
                description="A new RDP (Reconstruction and Development Programme) house needs a water storage tank.",
                category=ProblemCategory.HOUSING,
                shape_type="cylinder",
                given_values={"radius": 1.2, "height": 2.5},
                question="Calculate the volume of water this cylindrical tank can hold in litres.",
                solution_steps=[
                    "1. Identify the shape: Cylindrical water tank",
                    "2. Given: radius = 1.2m, height = 2.5m",
                    "3. Formula: Volume = π × r² × h",
                    "4. Calculate: V = π × (1.2)² × 2.5",
                    "5. V = π × 1.44 × 2.5 = 3.6π m³",
                    "6. Convert to litres: 3.6π × 1000 = 11,310 litres"
                ],
                answer=11310.0,
                units="litres",
                cultural_context="RDP houses are government-built homes for low-income families in South Africa. Water storage is crucial due to frequent water shortages.",
                difficulty="medium"
            ),
            
            SouthAfrican3DProblem(
                id="township_room_paint",
                title="Township Room Painting",
                description="A family in Soweto wants to paint their rectangular bedroom walls.",
                category=ProblemCategory.HOUSING,
                shape_type="rectangular_prism",
                given_values={"length": 4.0, "breadth": 3.0, "height": 2.8},
                question="Calculate the total wall area that needs painting (excluding floor and ceiling).",
                solution_steps=[
                    "1. Identify the shape: Rectangular room",
                    "2. Given: length = 4m, breadth = 3m, height = 2.8m",
                    "3. Wall area = 2 × (length × height) + 2 × (breadth × height)",
                    "4. Calculate: 2 × (4 × 2.8) + 2 × (3 × 2.8)",
                    "5. = 2 × 11.2 + 2 × 8.4 = 22.4 + 16.8 = 39.2 m²"
                ],
                answer=39.2,
                units="m²",
                cultural_context="Soweto is a famous township in Johannesburg. Many families paint their homes themselves to save money.",
                difficulty="easy"
            ),
            
            # WATER STORAGE PROBLEMS
            SouthAfrican3DProblem(
                id="jojo_tank_capacity",
                title="JoJo Tank Capacity",
                description="A farmer in the Free State needs to calculate the capacity of their JoJo water tank.",
                category=ProblemCategory.WATER_STORAGE,
                shape_type="cylinder",
                given_values={"radius": 0.8, "height": 1.5},
                question="How many litres of water can this JoJo tank hold?",
                solution_steps=[
                    "1. Identify the shape: Cylindrical JoJo tank",
                    "2. Given: radius = 0.8m, height = 1.5m",
                    "3. Formula: Volume = π × r² × h",
                    "4. Calculate: V = π × (0.8)² × 1.5",
                    "5. V = π × 0.64 × 1.5 = 0.96π m³",
                    "6. Convert to litres: 0.96π × 1000 = 3,016 litres"
                ],
                answer=3016.0,
                units="litres",
                cultural_context="JoJo tanks are popular water storage solutions in South Africa, especially in rural areas and farms.",
                difficulty="easy"
            ),
            
            SouthAfrican3DProblem(
                id="water_shortage_storage",
                title="Cape Town Water Crisis Storage",
                description="During the Cape Town water crisis, a family installed multiple water storage containers.",
                category=ProblemCategory.WATER_STORAGE,
                shape_type="rectangular_prism",
                given_values={"length": 1.0, "breadth": 0.5, "height": 0.8},
                question="If they have 6 identical rectangular water containers, what is the total water storage capacity in litres?",
                solution_steps=[
                    "1. Identify the shape: Rectangular water container",
                    "2. Given: length = 1m, breadth = 0.5m, height = 0.8m",
                    "3. Volume of one container: V = l × b × h = 1 × 0.5 × 0.8 = 0.4 m³",
                    "4. Convert to litres: 0.4 × 1000 = 400 litres per container",
                    "5. Total for 6 containers: 6 × 400 = 2,400 litres"
                ],
                answer=2400.0,
                units="litres",
                cultural_context="Cape Town experienced severe water shortages in 2017-2018, leading to 'Day Zero' concerns and water restrictions.",
                difficulty="medium"
            ),
            
            # MINING PROBLEMS
            SouthAfrican3DProblem(
                id="gold_mine_tunnel",
                title="Gold Mine Tunnel Volume",
                description="A mining engineer needs to calculate the volume of a tunnel in a gold mine near Johannesburg.",
                category=ProblemCategory.MINING,
                shape_type="rectangular_prism",
                given_values={"length": 50.0, "breadth": 3.0, "height": 2.5},
                question="Calculate the volume of air space in this mine tunnel in cubic metres.",
                solution_steps=[
                    "1. Identify the shape: Rectangular tunnel",
                    "2. Given: length = 50m, breadth = 3m, height = 2.5m",
                    "3. Formula: Volume = l × b × h",
                    "4. Calculate: V = 50 × 3 × 2.5 = 375 m³"
                ],
                answer=375.0,
                units="m³",
                cultural_context="South Africa is one of the world's largest gold producers, with major mines around Johannesburg (the 'City of Gold').",
                difficulty="easy"
            ),
            
            SouthAfrican3DProblem(
                id="diamond_mine_ore",
                title="Diamond Mine Ore Storage",
                description="A diamond mine in Kimberley needs to store processed ore in cubic containers.",
                category=ProblemCategory.MINING,
                shape_type="cube",
                given_values={"side_length": 2.0},
                question="Calculate the volume of ore that can be stored in this cubic container in cubic metres.",
                solution_steps=[
                    "1. Identify the shape: Cube",
                    "2. Given: side length = 2m",
                    "3. Formula: Volume = side³",
                    "4. Calculate: V = 2³ = 8 m³"
                ],
                answer=8.0,
                units="m³",
                cultural_context="Kimberley is famous for the 'Big Hole' diamond mine and is known as the 'Diamond City' of South Africa.",
                difficulty="easy"
            ),
            
            # AGRICULTURE PROBLEMS
            SouthAfrican3DProblem(
                id="maize_silo_capacity",
                title="Maize Silo Capacity",
                description="A farmer in Mpumalanga needs to calculate the capacity of their cylindrical maize silo.",
                category=ProblemCategory.AGRICULTURE,
                shape_type="cylinder",
                given_values={"radius": 2.5, "height": 4.0},
                question="How many cubic metres of maize can this silo hold?",
                solution_steps=[
                    "1. Identify the shape: Cylindrical silo",
                    "2. Given: radius = 2.5m, height = 4m",
                    "3. Formula: Volume = π × r² × h",
                    "4. Calculate: V = π × (2.5)² × 4",
                    "5. V = π × 6.25 × 4 = 25π m³ ≈ 78.5 m³"
                ],
                answer=78.5,
                units="m³",
                cultural_context="Mpumalanga is a major maize-producing province in South Africa. Maize is a staple food crop.",
                difficulty="medium"
            ),
            
            SouthAfrican3DProblem(
                id="wine_barrel_volume",
                title="Stellenbosch Wine Barrel",
                description="A winery in Stellenbosch needs to calculate the volume of their wine barrel.",
                category=ProblemCategory.AGRICULTURE,
                shape_type="cylinder",
                given_values={"radius": 0.6, "height": 1.2},
                question="Calculate the volume of wine this barrel can hold in litres.",
                solution_steps=[
                    "1. Identify the shape: Cylindrical wine barrel",
                    "2. Given: radius = 0.6m, height = 1.2m",
                    "3. Formula: Volume = π × r² × h",
                    "4. Calculate: V = π × (0.6)² × 1.2",
                    "5. V = π × 0.36 × 1.2 = 0.432π m³",
                    "6. Convert to litres: 0.432π × 1000 ≈ 1,357 litres"
                ],
                answer=1357.0,
                units="litres",
                cultural_context="Stellenbosch is the heart of South Africa's wine industry, known for producing world-class wines.",
                difficulty="medium"
            ),
            
            # TRANSPORT PROBLEMS
            SouthAfrican3DProblem(
                id="taxi_cargo_space",
                title="Minibus Taxi Cargo Space",
                description="A minibus taxi driver needs to calculate the cargo space for passengers' luggage.",
                category=ProblemCategory.TRANSPORT,
                shape_type="rectangular_prism",
                given_values={"length": 1.8, "breadth": 1.2, "height": 0.6},
                question="Calculate the cargo space volume in cubic metres.",
                solution_steps=[
                    "1. Identify the shape: Rectangular cargo space",
                    "2. Given: length = 1.8m, breadth = 1.2m, height = 0.6m",
                    "3. Formula: Volume = l × b × h",
                    "4. Calculate: V = 1.8 × 1.2 × 0.6 = 1.296 m³"
                ],
                answer=1.296,
                units="m³",
                cultural_context="Minibus taxis are the most common form of public transport in South Africa, especially in townships and rural areas.",
                difficulty="easy"
            ),
            
            # PACKAGING PROBLEMS
            SouthAfrican3DProblem(
                id="biltong_packaging",
                title="Biltong Packaging Box",
                description="A biltong manufacturer needs to design packaging boxes for their product.",
                category=ProblemCategory.PACKAGING,
                shape_type="rectangular_prism",
                given_values={"length": 0.3, "breadth": 0.2, "height": 0.1},
                question="Calculate the volume of this biltong packaging box in cubic centimetres.",
                solution_steps=[
                    "1. Identify the shape: Rectangular packaging box",
                    "2. Given: length = 0.3m, breadth = 0.2m, height = 0.1m",
                    "3. Convert to cm: 30cm × 20cm × 10cm",
                    "4. Formula: Volume = l × b × h",
                    "5. Calculate: V = 30 × 20 × 10 = 6,000 cm³"
                ],
                answer=6000.0,
                units="cm³",
                cultural_context="Biltong is a popular South African dried meat snack, similar to jerky but with a unique flavor.",
                difficulty="easy"
            ),
            
            SouthAfrican3DProblem(
                id="rooibos_tea_box",
                title="Rooibos Tea Box Volume",
                description="A tea company needs to calculate the volume of their rooibos tea packaging.",
                category=ProblemCategory.PACKAGING,
                shape_type="rectangular_prism",
                given_values={"length": 0.15, "breadth": 0.1, "height": 0.08},
                question="What is the volume of this tea box in cubic centimetres?",
                solution_steps=[
                    "1. Identify the shape: Rectangular tea box",
                    "2. Given: length = 0.15m, breadth = 0.1m, height = 0.08m",
                    "3. Convert to cm: 15cm × 10cm × 8cm",
                    "4. Formula: Volume = l × b × h",
                    "5. Calculate: V = 15 × 10 × 8 = 1,200 cm³"
                ],
                answer=1200.0,
                units="cm³",
                cultural_context="Rooibos tea is a uniquely South African herbal tea, grown only in the Cederberg region of the Western Cape.",
                difficulty="easy"
            ),

            # ADVANCED PROBLEMS - Missing Dimension Challenges
            
            SouthAfrican3DProblem(
                id="rdp_house_missing_height",
                title="RDP House Water Tank - Missing Height",
                description="An RDP house has a cylindrical water tank with a radius of 1.2m and a volume of 11,310 litres. Find the height of the tank.",
                category=ProblemCategory.HOUSING,
                shape_type="cylinder",
                given_values={"radius": 1.2, "volume": 11.31},
                question="What is the height of the water tank in metres?",
                solution_steps=[
                    "1. Identify the shape: Cylindrical water tank",
                    "2. Given: radius = 1.2m, volume = 11.31 m³ (11,310 litres = 11.31 m³)",
                    "3. Formula: Volume = π × r² × h",
                    "4. Rearrange: h = Volume ÷ (π × r²)",
                    "5. Calculate: h = 11.31 ÷ (π × 1.44) = 11.31 ÷ 4.52 = 2.5m"
                ],
                answer=2.5,
                units="m",
                cultural_context="RDP houses often have water storage challenges. Calculating tank dimensions helps ensure adequate water supply.",
                difficulty="medium"
            ),

            SouthAfrican3DProblem(
                id="mining_tunnel_missing_width",
                title="Gold Mine Tunnel - Missing Width",
                description="A gold mine tunnel has a length of 50m, height of 2.5m, and volume of 375 m³. Find the width of the tunnel.",
                category=ProblemCategory.MINING,
                shape_type="rectangular_prism",
                given_values={"length": 50.0, "height": 2.5, "volume": 375.0},
                question="What is the width of the mine tunnel in metres?",
                solution_steps=[
                    "1. Identify the shape: Rectangular tunnel",
                    "2. Given: length = 50m, height = 2.5m, volume = 375 m³",
                    "3. Formula: Volume = l × w × h",
                    "4. Rearrange: w = Volume ÷ (l × h)",
                    "5. Calculate: w = 375 ÷ (50 × 2.5) = 375 ÷ 125 = 3m"
                ],
                answer=3.0,
                units="m",
                cultural_context="Mining engineers need to calculate tunnel dimensions for safety and efficiency in South Africa's gold mines.",
                difficulty="medium"
            ),

            SouthAfrican3DProblem(
                id="wine_barrel_missing_radius",
                title="Stellenbosch Wine Barrel - Missing Radius",
                description="A Stellenbosch winery has a cylindrical wine barrel with height 1.2m and volume 1,357 litres. Find the radius of the barrel.",
                category=ProblemCategory.AGRICULTURE,
                shape_type="cylinder",
                given_values={"height": 1.2, "volume": 1.357},
                question="What is the radius of the wine barrel in metres?",
                solution_steps=[
                    "1. Identify the shape: Cylindrical wine barrel",
                    "2. Given: height = 1.2m, volume = 1.357 m³ (1,357 litres = 1.357 m³)",
                    "3. Formula: Volume = π × r² × h",
                    "4. Rearrange: r² = Volume ÷ (π × h)",
                    "5. Calculate: r² = 1.357 ÷ (π × 1.2) = 1.357 ÷ 3.77 = 0.36",
                    "6. Therefore: r = √0.36 = 0.6m"
                ],
                answer=0.6,
                units="m",
                cultural_context="Wine barrel dimensions affect wine aging. Stellenbosch wineries need precise calculations for optimal wine production.",
                difficulty="hard"
            ),

            SouthAfrican3DProblem(
                id="maize_silo_missing_height",
                title="Maize Silo - Missing Height",
                description="A farmer in Mpumalanga has a cylindrical maize silo with radius 2.5m and volume 78.5 m³. Find the height of the silo.",
                category=ProblemCategory.AGRICULTURE,
                shape_type="cylinder",
                given_values={"radius": 2.5, "volume": 78.5},
                question="What is the height of the maize silo in metres?",
                solution_steps=[
                    "1. Identify the shape: Cylindrical silo",
                    "2. Given: radius = 2.5m, volume = 78.5 m³",
                    "3. Formula: Volume = π × r² × h",
                    "4. Rearrange: h = Volume ÷ (π × r²)",
                    "5. Calculate: h = 78.5 ÷ (π × 6.25) = 78.5 ÷ 19.63 = 4m"
                ],
                answer=4.0,
                units="m",
                cultural_context="Maize storage capacity is crucial for South African farmers. Proper silo dimensions ensure efficient grain storage.",
                difficulty="medium"
            ),

            SouthAfrican3DProblem(
                id="biltong_box_missing_length",
                title="Biltong Packaging - Missing Length",
                description="A biltong manufacturer needs a rectangular box with breadth 20cm, height 10cm, and volume 6,000 cm³. Find the length of the box.",
                category=ProblemCategory.PACKAGING,
                shape_type="rectangular_prism",
                given_values={"breadth": 20, "height": 10, "volume": 6000},
                question="What is the length of the biltong box in centimetres?",
                solution_steps=[
                    "1. Identify the shape: Rectangular packaging box",
                    "2. Given: breadth = 20cm, height = 10cm, volume = 6,000 cm³",
                    "3. Formula: Volume = l × b × h",
                    "4. Rearrange: l = Volume ÷ (b × h)",
                    "5. Calculate: l = 6,000 ÷ (20 × 10) = 6,000 ÷ 200 = 30cm"
                ],
                answer=30.0,
                units="cm",
                cultural_context="Biltong packaging must be precise to maintain product quality and meet South African food safety standards.",
                difficulty="easy"
            ),

            SouthAfrican3DProblem(
                id="jojo_tank_optimization",
                title="JoJo Tank Optimization Challenge",
                description="A farmer needs a JoJo tank with exactly 3,016 litres capacity. The tank must have a radius of 0.8m. What height is needed?",
                category=ProblemCategory.WATER_STORAGE,
                shape_type="cylinder",
                given_values={"radius": 0.8, "volume": 3.016},
                question="What height is needed for the JoJo tank in metres?",
                solution_steps=[
                    "1. Identify the shape: Cylindrical JoJo tank",
                    "2. Given: radius = 0.8m, volume = 3.016 m³ (3,016 litres = 3.016 m³)",
                    "3. Formula: Volume = π × r² × h",
                    "4. Rearrange: h = Volume ÷ (π × r²)",
                    "5. Calculate: h = 3.016 ÷ (π × 0.64) = 3.016 ÷ 2.01 = 1.5m"
                ],
                answer=1.5,
                units="m",
                cultural_context="JoJo tank optimization is important for water storage efficiency in South African farming communities.",
                difficulty="medium"
            ),

            SouthAfrican3DProblem(
                id="township_room_missing_breadth",
                title="Township Room - Missing Breadth",
                description="A family in Soweto wants to paint their room. The room is 4m long, 2.8m high, and has a wall area of 39.2 m². Find the breadth of the room.",
                category=ProblemCategory.HOUSING,
                shape_type="rectangular_prism",
                given_values={"length": 4.0, "height": 2.8, "wall_area": 39.2},
                question="What is the breadth of the room in metres?",
                solution_steps=[
                    "1. Identify the shape: Rectangular room",
                    "2. Given: length = 4m, height = 2.8m, wall area = 39.2 m²",
                    "3. Wall area formula: 2 × (length × height) + 2 × (breadth × height)",
                    "4. Substitute: 39.2 = 2 × (4 × 2.8) + 2 × (breadth × 2.8)",
                    "5. Calculate: 39.2 = 22.4 + 5.6 × breadth",
                    "6. Solve: 16.8 = 5.6 × breadth, so breadth = 3m"
                ],
                answer=3.0,
                units="m",
                cultural_context="Township families often need to calculate room dimensions for DIY home improvements and cost estimation.",
                difficulty="hard"
            )
        ]
    
    def get_problem_by_category(self, category: ProblemCategory) -> List[SouthAfrican3DProblem]:
        """Get all problems in a specific category"""
        return [p for p in self.problems if p.category == category]
    
    def get_problem_by_difficulty(self, difficulty: str) -> List[SouthAfrican3DProblem]:
        """Get all problems of a specific difficulty level"""
        return [p for p in self.problems if p.difficulty == difficulty]
    
    def get_random_problem(self, category: ProblemCategory = None, difficulty: str = None) -> SouthAfrican3DProblem:
        """Get a random problem, optionally filtered by category and/or difficulty"""
        filtered_problems = self.problems
        
        if category:
            filtered_problems = [p for p in filtered_problems if p.category == category]
        
        if difficulty:
            filtered_problems = [p for p in filtered_problems if p.difficulty == difficulty]
        
        if not filtered_problems:
            raise ValueError("No problems found matching the criteria")
        
        return random.choice(filtered_problems)
    
    def get_problem_by_id(self, problem_id: str) -> SouthAfrican3DProblem:
        """Get a specific problem by its ID"""
        for problem in self.problems:
            if problem.id == problem_id:
                return problem
        raise ValueError(f"Problem with ID '{problem_id}' not found")
    
    def get_all_categories(self) -> List[ProblemCategory]:
        """Get all available problem categories"""
        return list(ProblemCategory)
    
    def get_problem_statistics(self) -> Dict[str, Any]:
        """Get statistics about available problems"""
        stats = {
            "total_problems": len(self.problems),
            "by_category": {},
            "by_difficulty": {
                "easy": 0,
                "medium": 0,
                "hard": 0
            }
        }
        
        for problem in self.problems:
            # Count by category
            cat_name = problem.category.value
            if cat_name not in stats["by_category"]:
                stats["by_category"][cat_name] = 0
            stats["by_category"][cat_name] += 1
            
            # Count by difficulty
            stats["by_difficulty"][problem.difficulty] += 1
        
        return stats
