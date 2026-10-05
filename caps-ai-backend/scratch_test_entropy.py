import sys
import os
sys.path.insert(0, os.path.abspath("caps-ai-backend"))

def _get_q_list(res):
    if isinstance(res, dict) and "questions" in res:
        return res["questions"]
    if isinstance(res, list):
        return res
    return [res]

def test_entropy():
    # 1. Life Sciences Dihybrid
    from app.utils.life_sciences.dihybrid_pedigree_generator import generate as gen_dihybrid
    qs_dihybrid = [_get_q_list(gen_dihybrid(seed=s))[0]["prompt"] for s in range(100)]
    unique_dihybrid = len(set(qs_dihybrid))
    print(f"Dihybrid entropy: {unique_dihybrid}/100")

    # 2. Momentum & Impulse
    from app.utils.grade12_physical_sciences.momentum_impulse_generator import generate as gen_momentum
    qs_momentum = [_get_q_list(gen_momentum(seed=s))[0]["prompt"] for s in range(100)]
    unique_momentum = len(set(qs_momentum))
    print(f"Momentum entropy: {unique_momentum}/100")

    # 3. Math Distance Drill
    from app.utils.grade10_mathematics.term_2.analytical_geometry_generator import generate as gen_analytical
    qs_dist = [_get_q_list(gen_analytical(subskill="distance_formula", seed=s))[0]["prompt"] for s in range(100)]
    unique_dist = len(set(qs_dist))
    print(f"Math Distance entropy: {unique_dist}/100")

if __name__ == "__main__":
    test_entropy()
