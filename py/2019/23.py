class IntCode:

    def __init__(self, obj_id, init_state):
        self.id = obj_id
        self.init_cond = init_state
        self.state = self.init_cond.copy()

        self.op_param_count = {
            1: 3,
            2: 3,
            3: 1,
            4: 1,
            5: 2,
            6: 2,
            7: 3,
            8: 3,
            9: 1,
            99: 0,
        }
        self.op_param_modal = {
            1: 2,
            2: 2,
            3: 0,
            4: 1,
            5: 2,
            6: 2,
            7: 2,
            8: 2,
            9: 1,
            99: 0,
        }

        self.pos = 0
        self.input_pos = 0
        self.relative_base = 0

        self.auto_inputs = []
        self.outputs = []

        self.cmd_count = 0
        self.halted = False
        self.awaiting_input = False
        self.input_op = None

    def get_addr(self, addr):
        if addr >= len(self.state):
            return 0
        return self.state[addr]

    def set_addr(self, addr, val):
        while addr >= len(self.state) - 1:
            self.state.append(0)
        self.state[addr] = val

    def run_op(self):
        if self.awaiting_input:
            return False

        full_op = self.state[self.pos]
        op = full_op % 100
        params = self.state[self.pos+1:self.pos+self.op_param_count[op]+1]
        for i in range(self.op_param_count[op]):
            mode = (full_op // [100, 1000, 10000][i]) % 10
            if i < self.op_param_modal[op]:
                if mode == 0:
                    params[i] = self.get_addr(params[i])
                elif mode == 2:
                    params[i] = self.get_addr(self.relative_base + params[i])
            elif mode == 2:
                params[i] = self.relative_base + params[i]

        self.cmd_count += 1

        if op == 1:
            self.set_addr(params[2], params[0] + params[1])
        elif op == 2:
            self.set_addr(params[2], params[0] * params[1])
        elif op == 3:
            if self.input_pos > len(self.auto_inputs) - 1:
                self.awaiting_input = True
                self.input_op = params[0]
                return False
            self.set_addr(params[0], self.auto_inputs[self.input_pos])
            self.input_pos += 1
        elif op == 4:
            self.outputs.append(params[0])
        elif op == 5:
            if params[0] != 0:
                self.pos = params[1] - 3
        elif op == 6:
            if params[0] == 0:
                self.pos = params[1] - 3
        elif op == 7:
            self.set_addr(params[2], 1 if params[0] < params[1] else 0)
        elif op == 8:
            self.set_addr(params[2], 1 if params[0] == params[1] else 0)
        elif op == 9:
            self.relative_base += params[0]
        elif op == 99:
            self.halted = True
            return False

        self.pos += self.op_param_count[op] + 1

        return True

    def add_input(self, in_val):
        self.auto_inputs.append(in_val)
        if self.awaiting_input:
            self.set_addr(self.input_op, self.auto_inputs[self.input_pos])
            self.input_pos += 1
            self.pos += 2
            self.awaiting_input = False
            self.input_op = None

    def run_until_input_or_halt(self):
        while not self.awaiting_input and not self.halted:
            self.run_op()

    def run_until_output_or_halt(self):
        outs = len(self.outputs)
        while len(self.outputs) == outs and not self.halted:
            self.run_op()

    def run_until_io_or_halt(self):
        outs = len(self.outputs)
        while len(self.outputs) == outs and not self.awaiting_input and not self.halted:
            self.run_op()

    def run_until_halt(self):
        while not self.halted:
            self.run_op()

    def reset_state(self):
        self.state = self.init_cond.copy()

        self.pos = 0
        self.input_pos = 0
        self.relative_base = 0

        self.auto_inputs = []
        self.outputs = []

        self.cmd_count = 0
        self.halted = False
        self.awaiting_input = False
        self.input_op = None


class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read()
            self.init_cond = list(map(int, self.input.split(',')))
        self.machines = []
        for i in range(50):
            machine = IntCode(f'NIC_{i}', self.init_cond)
            machine.add_input(i)
            self.machines.append(machine)

    def part1(self):
        for i in range(50):
            self.machines[i].reset_state()
            self.machines[i].add_input(i)
        while True:
            packets_to_process = []
            for i in range(50):
                m = self.machines[i]
                m.outputs = []
                m.run_until_input_or_halt()
                for j in range(int(len(m.outputs) / 3)):
                    p = tuple(m.outputs[j*3:j*3 + 3])
                    packets_to_process.append(p)
                    # print(f'Machine {i} sending packet {p}')
                    if p[0] == 255:
                        # print(p[2])
                        return p[2]

            for i in range(50):
                m = self.machines[i]
                packets_for_this_machine = []
                for p in packets_to_process:
                    if p[0] == i:
                        packets_for_this_machine.append(p)
                if len(packets_for_this_machine) == 0:
                    m.add_input(-1)
                for p in packets_for_this_machine:
                    # print(f'Machine {i} receiving packet {p}')
                    packets_to_process.remove(p)
                    m.add_input(p[1])
                    m.add_input(p[2])
            # print()

    def part2(self):
        for i in range(50):
            self.machines[i].reset_state()
            self.machines[i].add_input(i)
        nat_in = None
        nat_out_y = set()
        while True:
            packets_to_process = []
            for i in range(50):
                m = self.machines[i]
                m.outputs = []
                m.run_until_input_or_halt()
                for j in range(int(len(m.outputs) / 3)):
                    p = tuple(m.outputs[j*3:j*3 + 3])
                    packets_to_process.append(p)
                    # print(f'Machine {i} sending packet {p}')
                    if p[0] == 255:
                        nat_in = p

            if len(packets_to_process) == 0 and nat_in is not None:
                self.machines[0].add_input(nat_in[1])
                self.machines[0].add_input(nat_in[2])
                if nat_in[2] in nat_out_y:
                    return nat_in[2]
                else:
                    nat_out_y.add(nat_in[2])

            for i in range(50):
                m = self.machines[i]
                packets_for_this_machine = []
                for p in packets_to_process:
                    if p[0] == i:
                        packets_for_this_machine.append(p)
                if len(packets_for_this_machine) == 0:
                    m.add_input(-1)
                for p in packets_for_this_machine:
                    # print(f'Machine {i} receiving packet {p}')
                    packets_to_process.remove(p)
                    m.add_input(p[1])
                    m.add_input(p[2])
            # print()
