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
            99: 0,
        }

        self.pos = 0
        self.input_pos = 0
        self.auto_inputs = None
        self.outputs = []

        self.halted = False

    def run_op(self):
        full_op = self.state[self.pos]
        op = full_op % 100
        params = [self.state[self.pos+i+1] for i in range(self.op_param_count[op])]
        for i in range(self.op_param_modal[op]):
            params[i] = params[i] if (full_op // [100, 1000, 10000][i]) % 10 == 1 else self.state[params[i]]

        if op == 1:
            self.state[params[2]] = params[0] + params[1]
        elif op == 2:
            self.state[params[2]] = params[0] * params[1]
        elif op == 3:
            self.state[params[0]] = self.auto_inputs[self.input_pos]
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
            self.state[params[2]] = 1 if params[0] < params[1] else 0
        elif op == 8:
            self.state[params[2]] = 1 if params[0] == params[1] else 0
        elif op == 99:
            self.halted = True
            return False

        self.pos += self.op_param_count[op] + 1

        return True

    def reset_state(self):
        self.state = self.init_cond.copy()
        self.pos = 0
        self.input_pos = 0
        self.outputs = []
        self.halted = False
        self.auto_inputs = None


class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read()
            self.init_cond = list(map(int, self.input.split(',')))
        self.amp = IntCode(0, self.init_cond)
        self.amps = [IntCode(i, self.init_cond) for i in range(5)]

    def part1(self):
        self.amp.reset_state()

        max_val = 0

        nums = set(range(5))
        for a in nums:
            self.amp.reset_state()
            self.amp.auto_inputs = [a, 0]
            run = True
            while run:
                run = self.amp.run_op()
            output_a = self.amp.outputs[-1]

            for b in nums:
                if b == a:
                    continue
                self.amp.reset_state()
                self.amp.auto_inputs = [b, output_a]
                run = True
                while run:
                    run = self.amp.run_op()
                output_b = self.amp.outputs[-1]

                for c in nums:
                    if c == a or c == b:
                        continue
                    self.amp.reset_state()
                    self.amp.auto_inputs = [c, output_b]
                    run = True
                    while run:
                        run = self.amp.run_op()
                    output_c = self.amp.outputs[-1]

                    for d in nums:
                        if d == a or d == b or d == c:
                            continue
                        self.amp.reset_state()
                        self.amp.auto_inputs = [d, output_c]
                        run = True
                        while run:
                            run = self.amp.run_op()
                        output_d = self.amp.outputs[-1]

                        for e in nums:
                            if e == a or e == b or e == c or e == d:
                                continue
                            self.amp.reset_state()
                            self.amp.auto_inputs = [e, output_d]
                            run = True
                            while run:
                                run = self.amp.run_op()
                            output_e = self.amp.outputs[-1]

                            if output_e > max_val:
                                max_val = output_e

        return max_val

    def part2(self):
        for amp in self.amps:
            amp.reset_state()

        max_val = 0

        nums = set(range(5, 10))
        for a in nums:
            for b in nums:
                if b == a:
                    continue
                for c in nums:
                    if c == a or c == b:
                        continue
                    for d in nums:
                        if d == a or d == b or d == c:
                            continue
                        for e in nums:
                            if e == a or e == b or e == c or e == d:
                                continue
                            for amp in self.amps:
                                amp.reset_state()
                            self.amps[0].auto_inputs = [a, 0]
                            self.amps[1].auto_inputs = [b]
                            self.amps[2].auto_inputs = [c]
                            self.amps[3].auto_inputs = [d]
                            self.amps[4].auto_inputs = [e]

                            i_amp = 0
                            while True:
                                outs = len(self.amps[i_amp].outputs)
                                self.amps[i_amp].run_op()

                                if len(self.amps[i_amp].outputs) > outs:
                                    next_in = self.amps[i_amp].outputs[-1]
                                    i_amp = (i_amp + 1) % 5
                                    self.amps[i_amp].auto_inputs.append(next_in)

                                if self.amps[i_amp].halted:
                                    if i_amp < 4:
                                        i_amp += 1
                                    else:
                                        output_e = self.amps[4].outputs[-1]

                                        if output_e > max_val:
                                            max_val = output_e

                                        break

        return max_val
