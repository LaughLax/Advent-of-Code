class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input_raw = f.read()

        self.input = int(self.input_raw)

    def part1(self):
        self.recipes = [3, 7]
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

        check = [int(d) for d in self.input_raw]
        check_pos = 0
        length = len(self.input_raw)

        while True:
            new_val = self.recipes[elf_1] + self.recipes[elf_2]

            if new_val >= 10:
                new_val = new_val % 10
                self.recipes.append(1)
                if check[check_pos] == 1:
                    check_pos += 1
                    if check_pos == length:
                        break
                else:
                    check_pos = 0
            
            self.recipes.append(new_val)
            if check[check_pos] == new_val:
                check_pos += 1
                if check_pos == length:
                    break
            else:
                check_pos = 0

            elf_1 = (elf_1 + self.recipes[elf_1] + 1) % len(self.recipes)
            elf_2 = (elf_2 + self.recipes[elf_2] + 1) % len(self.recipes)

        return len(self.recipes) - length
