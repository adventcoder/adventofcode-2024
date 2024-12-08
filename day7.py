from aoc import get_input, submit

ops = {
    '+': lambda x, y: x + y,
    '*': lambda x, y: x * y,
    '||': lambda x, y: int(str(x) + str(y))
}

inv_ops = {
    '+': lambda target, y: target - y,
    '*': lambda target, y: target // y if target % y == 0 else None,
    '||': lambda target, y: int(str(target).removesuffix(str(y))) if y != target and str(target).endswith(str(y)) else None
}

def parse(input):
    eqns = []
    for line in input.splitlines():
        lhs, rhs = line.split(':')
        eqns.append((int(lhs), list(map(int, rhs.split()))))
    return eqns

def solvable(target, xs, opnames):
    lower = [xs[0]]
    upper = [xs[0]]
    for x in xs[1:]:
        lower.append(min(ops[opname](lower[-1], x) for opname in opnames))
        upper.append(max(ops[opname](upper[-1], x) for opname in opnames))

    def recur(target, i):
        if not lower[i] <= target <= upper[i]:
            return False
        if i == 0:
            return xs[0] == target
        for opname in opnames:
            new_target = inv_ops[opname](target, xs[i])
            if new_target is not None and recur(new_target, i - 1):
                return True
        return False

    return recur(target, len(xs) - 1)

def total_calibration_result(eqns, opnames):
    return sum(target for target, xs in eqns if solvable(target, xs, opnames))

eqns = parse(get_input(7))
submit(total_calibration_result(eqns, ['+', '*']))
submit(total_calibration_result(eqns, ['+', '*', '||']))
