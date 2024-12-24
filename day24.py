from aoc import get_input, submit

input = get_input(24)
sections = input.split('\n\n')

ops = {
    'AND': lambda a, b: a & b,
    'OR': lambda a, b: a | b,
    'XOR': lambda a, b: a ^ b
}

vals = {}
for line in sections[0].splitlines():
    out, s = line.split(': ')
    vals[out] = int(s)

gates = {}
for line in sections[1].splitlines():
    expr, out = line.split(' -> ')
    gates[out] = expr.split()

def eval(out):
    if out not in vals:
        a, opname, b = gates[out]
        vals[out] = ops[opname](eval(a), eval(b))
    return vals[out]

n = 0
for out in gates.keys():
    if out.startswith('z'):
        i = int(out[1:])
        n |= eval(out) << i
submit(n)

with open('inputs/day24.dot', 'w') as file:
    print('digraph {', file=file)
    for out, (in1, opname, in2) in gates.items():
        print(out, f'[label={opname}]', file=file)
        print(in1, '->', out, file=file)
        print(in2, '->', out, file=file)
        if out.startswith('z'):
            print(f'{out}x', f'[label={out}]', file=file)
            print(out, '->', f'{out}x', file=file)
    print('}', file=file)
