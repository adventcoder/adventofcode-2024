from aoc import get_input, submit
from utils import Vector2D, ints

def solve(A, B, P):
    # n*Ax + m*Bx = Px
    # n*Ay + m*By = Py
    #
    # n = (Px*By - Py*Bx)/(Ax*By - Ay*Bx)
    # m = (Px*Ay - Py*Ax)/(Bx*Ay - By*Ax)
    #
    d = A.cross(B)
    if P.cross(B) % d != 0 or P.cross(A) % d != 0:
        return None
    n = P.cross(B) // d
    m = A.cross(P) // d
    return 3*n + m

input = get_input(13)
total_tokens1 = 0
total_tokens2 = 0
for section in input.split('\n\n'):
    A, B, P = [Vector2D(*ints(line)) for line in section.splitlines()]
    if tokens1 := solve(A, B, P):
        total_tokens1 += tokens1
    if tokens2 := solve(A, B, P + Vector2D(10000000000000, 10000000000000)):
        total_tokens2 += tokens2
submit(total_tokens1)
submit(total_tokens2)
