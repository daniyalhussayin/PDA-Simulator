# pda_simulator.py

def simulate_anbn(input_str):
    stack = ['Z']
    steps = []
    state = 'q0'
    i = 0

    while i < len(input_str):
        char = input_str[i]
        top = stack[-1]

        if state == 'q0':
            if char == 'a':
                stack.append('a')
                steps.append(f"q0 | a | {top} | {''.join(stack)} | Push a")
                i += 1
            elif char == 'b':
                state = 'q1'
                steps.append(f"q0→q1 | ε | {top} | {''.join(stack)} | Switch to pop mode")
            else:
                return False, steps, state, stack
        elif state == 'q1':
            if char == 'b' and stack[-1] == 'a':
                stack.pop()
                steps.append(f"q1 | b | {top} | {''.join(stack)} | Pop a")
                i += 1
            else:
                return False, steps, state, stack

    if state == 'q0':
        state = 'q1'
        steps.append(f"q0→q1 | ε | {stack[-1]} | {''.join(stack)} | Switch to pop mode")

    if state == 'q1' and stack == ['Z']:
        return True, steps, 'q_accept', stack
    return False, steps, state, stack


def simulate_palindrome_wcwr(input_str):
    stack = ['Z']
    steps = []
    state = 'q0'
    i = 0

    while i < len(input_str):
        char = input_str[i]
        if state == 'q0':
            if char in ['a', 'b']:
                stack.append(char)
                steps.append(f"q0 | {char} | {stack[-2]} | {''.join(stack)} | Push {char}")
                i += 1
            elif char == 'c':
                state = 'q1'
                steps.append(f"q0→q1 | c | {stack[-1]} | {''.join(stack)} | Switch to compare mode")
                i += 1
            else:
                return False, steps, state, stack
        elif state == 'q1':
            if char in ['a', 'b']:
                if stack[-1] == char:
                    steps.append(f"q1 | {char} | {stack[-1]} | {''.join(stack[:-1])} | Pop {char}")
                    stack.pop()
                    i += 1
                else:
                    return False, steps, state, stack
            else:
                return False, steps, state, stack

    if state == 'q1' and stack == ['Z']:
        return True, steps, 'q_accept', stack
    return False, steps, state, stack