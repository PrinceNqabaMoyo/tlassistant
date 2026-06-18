from typing import List, Dict, Any

# Standard Schema for tiered hints in Scaffold Mode
# Every generator that supports Scaffold Mode should include a 'hints' list
# structured according to this schema.

def build_tiered_hints(nudge: str, concept: str, breakdown: str) -> List[Dict[str, Any]]:
    """
    Builds a standard tiered hint structure for scaffold mode.
    
    Args:
        nudge (str): A vague clue to orient the student without giving much away.
                     (e.g., "Think about the three types of business environments.")
                     
        concept (str): A direct pull or definition from caps_wiki.
                       (e.g., "The Macro environment consists of external factors 
                       the business cannot control.")
                       
        breakdown (str): A specific pointer applying the concept directly to the scenario.
                         (e.g., "The supplier raising prices is an external factor, but 
                         you have some control over who your supplier is. Which environment is that?")
                         
    Returns:
        List[Dict[str, Any]]: A list of hint objects ready to be attached to the question JSON.
    """
    return [
        {
            "tier": 1,
            "type": "nudge",
            "text": nudge,
            "xp_cost": 5
        },
        {
            "tier": 2,
            "type": "concept",
            "text": concept,
            "xp_cost": 15
        },
        {
            "tier": 3,
            "type": "breakdown",
            "text": breakdown,
            "xp_cost": 30
        }
    ]
