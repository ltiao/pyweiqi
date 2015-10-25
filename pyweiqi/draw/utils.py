from itertools import (chain, permutations, product, repeat)
from six.moves import map


def xor(a, b):
    """
    Examples
    --------
    >>> xor(True, True)
    False

    >>> xor(True, False)
    True

    >>> xor(False, True)
    True

    >>> xor(False, False)
    False
    """
    return a != b


def hoshi_coords(start=3, size=19, include_sides=True, include_tengen=True):
    """
    Examples
    --------
    >>> sorted(hoshi_coords())
    [(3, 3), (3, 9), (3, 15), (9, 3), (9, 9), (9, 15), (15, 3), (15, 9), (15, 15)]

    >>> sorted(hoshi_coords(include_sides=False))
    [(3, 3), (3, 15), (9, 9), (15, 3), (15, 15)]

    >>> sorted(hoshi_coords(include_tengen=False))
    [(3, 3), (3, 9), (3, 15), (9, 3), (9, 15), (15, 3), (15, 9), (15, 15)]

    >>> sorted(hoshi_coords(include_sides=False, include_tengen=False))
    [(3, 3), (3, 15), (15, 3), (15, 15)]
    """
    end = size - start - 1
    mid = size // 2

    hoshi = list(product((start, end), repeat=2))

    if include_sides and include_tengen:
        return list(product((start, mid, end), repeat=2))

    if include_sides:
        hoshi.extend(list(chain(*map(permutations, product((mid,), [start, end])))))

    if include_tengen:
        hoshi.append(tuple(repeat(mid, times=2)))

    return hoshi
