class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input_raw = f.read()

        self.input = int(self.input_raw)

        self.recipe_list = RecipeList()
        
    def part1(self):
        elf_1 = self.recipe_list.first_recipe
        elf_2 = self.recipe_list.first_recipe.right

        while self.recipe_list.num_recipes < self.input + 10:
            new_val = elf_1.value + elf_2.value

            if new_val >= 10:
                self.recipe_list.add_recipe(Recipe(1))
                self.recipe_list.add_recipe(Recipe(new_val % 10))
            else:
                self.recipe_list.add_recipe(Recipe(new_val))

            elf_1 = elf_1.move_right(elf_1.value + 1)
            elf_2 = elf_2.move_right(elf_2.value + 1)

        return self.recipe_list.values_after(self.input, 10)

    
    def part2(self):
        self.recipe_list = RecipeList()
        elf_1 = self.recipe_list.first_recipe
        elf_2 = self.recipe_list.first_recipe.right

        while True:
            new_val = elf_1.value + elf_2.value

            if new_val >= 10:
                self.recipe_list.add_recipe(Recipe(1))
                if self.recipe_list.check_if_sequence_at_end(self.input_raw):
                    break
                self.recipe_list.add_recipe(Recipe(new_val % 10))
            else:
                self.recipe_list.add_recipe(Recipe(new_val))
            if self.recipe_list.check_if_sequence_at_end(self.input_raw):
                break

            elf_1 = elf_1.move_right(elf_1.value + 1)
            elf_2 = elf_2.move_right(elf_2.value + 1)

        return self.recipe_list.num_recipes - len(self.input_raw)


class RecipeList:

    def __init__(self):
        self.first_recipe = Recipe(3)
        Recipe(7).insert_after(self.first_recipe)
        self.num_recipes = 2

    def add_recipe(self, recipe):
        recipe.insert_before(self.first_recipe)
        self.num_recipes += 1

    def values_as_list(self):
        vals = [self.first_recipe.value]
        recipe = self.first_recipe.right
        while recipe is not self.first_recipe:
            vals.append(recipe.value)
            recipe = recipe.right
        return vals

    def values_after(self, after, num):
        if after >= self.num_recipes:
            return ''

        added = 0
        nums = []
        recipe = self.first_recipe.move_left(self.num_recipes - after)
        while added < num and recipe is not self.first_recipe:
            nums.append(str(recipe.value))
            added += 1
            recipe = recipe.right

        return ''.join(nums)

    def check_if_sequence_at_end(self, sequence):
        length = len(sequence)
        end_seq = self.values_after(self.num_recipes - length, length)

        return True if end_seq == sequence else False


class Recipe:

    def __init__(self, value):
        self.value = value
        self.left = self
        self.right = self

    def insert_before(self, other):
        self.right = other
        self.left = other.left

        other.left = self
        self.left.right = self

    def insert_after(self, other):
        self.left = other
        self.right = other.right

        other.right = self
        self.right.left = self

    def move_right(self, n):
        if n <= 0:
            return self
        
        return self.right.move_right(n - 1)
        
    def move_left(self, n):
        if n <= 0:
            return self
        
        return self.left.move_left(n - 1)
        
