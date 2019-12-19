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

    def add_input(self, input):
        self.auto_inputs.append(input)
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
        self.machine = IntCode('drone', self.init_cond)

        self.grid = None

    def part1(self):
        beam = 0
        for y in range(50):
            for x in range(50):
                self.machine.reset_state()
                self.machine.auto_inputs = [x, y]
                self.machine.run_until_output_or_halt()
                out = self.machine.outputs[-1]
                if out == 1:
                    beam += 1
        return beam

    def part2(self):
        cols = {}
        rows = {}

        # Trace top of beam (max x, min y)
        y = 500
        x = 500
        while x <= 2000 and y <= 2000:
            self.machine.reset_state()
            self.machine.auto_inputs = [x, y]
            self.machine.run_until_output_or_halt()
            out = self.machine.outputs[-1]
            if out == 0:
                y += 1
            elif out == 1:
                col = cols.setdefault(x, [1_000, -1])
                col[0] = y if y < col[0] else col[0]
                row = rows.setdefault(y, [1_000, -1])
                row[1] = x if x > row[1] else row[1]
                x += 1

        # Trace bottom of beam (min x, max y)
        y = 500
        x = 500
        while x <= 2000 and y <= 2000:
            self.machine.reset_state()
            self.machine.auto_inputs = [x, y]
            self.machine.run_until_output_or_halt()
            out = self.machine.outputs[-1]
            if out == 0:
                x += 1
            elif out == 1:
                col = cols.setdefault(x, [1_000, -1])
                col[1] = y if y > col[1] else col[1]
                row = rows.setdefault(y, [1_000, -1])
                row[0] = x if x < row[0] else row[0]
                y += 1

        tl = (100_000, 100_000)
        for col in cols:
            if col > tl[0]:
                continue
            lims = cols[col]
            if lims[1] < 100:
                continue
            height = lims[1] - lims[0] + 1
            if height < 100:
                continue

            bl = (col, lims[1])
            tr = (col + 99, lims[1] - 99)
            if tr[0] in cols:
                if tr[1] >= cols[tr[0]][0]:
                    if lims[1] - 99 < tl[1]:
                        tl = (col, lims[1] - 99)

        for row in rows:
            if row > tl[1]:
                continue
            lims = rows[row]
            if lims[1] < 100:
                continue
            width = lims[1] - lims[0] + 1
            if width < 100:
                continue

            tr = (lims[1], row)
            bl = (lims[1] - 99, row + 99)
            if bl[1] in rows:
                if bl[0] >= rows[bl[1]][0]:
                    if lims[1] - 99 < tl[0]:
                        tl = (lims[1] - 99, row)

        return tl[0] * 10_000 + tl[1]
