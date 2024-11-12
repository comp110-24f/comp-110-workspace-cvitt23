"""CQO4 coordinates"""

__author__ = "730677548"


def get_coords(xs: str, ys: str) -> None:
    len_xs = len(xs)
    len_ys = len(ys)

    i = 0
    while i < len_xs:
        j = 0
        while j < len_ys:
            print(f"({xs[i]},{ys[j]})")
            j += 1
        i += 1
