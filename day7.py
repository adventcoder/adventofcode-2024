from aoc import get_input, submit

def parse(input):
    eqns = []
    for line in input.splitlines():
        lhs, rhs = line.split(':')
        eqns.append((int(lhs), list(map(int, rhs.split()))))
    return eqns

def add_inv(target, y): # x + y = target
    return target - y

def mul_inv(target, y): # x * y = target
    return target // y if target % y == 0 else None

def cat_inv(target, y):
    return mul_inv(target - y, 10**len(str(y)))

def solvable(target, xs, inv_ops):
    if len(xs) == 1:
        return xs[0] == target
    else:
        # if upper_bound(xs, ops) < target:
        #     return False
        return any(solvable(new_target, xs[:-1], inv_ops) for inv_op in inv_ops if (new_target := inv_op(target, xs[-1])) is not None)

def total_calibration_result(eqns, inv_ops):
    return sum(target for target, xs in eqns if solvable(target, xs, inv_ops))

eqns = parse(get_input(7))
# ops that produce a larger output come first to minimize branching
submit(total_calibration_result(eqns, [mul_inv, add_inv]))
submit(total_calibration_result(eqns, [cat_inv, mul_inv, add_inv]))
