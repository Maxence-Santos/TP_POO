"""def f(d, t, x1, y1, x2, y2):
    dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    if t == 'R':
        c = dist * 1.0
    elif t == 'H':
        c = dist * 1.5
    elif t == 'S':
        c = dist * 2.0
    else:
        c = dist * 3.0
    print("cout:", c)
    return c

qualite.py:1:0: R0913: Too many arguments (6/5) (too-many-arguments)
qualite.py:1:0: R0917: Too many positional arguments (6/5) (too-many-positional-arguments)
qualite.py:1:6: W0613: Unused argument 'd' (unused-argument)"""

def cout_deplacement_propre(t,x1,y1,x2,y2):
    """Calcule le coût énergétique selon le terrain"""
    dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    if t == 'R':
        c = dist * 1.0
    elif t == 'H':
        c = dist * 1.5
    elif t == 'S':
        c = dist * 2.0
    else:
        c = dist * 3.0
    print("cout:", c)
    return c
