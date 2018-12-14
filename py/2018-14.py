from collections import deque


class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input_raw = f.read()

        self.input = int(self.input_raw)

        self.recipes = [3, 7]

    def part1(self):
        elf_1 = 0
        elf_2 = 1

        while len(self.recipes) < self.input + 10:
            new_val = self.recipes[elf_1] + self.recipes[elf_2]

            if new_val >= 10:
                self.recipes.append(1)
                self.recipes.append(new_val % 10)
            else:
                self.recipes.append(new_val)

            elf_1 = (elf_1 + self.recipes[elf_1] + 1) % len(self.recipes)
            elf_2 = (elf_2 + self.recipes[elf_2] + 1) % len(self.recipes)

        return ''.join(str(n) for n in self.recipes[-10:])

    
    def part2(self):
        self.recipes = [3, 7]
        elf_1 = 0
        elf_2 = 1

        last_added = deque([-1]*(len(self.input_raw) - 1))
        check = deque([int(d) for d in self.input_raw])

        while True:
            new_val = self.recipes[elf_1] + self.recipes[elf_2]

            if new_val >= 10:
                self.recipes.append(1)
                last_added.append(1)
                if last_added == check:
                    break
                last_added.popleft()
                
                self.recipes.append(new_val % 10)
                last_added.append(new_val % 10)
            else:
                self.recipes.append(new_val)
                last_added.append(new_val)

            if last_added == check:
                break
            last_added.popleft()

            elf_1 = (elf_1 + self.recipes[elf_1] + 1) % len(self.recipes)
            elf_2 = (elf_2 + self.recipes[elf_2] + 1) % len(self.recipes)

        return len(self.recipes) - len(self.input_raw)
