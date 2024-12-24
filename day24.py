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

#TODO: automate this...

swaps = []

def swap(a, b):
    swaps.append(a)
    swaps.append(b)
    gates[a], gates[b] = gates[b], gates[a]

swap('jst', 'z05')
swap('gdf', 'mcm')
swap('dnt', 'z15')
swap('gwc', 'z30')

def match_gate(in1, opname, in2):
    for out in gates:
        if gates[out] == [in1, opname, in2] or gates[out] == [in2, opname, in1]:
            return out
    raise ValueError(f'no {opname} gate attached to {in1}, {in2}')

def match_half_adder(in1, in2):
    sum_out = match_gate(in1, 'XOR', in2)
    carry_out = match_gate(in1, 'AND', in2)
    return sum_out, carry_out

def match_full_adder(in1, in2, carry_in):
    t, c1 = match_half_adder(in1, in2)
    sum_out, c2 = match_half_adder(t, carry_in)
    carry_out = match_gate(c1, 'OR', c2)
    return sum_out, carry_out

zout, carry = match_half_adder('x00', 'y00')
assert zout == 'z00'
for i in range(1, 45):
    zout, carry = match_full_adder('x%02d' % i, 'y%02d' % i, carry)
    assert zout == 'z%02d' % i
assert carry == 'z45'

# with open('inputs/day24.dot', 'w') as file:
#     print('digraph {', file=file)
#     for out in gates:
#         in1, opname, in2 = gates[out]
#         print(out, f'[label={opname}]', file=file)
#         print(in1, '->', out, f'[label={in1}]', file=file)
#         print(in2, '->', out, f'[label={in2}]', file=file)
#     for i in range(46):
#         zin = 'z%02d' % i
#         print(zin, '->', f'dummy{i}', f'[label={zin}]', file=file)
#     print('}', file=file)

submit(','.join(sorted(swaps)))
