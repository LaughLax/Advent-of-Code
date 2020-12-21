class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().splitlines()

        self.allergens = {}

    def part1(self):
        meals = []
        ingr_to_meal = {}
        allerg_to_meal = {}
        allerg_to_ing = {}
        for i, line in enumerate(self.input):
            ingr, allerg = line.split(' (contains')
            ingr = ingr.split(' ')
            allerg = allerg[:-1].split(',')

            meals.append((ingr, set(allerg)))
            for v in ingr:
                ingr_to_meal.setdefault(v, set()).add(i)
            for v in allerg:
                allerg_to_meal.setdefault(v, set()).add(i)
                for v_i in ingr:
                    allerg_to_ing.setdefault(v, set()).add(v_i)

        for allerg in allerg_to_meal:
            meal_list = allerg_to_meal[allerg]

            remove = set()
            for ingr in allerg_to_ing[allerg]:
                for meal in meal_list:
                    if ingr not in meals[meal][0]:
                        remove.add(ingr)
            allerg_to_ing[allerg] -= remove

        allerg_s = sorted(allerg_to_ing.keys(), key=lambda k: len(allerg_to_ing[k]))
        while len(allerg_s) > 0:
            a1 = allerg_s.pop(0)

            if len(allerg_to_ing[a1]) == 1:
                ingr = next(iter(allerg_to_ing[a1]))
                self.allergens[a1] = ingr
                for a2 in allerg_s:
                    if a1 == a2:
                        continue
                    allerg_to_ing[a2].discard(ingr)
            else:
                allerg_s.append(a1)

        all_ingr = set(ingr_to_meal.keys())
        all_allerg_ingr = set(allerg_to_ing[a].pop() for a in allerg_to_ing)
        all_safe_ingr = all_ingr - all_allerg_ingr

        total = 0
        for meal in meals:
            for i in all_safe_ingr:
                total += meal[0].count(i)

        return total

    def part2(self):
        sorted_keys = sorted(self.allergens.keys())
        return ','.join([self.allergens[i] for i in sorted_keys])
