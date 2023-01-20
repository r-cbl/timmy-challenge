from automata.pda.npda import NPDA


npda_mountain = NPDA(
    states={'q0', 'q1', 'q2'},
    input_symbols={'/', '\\', ' '},
    stack_symbols={'A', 'B', '#'},
    transitions={
        'q0': {
            '': {
                '#': {('q2', '#')},  # no change to stack
            },
            '/': {
                '#': {('q0', ('A', '#'))},  # push 'A' to stack
                'A': {
                    ('q0', ('A', 'A')),  # push 'A' to stack
                    ('q1', ''),  # pop from stack
                },
                'B': {('q0', ('A', 'B'))},  # push 'A' to stack
            },
            '\\': {
                '#': {('q0', ('B', '#'))},  # push 'B' to stack
                'A': {('q0', ('B', 'A'))},  # push 'B' to stack
                'B': {
                    ('q0', ('B', 'B')),  # push 'B' to stack
                    ('q1', ''),  # pop from stack
                },
            },
        },
        'q1': {
            '': {'#': {('q2', '#')}},  # push '#' to (currently empty) stack
            ' ': {'#': {('q2', '#')}},  # push '#' to (currently empty) stack - end w one blank space
            '/': {'A': {('q1', '')}},  # pop from stack
            '\\': {'B': {('q1', '')}},  # pop from stack
        },
    },
    initial_state='q0',
    initial_stack_symbol='#',
    final_states={'q2'},
    acceptance_mode='both'
)

