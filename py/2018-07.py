import bisect


class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().splitlines()

        self.steps = {}
        for line in self.input:
            post_step = self.steps.setdefault(line[36], Step(line[36]))
            pre_step = self.steps.setdefault(line[5], Step(line[5]))
            post_step.add_pre_req(pre_step)

        self.first_step = list(self.steps.values())[0]
        while self.first_step.pre_reqs:
            if self.first_step.pre_reqs:
                self.first_step = self.first_step.pre_reqs[0]

    def part1(self):
        steps_to_process = {self.first_step}
        ready_step_names = []
        order = []

        while steps_to_process:
            for s in steps_to_process:
                if (not s.pre_reqs or all([i.done for i in s.pre_reqs])) and s.name not in ready_step_names:
                    bisect.insort(ready_step_names, s.name)

            s = self.steps[ready_step_names[0]]

            order.append(s.name)
            s.done = True
            steps_to_process.remove(s)
            for s_to_add in s.followers:
                steps_to_process.add(s_to_add)
            ready_step_names.pop(0)

        return ''.join(order)

    def part2(self):
        for step in self.steps.values():
            step.done = False
            step.time_completed = 0

        steps_to_process = {self.first_step}
        ready_step_names = []

        t = 0
        update_ready_steps = True
        while steps_to_process:
            for s in steps_to_process:

                if (update_ready_steps and
                        all([i.done for i in s.pre_reqs])
                        and s.name not in ready_step_names):
                    bisect.insort(ready_step_names, s.name)

            update_ready_steps = False

            for i, s_name in enumerate(ready_step_names):
                if i >=5:
                    break

                s = self.steps[s_name]
                s.time_completed += 1

                if s.time_completed == s.time_required:
                    s.done = True
                    update_ready_steps = True
                    steps_to_process.remove(s)
                    for s_to_add in s.followers:
                        steps_to_process.add(s_to_add)

            ready_step_names = [i for i in ready_step_names if not self.steps[i].done]
            t += 1

        return t


class Step:

    def __init__(self, name):
        self.name = name
        self.pre_reqs = []
        self.followers = []

        self.time_required = ord(name) - 4
        self.time_completed = 0
        self.done = False

    def add_pre_req(self, step):
        self.pre_reqs.append(step)
        step.followers.append(self)
