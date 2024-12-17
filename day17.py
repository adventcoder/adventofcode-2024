from aoc import get_input, submit

def parse(input):
    sections = input.split("\n\n")
    registers = [0] * 3
    for i, line in enumerate(sections[0].splitlines()):
        registers[i] = int(line.removeprefix(f'Register ' + 'ABC'[i] + ': '))
    program = list(map(int, sections[1].removeprefix('Program: ').split(',')))
    return registers, program

def display(program):    
    def combo(operand):
        return str(operand) if operand < 4 else 'ABC'[operand - 4]
    ip = 0
    while ip < len(program):
        opcode, operand = program[ip : ip + 2]
        match opcode:
            case 0: # adv
                print('A >>= ' + combo(operand))
            case 1: # bxl
                print('B ^= ' + str(operand))
            case 2: # bst
                print('B = ' + combo(operand) + '&7')
            case 3: # jnz
                print('if A != 0: ip = ' + str(operand))
            case 4: # bxc
                print('B ^= C')
            case 5: # out
                print('out ' + combo(operand) + '&7')
            case 6: # bdv
                print('B = A >> ' + combo(operand))
            case 7: # cdv
                print('C = A >> ' + combo(operand))
        ip += 2


def exec(program, A, B, C):
    reg = [A, B, C]
    def combo(operand):
        return operand if operand < 4 else reg[operand - 4]
    out = []
    ip = 0
    while ip < len(program):
        opcode, operand = program[ip : ip + 2]
        match opcode:
            case 0: # adv
                reg[0] >>= combo(operand)
            case 1: # bxl
                reg[1] ^= operand
            case 2: # bst
                reg[1] = combo(operand) & 7
            case 3: # jnz
                if reg[0] != 0:
                    ip = operand
                    continue
            case 4: # bxc
                reg[1] ^= reg[2]
            case 5: # out
                out.append(combo(operand) & 7)
            case 6: # bdv
                reg[1] = reg[0] >> combo(operand)
            case 7: # cdv
                reg[2] = reg[0] >> combo(operand)
        ip += 2
    return out

def find_A(program, B, C):
    #
    # Given an input with 3-bit digits ABCD, the program produces the output as follows:
    #
    # input = A
    # output = [f(A)]
    #
    # input = AB
    # output = [f(AB), f(A)]
    #
    # input = ABC
    # output = [f(ABC), f(AB), f(A)]
    #
    # That allows us to search one digit of the input at a time to match the desired output.
    #
    def recur(n):
        if n == 0:
            yield 0
        else:
            for A in recur(n - 1):
                for d in range(8):
                    new_A = (A << 3) | d
                    if exec(program, new_A, B, C)[0] == program[-n]:
                        yield new_A
    return next(recur(len(program)))

(A, B, C), program = parse(get_input(17))
# display(program)
submit(','.join(map(str, exec(program, A, B, C))))
submit(find_A(program, B, C))
