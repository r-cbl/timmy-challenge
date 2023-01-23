from automata.pda.dpda import DPDA


class MountainHelper:
    dpda_mountain = 0
    dpda_mountain_tunnel = 0

    def __init__(self):
        self.dpda_mountain1 = None
        self.create_automatas()

    def validate_mountain(self, characters):
        return self.dpda_mountain.accepts_input(characters)

    def validate_tunnel_mountain(self, characters):
        return self.dpda_mountain_tunnel.accepts_input(characters)

    def validate_fix_not_mountain(self, characters):
        if not self.validate_mountain(characters):
            return self.fix_mountain(characters)

        else:
            return 0

    @staticmethod
    def fix_mountain(not_mountain):
        heap = init_flank = start_flag = 0
        for character in not_mountain:
            match character:
                case '/':
                    heap += 1
                    if start_flag == 0:
                        start_flag = 1

                case '\\':
                    if start_flag == 0:
                        init_flank += 1
                    else:
                        heap -= 1

        return init_flank + abs(heap)

    def create_automatas(self):
        self.dpda_mountain = DPDA(
            states={'q0', 'q1', 'q2', 'q3'},
            input_symbols={'/', '\\', ' '},
            stack_symbols={'0', '1'},
            transitions={
                'q0': {
                    '/': {'0': ('q1', ('1', '0'))}  # push '1' to stack
                },
                'q1': {
                    '/': {'1': ('q1', ('1', '1'))},  # push '1' to stack
                    '\\': {'1': ('q2', '')}  # pop from stack
                },
                'q2': {
                    '\\': {'1': ('q2', '')},  # pop from stack
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
            acceptance_mode='both'
        )

        self.dpda_mountain_tunnel = DPDA(
            states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8'},
            input_symbols={'/', '\\', '<', '>'},
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
                    '\\': {'1': ('q4', '')},
                    '>': {'1': ('q2', ('2', '1'))},
                },
                'q4': {
                    '\\': {'1': ('q4', '')},
                    '<': {'2': ('q5', '')}
                },
                'q5': {
                    '<': {'2': ('q5', '')},
                    '\\': {'1': ('q6', '')},
                },
                'q6': {
                    '\\': {'1': ('q6', '')},
                    '/': {'1': ('q1', ('1', '1'))},
                    '<': {'2': ('q7', '')},
                    '': {'0': ('q8', ('0',))},
                },
                'q7': {
                    '\\': {'1': ('q6', '')},
                },
                'q8': {
                    '/': {'0': ('q1', ('1', '0'))},
                },
            },
            initial_state='q0',
            initial_stack_symbol='0',
            final_states={'q8'},
            acceptance_mode='both'
        )


