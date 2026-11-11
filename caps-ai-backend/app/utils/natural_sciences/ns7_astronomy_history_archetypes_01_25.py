"""Grade 7 Natural Sciences - Historical Development of Astronomy: Archetypes 01 to 25.
Grounded in CAPS: curriculum_docs_auto/NaturalSciences_Gr7/Term 4/02. Historical development of astronomy.md
Focus: Indigenous African starlore (Xhosa Isilimela/Pleiades, Sotho Selemela, San Milky Way/Magellanic Clouds,
Venus/iKhwezi, Southern Cross navigation, Adam's Calendar), Geocentric vs Heliocentric models,
Ptolemaic epicycles, Copernicus, retrograde motion of Mars, Tycho Brahe, Kepler's laws, Galileo's telescope discoveries.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def arch_01_indigenous_african_astronomy_heritage(rng: random.Random) -> Dict[str, Any]:
    peoples = [
        ("Xhosa, Zulu, and Sotho-Tswana societies", "agricultural cycles, cultural ceremonies, and seasonal navigation"),
        ("Khoisan hunter-gatherer communities", "mythological starlore, animal migration tracking, and campfire storytelling"),
        ("traditional pastoralist and farming communities across Southern Africa", "determining optimal soil preparation and harvesting windows")
    ]
    grp, use_case = rng.choice(peoples)
    prompt = (
        f"Long before the invention of optical telescopes, {grp} systematically studied the night sky for {use_case}.\n\n"
        "How is traditional indigenous astronomical knowledge (IK) preserved and transmitted across generations in Africa?"
    )
    correct = "Through rich oral traditions, cultural songs, proverbs, folktales, and practical seasonal ceremonies."
    options = [
        correct,
        "Exclusively on digital flash drives buried in sacred caves.",
        "Through printed university scientific textbooks written in Latin.",
        "Through radio transmissions received from orbiting space satellites."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Understand Indigenous Knowledge Systems (IKS):\n"
        "Indigenous knowledge is deeply rooted in practical environmental observation.\n"
        "Step 2: Transmission method:\n"
        "Knowledge of celestial patterns was passed down through generations orally via stories, songs, calendars, and cultural ceremonies."
    )
    return {
        "id": f"ns7_astro_01_{rng.randint(100000, 999999)}",
        "subskill": "01_indigenous_african_astronomy_heritage",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "How did communities without printing presses pass on wisdom?",
            "tier_2": "Oral traditions, songs, and cultural practices.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["indigenous_astronomy_transmission_error"]
    }


def arch_02_xhosa_traditional_calendar_isilimela_pleiades(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In traditional isiXhosa starlore, the Pleiades star cluster is known as **Isilimela**.\n\n"
        "What pivotal seasonal event in the traditional Xhosa calendar is marked by the dawn rising of Isilimela in June?"
    )
    correct = "The start of the agricultural new year, signaling the time to begin plowing fields, as well as initiation into manhood."
    options = [
        correct,
        "The start of mid-summer beach holidays in coastal cities.",
        "The peak of the autumn deciduous grape harvest in Stellenbosch.",
        "The arrival of ocean tidal waves along the Wild Coast."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Identify Isilimela:\n"
        "Isilimela is the Pleiades (Seven Sisters) open star cluster.\n"
        "Step 2: Cultural and agricultural significance:\n"
        "Its dawn appearance in early June marks the beginning of the Xhosa new year (inyanga yokulima - time for plowing and planting preparations) and cultural transitions."
    )
    return {
        "id": f"ns7_astro_02_{rng.randint(100000, 999999)}",
        "subskill": "02_xhosa_traditional_calendar_isilimela_pleiades",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Isilimela is connected to 'ukulima' (to plow/plant).",
            "tier_2": "It marks the agricultural new year in June.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["isilimela_calendar_significance_error"]
    }


def arch_03_sotho_tswana_starlore_selemela_agriculture(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In Sesotho and Setswana culture, the Pleiades cluster is revered as **Selemela** (from the verb 'ho lema' / 'go lema', meaning to plow or cultivate).\n\n"
        "What practical message did elders convey to farming communities when Selemela appeared on the horizon?"
    )
    correct = "'The planting stars have arrived; sharpen your hoes and prepare the fields for crops.'"
    options = [
        correct,
        "'Winter has just ended; take cattle into the snow peaks.'",
        "'Stop planting all grains because the soil has lost its nutrients forever.'",
        "'Prepare boats to sail across the Indian Ocean.'"
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Understand linguistic connection:\n"
        "Selemela derives from 'lema' (to plow or farm).\n"
        "Step 2: Agricultural instruction:\n"
        "When Selemela appeared in the morning sky, it served as an unmistakable astronomical calendar cue to begin preparing seedbeds for the upcoming summer rains."
    )
    return {
        "id": f"ns7_astro_03_{rng.randint(100000, 999999)}",
        "subskill": "03_sotho_tswana_starlore_selemela_agriculture",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "What does 'ho lema' mean in Sesotho/Setswana?",
            "tier_2": "It means to plow or cultivate crops.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["selemela_linguistic_agricultural_link"]
    }


def arch_04_san_bushman_starlore_milky_way_ashes(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In the rich mythological starlore of the |Xam San (Bushman) people of Southern Africa, "
        "what poetic legend explains the creation of the glowing band of the **Milky Way**?"
    )
    correct = "A young girl threw glowing wood embers and white ashes from a campfire high into the night sky, creating a glowing path to light the way home in darkness."
    options = [
        correct,
        "A giant serpent spilled fresh cow milk across a stone mountain plateau.",
        "A fierce desert dust storm carried white salt grains into outer space.",
        "Thunderbolts tore a white seam in the dark cloth of the heavens."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Recall |Xam San mythology:\n"
        "Recorded in the Bleek and Lloyd archives.\n"
        "Step 2: The story:\n"
        "The girl threw glowing red and white embers from a fire into the sky; the red embers became red stars and the white ash became the glowing pathway of the Milky Way."
    )
    return {
        "id": f"ns7_astro_04_{rng.randint(100000, 999999)}",
        "subskill": "04_san_bushman_starlore_milky_way_ashes",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Think about campfire ashes thrown into the night air.",
            "tier_2": "Wood embers and white ashes created the glowing starry path.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["san_starlore_mythology_confusion"]
    }


def arch_05_san_bushman_celestial_hunters_magellanic_clouds(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "The Large and Small Magellanic Clouds are two dwarf galaxies clearly visible in Southern Hemisphere skies. "
        "How were these celestial clouds traditionally perceived in indigenous Sotho, Tswana, and San lore?"
    )
    correct = "As celestial animals or hunting grounds, such as 'Dintsa le Dikolobe' (hunting dogs chasing wild pigs) or celestial steenbok."
    options = [
        correct,
        "As giant steam clouds produced by active ocean steamships.",
        "As alien spaceships preparing to enter Earth's atmosphere.",
        "As floating icebergs drifting across the upper stratosphere."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Identify Magellanic Clouds in African skies:\n"
        "Easily seen with the naked eye from dark African landscapes.\n"
        "Step 2: Indigenous interpretation:\n"
        "Sotho/Tswana starlore saw them as 'Dintsa le Dikolobe' (dogs and wild pigs), weaving deep natural observations into cultural astronomy."
    )
    return {
        "id": f"ns7_astro_05_{rng.randint(100000, 999999)}",
        "subskill": "05_san_bushman_celestial_hunters_magellanic_clouds",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "They were seen as celestial animals and hunting scenes.",
            "tier_2": "Hunting dogs chasing pigs (Dintsa le Dikolobe).",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["magellanic_clouds_indigenous_interpretation"]
    }


def arch_06_venus_morning_evening_star_ikhwezi(rng: random.Random) -> Dict[str, Any]:
    names = [
        ("iKhwezi (isiXhosa / isiZulu)", "the Morning Star shining brilliantly in the eastern predawn sky"),
        ("Kgogamashego (Setswana / Sesotho)", "the star that draws on the night / morning star signalling the coming day"),
        ("Naledi ya Moso (Sesotho)", "the bright morning star guiding herders out to pasture")
    ]
    trad_name, role = rng.choice(names)
    prompt = (
        f"In traditional African astronomy, **{trad_name}** represents {role}.\n\n"
        "Which celestial body in our solar system is actually being observed as the 'Morning Star' and 'Evening Star'?"
    )
    correct = "The planet Venus (the second planet from the Sun, reflecting brilliant sunlight from its dense clouds)."
    options = [
        correct,
        "The North Star (Polaris), which is a distant supergiant star.",
        "The planet Mars, famous for its red dusty surface.",
        "Earth's natural satellite, the Moon, during a lunar eclipse."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Identify the astronomical body:\n"
        "The 'Morning Star' and 'Evening Star' are not true stars at all; they are the planet Venus.\n"
        "Step 2: Why it shines so bright:\n"
        "Because Venus has highly reflective sulfuric acid clouds and is close to Earth and the Sun, it outshines all stars in the twilight sky."
    )
    return {
        "id": f"ns7_astro_06_{rng.randint(100000, 999999)}",
        "subskill": "06_venus_morning_evening_star_ikhwezi",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Is the Morning Star a true star or a reflective planet?",
            "tier_2": "It is the planet Venus.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["venus_is_a_true_star_fallacy"]
    }


def arch_07_southern_cross_crux_and_pointers_navigation(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Travellers across the open veld of Southern Africa have used the **Southern Cross (Crux)** "
        "and its two bright **Pointer stars** (Alpha and Beta Centauri) for centuries.\n\n"
        "How is this celestial constellation utilized as a navigational compass at night?"
    )
    correct = "By extending the long axis of the Cross 4.5 times toward the horizon, travellers locate the South Celestial Pole, indicating True South."
    options = [
        correct,
        "The Cross points like an arrow directly toward the geographic North Pole.",
        "The two Pointers always point directly toward the rising Sun in the morning.",
        "The Cross rotates to point towards whichever town has a burning campfire."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Locate the Southern Cross:\n"
        "Crux consists of four main bright stars arranged in a kite/cross pattern.\n"
        "Step 2: Navigational method:\n"
        "Extend a line through the long axis of the cross 4.5 times in the direction of the foot of the cross. Dropping a vertical line to the horizon marks True South."
    )
    return {
        "id": f"ns7_astro_07_{rng.randint(100000, 999999)}",
        "subskill": "07_southern_cross_crux_and_pointers_navigation",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Which cardinal compass direction does the Southern Cross help locate?",
            "tier_2": "It points to the South Celestial Pole (True South).",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["southern_cross_navigation_method_error"]
    }


def arch_08_sirius_inkwenkwezi_agricultural_calendar(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Sirius is the brightest star in the entire night sky, known in isiXhosa as **Inkwenkwezi**.\n\n"
        "In traditional African societies as well as ancient Egypt, what was the primary practical use of observing the seasonal rising of Sirius?"
    )
    correct = "Predicting the onset of seasonal flooding, warm weather, and timing agricultural planting cycles."
    options = [
        correct,
        "Determining when to construct iron-smelting blast furnaces in winter.",
        "Predicting total solar eclipses with 100% mathematical certainty.",
        "Warning communities of approaching volcanic ash clouds."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Sirius in cultural astronomy:\n"
        "In ancient Egypt, the heliacal rising of Sirius warned of the annual Nile flood.\n"
        "Step 2: Southern Africa:\n"
        "In Southern Africa, the prominence of Sirius (Inkwenkwezi) in summer skies signalled warm growing weather and coordinated farming tasks."
    )
    return {
        "id": f"ns7_astro_08_{rng.randint(100000, 999999)}",
        "subskill": "08_sirius_inkwenkwezi_agricultural_calendar",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Sirius is the brightest star; how did farmers use it?",
            "tier_2": "To predict seasons, warmth, and planting cycles.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["sirius_seasonal_tracking_confusion"]
    }


def arch_09_ancient_african_observatories_adams_calendar(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "At **Adam's Calendar** (near Kaapsehoop in Mpumalanga, South Africa), standing stones are arranged in a circular configuration.\n\n"
        "Archaeologists and archaeoastronomers suggest these megalithic standing stones served as an ancient observatory for tracking:"
    )
    correct = "The solstices, equinoxes, and seasonal transit of the Sun across the cardinal directions."
    options = [
        correct,
        "The flight paths of modern jet airliners across Africa.",
        "Underground diamond and gold seam concentrations.",
        "Radio wave transmissions from Jupiter."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Identify Adam's Calendar:\n"
        "A series of aligned standing stones in Mpumalanga.\n"
        "Step 2: Astronomical alignment:\n"
        "Certain stones align precisely with sunrise on the winter solstice, summer solstice, and equinoxes, demonstrating ancient astronomical tracking in Southern Africa."
    )
    return {
        "id": f"ns7_astro_09_{rng.randint(100000, 999999)}",
        "subskill": "09_ancient_african_observatories_adams_calendar",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "What do ancient stone circles track in the sky?",
            "tier_2": "Solstices, equinoxes, and solar movements.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["megalithic_observatory_purpose_error"]
    }


def arch_10_ancient_african_observatories_nabta_playa(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In southern Egypt (Nubia), the **Nabta Playa** stone circle dates back over 6 000 years, "
        "predating England's Stonehenge by more than a millennium.\n\n"
        "What key astronomical alignment did the Neolithic pastoralists build into Nabta Playa?"
    )
    correct = "Alignments marking the summer solstice sunrise, which signaled the imminent arrival of life-giving monsoon summer rains."
    options = [
        correct,
        "Alignments predicting the exact date of lunar eclipses for the next 10 000 years.",
        "Laser-like markings to guide extraterrestrial spacecraft.",
        "Markings showing the diameter of the planet Neptune."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Context of Nabta Playa:\n"
        "Constructed around 4500-4000 BCE in the Sahara desert.\n"
        "Step 2: Purpose:\n"
        "The standing stones align with the summer solstice sunrise, giving nomadic pastoralists a calendar warning that annual monsoon rains were about to arrive."
    )
    return {
        "id": f"ns7_astro_10_{rng.randint(100000, 999999)}",
        "subskill": "10_ancient_african_observatories_nabta_playa",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Which solstice heralds the summer rainy season?",
            "tier_2": "Summer solstice sunrise alignment.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["nabta_playa_chronology_and_alignment"]
    }


def arch_11_cultural_interpretations_shooting_stars_meteors(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In indigenous cultures across the world, people observed 'shooting stars' streak across the night sky.\n\n"
        "What is the actual scientific nature of a shooting star (meteor)?"
    )
    correct = "A small grain of space dust or rock (meteoroid) burning up due to frictional heating upon entering Earth's upper atmosphere."
    options = [
        correct,
        "A distant nuclear star detaching from its constellation and plunging into the ocean.",
        "A lightning bolt traveling backward from outer space into the clouds.",
        "A piece of volcanic ash ejected from the center of the Moon."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Clarify terminology:\n"
        "A 'shooting star' is not a true star.\n"
        "Step 2: Physics of a meteor:\n"
        "When tiny space rock fragments (often from cometary trails) enter Earth's atmosphere at high speeds (30-70 km/s), ram-pressure and friction compress and heat the air, creating a brief luminous streak."
    )
    return {
        "id": f"ns7_astro_11_{rng.randint(100000, 999999)}",
        "subskill": "11_cultural_interpretations_shooting_stars_meteors",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Does a real star fall from the sky?",
            "tier_2": "Small space dust particles burn in Earth's atmosphere.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["shooting_star_is_a_falling_star_myth"]
    }


def arch_12_cultural_interpretations_comets_celestial_messengers(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Historically, the sudden appearance of a bright **comet** with a glowing tail sweeping across constellations "
        "was viewed with great apprehension in many ancient societies.\n\n"
        "How were comets traditionally interpreted, and what are comets in modern scientific understanding?"
    )
    correct = "Traditionally seen as omens of major upheaval or royal deaths; scientifically, they are 'dirty snowballs' of ice, dust, and rock orbiting the Sun."
    options = [
        correct,
        "Traditionally seen as harmless rain clouds; scientifically, they are burning metal airships.",
        "Traditionally worshiped as the creators of salt; scientifically, they are pieces of the Sun's core.",
        "Traditionally believed to be migrating spirits; scientifically, they are optical illusions with no physical mass."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Historical cultural interpretation:\n"
        "Because comets appeared unpredictably, many cultures regarded them as supernatural portents or warnings of drought, war, or change.\n"
        "Step 2: Modern scientific definition:\n"
        "Comets are icy small solar system bodies that sublimate when approaching the Sun, creating a glowing coma and extended dust/gas tail."
    )
    return {
        "id": f"ns7_astro_12_{rng.randint(100000, 999999)}",
        "subskill": "12_cultural_interpretations_comets_celestial_messengers",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "What are comets made of? Ice, rock, and dust.",
            "tier_2": "Ancient societies saw them as dramatic omens.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["comet_omen_vs_physical_nature"]
    }


def arch_13_geocentric_model_aristotle_ptolemy_earth_centred(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "For over 1 500 years, Western and Middle Eastern astronomy was dominated by the **Geocentric model**, "
        "advanced by the ancient Greek philosophers Aristotle and Claudius Ptolemy.\n\n"
        "What was the central claim of this geocentric model?"
    )
    correct = "Earth is stationary at the exact center of the universe, and the Moon, Sun, planets, and stars all revolve around Earth in circular orbits."
    options = [
        correct,
        "The Sun is at the center of the universe and Earth orbits it as a normal planet.",
        "Jupiter is at the center and all stars orbit Jupiter in straight lines.",
        "Earth is floating in an infinite ocean of freshwater inside an iceberg."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Analyze etymology:\n"
        "'Geo' means Earth; 'centric' means centered.\n"
        "Step 2: Principles of Geocentric model:\n"
        "Ptolemy and Aristotle believed Earth was stationary and unmoving at the centre, with celestial bodies carried on revolving crystal spheres."
    )
    r_earth = rng.choice([16, 18, 20])
    spec = {
        "kind": "inline_svg",
        "svg": f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 180" width="100%" height="140"><circle cx="140" cy="90" r="{r_earth}" fill="#3b82f6"/><text x="140" y="95" text-anchor="middle" fill="#ffffff" font-size="9">Earth</text><circle cx="140" cy="90" r="45" fill="none" stroke="#94a3b8" stroke-dasharray="3"/><circle cx="185" cy="90" r="8" fill="#64748b"/><text x="185" y="105" font-size="8">Moon</text><circle cx="140" cy="90" r="75" fill="none" stroke="#f59e0b" stroke-dasharray="3"/><circle cx="215" cy="90" r="12" fill="#f59e0b"/><text x="215" y="110" font-size="8">Sun</text><text x="140" y="20" text-anchor="middle" fill="#0f172a" font-size="11" font-weight="bold">Geocentric Model (Earth at Centre)</text></svg>',
        "diagram_role": "context"
    }
    return {
        "id": f"ns7_astro_13_{rng.randint(100000, 999999)}",
        "subskill": "13_geocentric_model_aristotle_ptolemy_earth_centred",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "diagram_spec": spec,
        "hints": {
            "tier_1": "What does 'geo' mean? Earth.",
            "tier_2": "Geocentric means Earth-centered.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["geocentric_model_principles_error"]
    }


def arch_14_ptolemaic_epicycles_explaining_planetary_motion(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In the Ptolemaic geocentric system, astronomers struggled to explain why planets like Mars "
        "periodically appeared to slow down, stop, and temporarily move backwards in the night sky.\n\n"
        "What complex geometric mechanism did Ptolemy invent to explain this retrograde motion while keeping Earth at the centre?"
    )
    correct = "Epicycles: Small circular orbits whose centres moved along a larger circular orbit (deferent) around Earth."
    options = [
        correct,
        "Helical wormholes that swallowed and regurgitated Mars every few months.",
        "Parabolic rocket boosters built into the surface of planetary crusts.",
        "Square glass walls that bounced the planets back like billiard balls."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: The problem of retrograde motion:\n"
        "Planets occasionally appear to move westward (backward) relative to background stars.\n"
        "Step 2: Ptolemy's mathematical fix:\n"
        "To preserve circular motion around stationary Earth, Ptolemy introduced epicycles (circles rolling upon larger circles)."
    )
    return {
        "id": f"ns7_astro_14_{rng.randint(100000, 999999)}",
        "subskill": "14_ptolemaic_epicycles_explaining_planetary_motion",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Think about circles moving upon circles.",
            "tier_2": "Ptolemy called these circles on circles 'epicycles'.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["epicycle_concept_confusion"]
    }


def arch_15_heliocentric_model_copernicus_sun_centred(rng: random.Random) -> Dict[str, Any]:
    year = "1543"
    prompt = (
        f"In {year}, the Polish astronomer Nicolaus Copernicus published *De revolutionibus orbium coelestium*, "
        "launching the Copernican Revolution.\n\n"
        "What fundamental model of the solar system did Copernicus propose?"
    )
    correct = "The Heliocentric model: The Sun is at the centre, and Earth is merely one of several planets revolving around the Sun."
    options = [
        correct,
        "The Flat Earth model: Earth is a flat disc supported by giant pillars over a cosmic abyss.",
        "The Lunar model: The Moon is the central star around which both the Sun and Earth revolve.",
        "The Static model: The universe has no motion and all stars are stationary in an icy dome."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Etymology:\n"
        "'Helios' is Greek for Sun; 'centric' means centered.\n"
        "Step 2: Copernicus's breakthrough:\n"
        "Copernicus demonstrated that placing the Sun at the center and having Earth rotate daily on its axis and revolve annually around the Sun provided a far simpler, elegant explanation of the cosmos."
    )
    r_sun = rng.choice([20, 22, 24])
    spec = {
        "kind": "inline_svg",
        "svg": f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 180" width="100%" height="140"><circle cx="140" cy="90" r="{r_sun}" fill="#f59e0b"/><text x="140" y="95" text-anchor="middle" fill="#ffffff" font-size="9">Sun</text><circle cx="140" cy="90" r="50" fill="none" stroke="#3b82f6" stroke-dasharray="3"/><circle cx="190" cy="90" r="9" fill="#3b82f6"/><text x="190" y="105" font-size="8">Earth</text><circle cx="140" cy="90" r="80" fill="none" stroke="#ef4444" stroke-dasharray="3"/><circle cx="220" cy="90" r="7" fill="#ef4444"/><text x="220" y="105" font-size="8">Mars</text><text x="140" y="20" text-anchor="middle" fill="#0f172a" font-size="11" font-weight="bold">Heliocentric Model (Sun at Centre)</text></svg>',
        "diagram_role": "context"
    }
    return {
        "id": f"ns7_astro_15_{rng.randint(100000, 999999)}",
        "subskill": "15_heliocentric_model_copernicus_sun_centred",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "diagram_spec": spec,
        "hints": {
            "tier_1": "What does 'helios' mean? Sun.",
            "tier_2": "Copernicus placed the Sun at the center.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["copernican_heliocentric_model_principles"]
    }


def arch_16_apparent_retrograde_motion_mars_perspective(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In the Copernican heliocentric model, how is the apparent backward (retrograde) loop "
        "of Mars in the night sky explained naturally without needing complicated epicycles?"
    )
    correct = "Earth orbits the Sun faster on an inside track and overtakes slower-moving Mars, creating an optical illusion of backward motion against distant stars."
    options = [
        correct,
        "Mars physically stops, turns around, and flies backwards in its orbital track for three weeks.",
        "The Sun's gravity repels Mars into a giant figure-eight spiral every two years.",
        "Earth's magnetic field bends the light rays of Mars in a reverse optical mirror."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Perspective illusion:\n"
        "Consider driving in a fast car overtaking a slower truck on the highway: against distant scenery, the truck appears to move backwards.\n"
        "Step 2: Heliocentric explanation:\n"
        "Earth (inner, faster planet) overtakes Mars (outer, slower planet). Against background constellations, Mars appears to loop backwards."
    )
    return {
        "id": f"ns7_astro_16_{rng.randint(100000, 999999)}",
        "subskill": "16_apparent_retrograde_motion_mars_perspective",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Think about passing a slower car on the highway.",
            "tier_2": "Faster inner Earth overtakes slower outer Mars.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["retrograde_motion_physical_vs_perspective_error"]
    }


def arch_17_tycho_brahe_naked_eye_astronomical_measurements(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "The Danish nobleman Tycho Brahe (1546–1601) built the state-of-the-art Uraniborg observatory "
        "decades before the telescope was invented.\n\n"
        "What made Tycho Brahe's astronomical observations so historically vital to the Scientific Revolution?"
    )
    correct = "He used huge brass quadrants and sextants to compile decades of highly accurate, continuous, naked-eye measurements of planetary positions."
    options = [
        correct,
        "He invented the first digital radio telescope and discovered pulsars.",
        "He was the first human astronaut to travel to the Moon and return.",
        "He mathematically proved that Earth was completely hollow like a basketball."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Tycho Brahe's contribution:\n"
        "Tycho did not have telescopes, but designed massive sighting instruments.\n"
        "Step 2: Historical significance:\n"
        "His unprecedented precision (accurate to 1-2 arcminutes) provided the raw empirical data that Johannes Kepler later used to uncover the laws of planetary motion."
    )
    return {
        "id": f"ns7_astro_17_{rng.randint(100000, 999999)}",
        "subskill": "17_tycho_brahe_naked_eye_astronomical_measurements",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Tycho lived before telescopes were invented.",
            "tier_2": "He made the most accurate naked-eye planetary measurements in history.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["tycho_brahe_telescope_chronology_error"]
    }


def arch_18_keplers_first_law_elliptical_orbits(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "When German mathematician Johannes Kepler analyzed Tycho Brahe's precise observational data of Mars, "
        "he abandoned the ancient Greek belief in perfect circular orbits.\n\n"
        "What does **Kepler's First Law of Planetary Motion** state about planetary orbits?"
    )
    correct = "All planets move in elliptical orbits, with the Sun situated at one of the two foci."
    options = [
        correct,
        "All planets move in perfect circles with Earth at the exact geometric center.",
        "All planets travel in straight zig-zag lines bounced off magnetic nebulae.",
        "Planets travel along triangular tracks around the constellation Orion."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: State Kepler's First Law (The Law of Ellipses):\n"
        "Planetary orbits are not perfect circles.\n"
        "Step 2: Geometry:\n"
        "An ellipse has two foci. The Sun sits at one focus, and the other focus is empty space."
    )
    rx_e = rng.choice([68, 70, 72])
    spec = {
        "kind": "inline_svg",
        "svg": f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 160" width="100%" height="130"><ellipse cx="150" cy="80" rx="{rx_e}" ry="50" fill="none" stroke="#38bdf8" stroke-width="2"/><circle cx="110" cy="80" r="14" fill="#f59e0b"/><text x="110" y="85" text-anchor="middle" fill="#ffffff" font-size="8">Sun</text><circle cx="190" cy="80" r="3" fill="#94a3b8"/><text x="190" y="70" text-anchor="middle" fill="#94a3b8" font-size="8">Focus 2</text><circle cx="218" cy="80" r="6" fill="#ef4444"/><text x="218" y="100" text-anchor="middle" fill="#ef4444" font-size="8">Planet</text><text x="150" y="20" text-anchor="middle" fill="#0f172a" font-size="11" font-weight="bold">Kepler\'s First Law: Elliptical Orbit</text></svg>',
        "diagram_role": "context"
    }
    return {
        "id": f"ns7_astro_18_{rng.randint(100000, 999999)}",
        "subskill": "18_keplers_first_law_elliptical_orbits",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "diagram_spec": spec,
        "hints": {
            "tier_1": "What oval geometric shape replaces a circle?",
            "tier_2": "An ellipse, with the Sun at one focus.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["keplers_first_law_shape_error"]
    }


def arch_19_keplers_second_law_orbital_speeds_perihelion_aphelion(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "According to **Kepler's Second Law** (The Law of Equal Areas in Equal Times), a line connecting a planet "
        "to the Sun sweeps out equal areas in equal intervals of time.\n\n"
        "How does a planet's orbital speed change as it travels between perihelion (closest to Sun) and aphelion (farthest from Sun)?"
    )
    correct = "The planet moves fastest when closest to the Sun (perihelion) and slowest when farthest from the Sun (aphelion)."
    options = [
        correct,
        "The planet maintains an identical constant speed at every point along its orbit.",
        "The planet moves slowest at perihelion and fastest at aphelion.",
        "The planet stops moving completely whenever it is closest to the Sun."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Understand Kepler's Second Law:\n"
        "To sweep out equal triangular areas in equal time intervals, the orbital arc must be longer when the radius is short.\n"
        "Step 2: Speed conclusion:\n"
        "Planets accelerate to their highest speed at perihelion (strongest gravitational pull) and slow down to their lowest speed at aphelion."
    )
    return {
        "id": f"ns7_astro_19_{rng.randint(100000, 999999)}",
        "subskill": "19_keplers_second_law_orbital_speeds_perihelion_aphelion",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Does gravity pull harder when you are closer or farther?",
            "tier_2": "Fastest when closest (perihelion), slowest when farthest (aphelion).",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["keplers_second_law_orbital_speed_inversion"]
    }


def arch_20_keplers_third_law_orbital_period_distance_ratio(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "**Kepler's Third Law** (The Harmonic Law) establishes a mathematical relationship between a planet's distance from the Sun "
        "and the time it takes to complete one orbit (period T).\n\n"
        "What fundamental relationship does this law prove about the planets in our solar system?"
    )
    correct = "Planets farther from the Sun take significantly longer to complete an orbit than planets closer to the Sun (T² is proportional to r³)."
    options = [
        correct,
        "All planets take exactly 365 days to orbit the Sun regardless of distance.",
        "Planets farther from the Sun travel faster and complete orbits in fewer days than inner planets.",
        "The size of a planet determines its orbit time, while distance has zero effect."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Kepler's Third Law formulation:\n"
        "T² = a³ (where T is orbital period in years, and a is semi-major axis in AU).\n"
        "Step 2: Application:\n"
        "Mercury (closest) orbits in 88 days; Earth takes 1 year; Neptune (farthest) takes 165 years. Distant planets have both longer paths and slower orbital speeds."
    )
    return {
        "id": f"ns7_astro_20_{rng.randint(100000, 999999)}",
        "subskill": "20_keplers_third_law_orbital_period_distance_ratio",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Do outer planets like Neptune take longer to orbit than inner planets like Earth?",
            "tier_2": "Greater distance means much longer orbital period.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["keplers_third_law_distance_period_fallacy"]
    }


def arch_21_invention_of_optical_telescope_hans_lippershey(rng: random.Random) -> Dict[str, Any]:
    year = "1608"
    prompt = (
        f"In {year}, Dutch spectacle-maker **Hans Lippershey** filed a patent for a device consisting of two glass lenses in a tube "
        "that made distant objects appear closer.\n\n"
        "What was this revolutionary scientific instrument called?"
    )
    correct = "The refracting telescope (spyglass)."
    options = [
        correct,
        "The electron microscope.",
        "The magnetic compass.",
        "The mercury barometer."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Historical origin of telescope:\n"
        "Hans Lippershey assembled convex and concave glass lenses in a tube in 1608 in the Netherlands.\n"
        "Step 2: Instrument classification:\n"
        "It was the first operational optical refracting telescope."
    )
    return {
        "id": f"ns7_astro_21_{rng.randint(100000, 999999)}",
        "subskill": "21_invention_of_optical_telescope_hans_lippershey",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Which instrument uses lenses to make distant stars and ships look closer?",
            "tier_2": "The telescope (refracting).",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["telescope_invention_chronology_error"]
    }


def arch_22_galileo_galilei_systematic_telescopic_observations(rng: random.Random) -> Dict[str, Any]:
    year = "1609"
    prompt = (
        f"In {year}, the Italian scientist **Galileo Galilei** built his own improved 20x telescope.\n\n"
        "What made Galileo's work historically unprecedented compared to earlier lens grinders?"
    )
    correct = "He was the first person to turn the telescope systematically toward the night sky, methodically recording and publishing telescopic astronomical observations."
    options = [
        correct,
        "He used the telescope exclusively to spy on trading ships entering Venice harbour.",
        "He dismantled his telescope to manufacture eyeglasses for kings.",
        "He claimed the telescope was a demonic illusion and banned anyone from looking through it."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Galileo's contribution:\n"
        "While Galileo did not invent the lens or first spyglass, in late 1609 he improved lens grinding and pointed his telescope celestial.\n"
        "Step 2: Publishing the results:\n"
        "In 1610, he published *Sidereus Nuncius* (The Starry Messenger), transforming human understanding of the heavens."
    )
    return {
        "id": f"ns7_astro_22_{rng.randint(100000, 999999)}",
        "subskill": "22_galileo_galilei_systematic_telescopic_observations",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Did Galileo point the telescope at the sky or just use it on land?",
            "tier_2": "First to systematically observe and publish celestial telescopic discoveries.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["galileo_invented_telescope_myth"]
    }


def arch_23_galilean_moons_of_jupiter_revolution(rng: random.Random) -> Dict[str, Any]:
    moons = ["Io", "Europa", "Ganymede", "Callisto"]
    m_choice = rng.choice(moons)
    prompt = (
        f"In January 1610, Galileo observed four small points of light ({m_choice} and three others) "
        "moving back and forth alongside Jupiter night after night.\n\n"
        "Why was the discovery of Jupiter's four large moons a catastrophic blow to the Geocentric model?"
    )
    correct = "It proved conclusively that celestial bodies could orbit something other than Earth, shattering the claim that everything revolved around Earth."
    options = [
        correct,
        "It proved that Jupiter was made entirely of melted gold and silver.",
        "It showed that the solar system had ceased expanding.",
        "It proved that the Moon had separated from Jupiter during a collision."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Geocentric dogmatic claim:\n"
        "The Aristotelian-Ptolemaic dogma claimed that Earth was the sole centre of all orbital motion in the universe.\n"
        "Step 2: Galileo's evidence:\n"
        "The four Galilean moons clearly revolved around Jupiter, proving Earth was NOT the unique centre of celestial motion."
    )
    return {
        "id": f"ns7_astro_23_{rng.randint(100000, 999999)}",
        "subskill": "23_galilean_moons_of_jupiter_revolution",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "If moons orbit Jupiter, does everything have to orbit Earth?",
            "tier_2": "Proved objects can orbit bodies other than Earth.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["galilean_moons_geocentric_refutation"]
    }


def arch_24_phases_of_venus_proving_heliocentrism(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Using his telescope, Galileo observed that **Venus goes through a complete cycle of phases** "
        "(crescent, gibbous, and full), accompanied by dramatic changes in apparent size.\n\n"
        "Why was observing a gibbous and full phase of Venus impossible under the Ptolemaic Geocentric model?"
    )
    correct = "Under Ptolemy's model, Venus stayed between Earth and the Sun, so it could only show crescents; showing a full set of phases proves Venus orbits the Sun."
    options = [
        correct,
        "Under Ptolemy's model, Venus was believed to be a square box with no reflective surface.",
        "Under Ptolemy's model, Venus had to be permanently invisible during daytime.",
        "Under Ptolemy's model, the Sun was thought to revolve inside Earth's core."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Geocentric prediction for Venus:\n"
        "In the Ptolemaic system, Venus's epicycle was pinned to a line between Earth and Sun. Observers could never see more than a crescent phase.\n"
        "Step 2: Galileo's observation:\n"
        "Seeing gibbous and nearly full phases meant Venus passed behind the Sun from Earth's perspective, proving Venus orbits the Sun (heliocentrism)."
    )
    return {
        "id": f"ns7_astro_24_{rng.randint(100000, 999999)}",
        "subskill": "24_phases_of_venus_proving_heliocentrism",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "If Venus shows full and gibbous phases, must it travel behind the Sun?",
            "tier_2": "Yes, proving Venus orbits the Sun directly.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["phases_of_venus_heliocentric_proof"]
    }


def arch_25_lunar_craters_and_imperfection_of_celestial_bodies(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Aristotelian doctrine taught that all celestial bodies above Earth were unblemished, perfect, smooth crystalline spheres.\n\n"
        "What did Galileo discover when he examined the surface of the Moon through his telescope?"
    )
    correct = "The Moon was rough, mountainous, covered in impact craters, and geologically imperfect, just like the rocky surface of Earth."
    options = [
        correct,
        "The Moon was made of pure translucent green glass with completely flat polished plains.",
        "The Moon was inhabited by cities of alien beings farming lunar wheat.",
        "The Moon was a burning star that extinguished itself every morning."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Aristotelian belief:\n"
        "The heavens were corrupt-free, perfect, and smooth.\n"
        "Step 2: Galileo's revelation:\n"
        "Galileo saw shadows shifting across lunar mountains, valleys, and craters, proving the Moon was a rugged, imperfect rocky world sharing physical properties with Earth."
    )
    return {
        "id": f"ns7_astro_25_{rng.randint(100000, 999999)}",
        "subskill": "25_lunar_craters_and_imperfection_of_celestial_bodies",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Did Galileo find a smooth glass ball or rugged mountains and craters?",
            "tier_2": "Craters, valleys, and mountains like Earth.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["crystalline_sphere_dogma_error"]
    }
