import sys
import re
sys.path.insert(0, 'caps-ai-backend')
from app.services.generator_registry import generate_variant

topics = [
    ('Integers', '7'),
    ('Working with whole numbers', '7'),
    ('The decimal notation for fractions', '7'),
    ('Functions and relationships 1', '7'),
    ('Algebraic expressions 1', '7'),
    ('Integers', '9'),
    ('Geometry of straight lines', '9'),
    ('Area and perimeter of 2D shapes', '9'),
    ('Surface area volume and capacity of 3D objects', '9'),
]

rx_method = re.compile(
    r'(?i)\b(difference of (two )?squares|bodmas|pemdas|additive inverse|'
    r'multiplicative inverse|distributive (law|property)|'
    r'(using|use|by using|apply) the [a-z\- ]{0,30}(method|property|law|formula|rule))\b'
)
rx_fig = re.compile(
    r'(?i:\b(in the (given )?(figure|diagram)|given (figure|diagram)|shown (below|above)|'
    r'wireframe|icosahedron|dodecahedron|octahedron|tetrahedron|'
    r'(rectangular|triangular) prism|pyramid|cylinder|cone|(?<!celestial\s)sphere)\b)|'
    r'(?i:\b(triangle|quadrilateral|parallelogram|trapezium)\b)\s+[A-Z]{3,4}\b'
)
rx_bs = re.compile(r'\\\\[a-zA-Z]')
rx_quote = re.compile(r'\*\*\s*["\u201c]')

for topic, gr in topics:
    for seed in [42, 101, 777]:
        try:
            qs = generate_variant(topic=topic, grade=gr, subject='mathematics', seed=seed)
            for q in (qs if isinstance(qs, list) else [qs]):
                p = q.get('prompt') or q.get('question') or ''
                m = rx_method.search(p)
                if m:
                    print(f"METHOD [{gr} {topic} seed {seed}]: matched '{m.group()}' in '{p[:80]}...'")
                m_bs = rx_bs.search(str(q))
                if m_bs:
                    print(f"DOUBLE BS [{gr} {topic} seed {seed}]: matched '{m_bs.group()}'")
                m_q = rx_quote.search(p)
                if m_q:
                    print(f"BOLD QUOTE [{gr} {topic} seed {seed}]: matched in '{p[:80]}...'")
                if rx_fig.search(p) and not q.get('diagram_spec'):
                    print(f"FIG NO DIAG [{gr} {topic} seed {seed}]: in '{p[:80]}...'")
        except Exception as e:
            print(f"ERR [{gr} {topic}]: {e}")
