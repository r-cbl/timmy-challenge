from automata.pda.dpda import DPDA

dpda_mountain = DPDA(
    states={'q0', 'q1', 'q2', 'q3'},
    input_symbols={'/', 'b'},
    stack_symbols={'0', '1'},
    transitions={
        'q0': {
            '/': {'0': ('q1', ('1', '0'))}  # push '1' to stack
        },
        'q1': {
            '/': {'1': ('q1', ('1', '1'))},  # push '1' to stack
            'b': {'1': ('q2', '')}  # pop from stack
        },
        'q2': {
            'b': {'1': ('q2', '')},  # pop from stack
            '/': {'1': ('q1', ('1', '1'))},  # push '1' to stack
            '': {'0': ('q3', ('0',))},  # no change to stack
        },
        'q3': {
            '/': {'0': ('q1', ('1', '0'))},
        }
    },
    initial_state='q0',
    initial_stack_symbol='0',
    final_states={'q3'},
    acceptance_mode='final_state'
)

dpda_mountain_tunnel = DPDA(
    states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8'},
    input_symbols={'/', 'b', '<', '>'},
    stack_symbols={'0', '1', '2'},
    transitions={
        'q0': {
            '/': {'0': ('q1', ('1', '0'))}  # push '1' to stack
        },
        'q1': {
            '/': {'1': ('q1', ('1', '1'))},  # push '1' to stack
            '>': {'1': ('q2', ('2', '1'))}  # push '2' and move on
        },
        'q2': {
            '/': {'2': ('q3', ('1', '2'))},
            '>': {'1': ('q2', ('2', '1'))},
        },
        'q3': {
            '/': {'1': ('q3', ('1', '1'))},
            'b': {'1': ('q4', '')},
            '>': {'1': ('q2', ('2', '1'))},
        },
        'q4': {
            'b': {'1': ('q4', '')},
            '<': {'2': ('q5', '')}
        },
        'q5': {
            '<': {'2': ('q5', '')},
            'b': {'1': ('q6', '')},
        },
        'q6': {
            'b': {'1': ('q6', '')},
            '/': {'1': ('q1', ('1', '1'))},
            '<': {'2': ('q7', '')},
            '': {'0': ('q8', ('0',))},
        },
        'q7': {
            'b': {'1': ('q6', '')},
        },
        'q8': {
            '/': {'0': ('q1', ('1', '0'))},
        },
    },
    initial_state='q0',
    initial_stack_symbol='0',
    final_states={'q8'},
    acceptance_mode='final_state'
)
