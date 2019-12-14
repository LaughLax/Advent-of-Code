import numpy as np


class ReactionTree:
    def __init__(self, res_amount, res_type, inputs):
        self.res_type = res_type
        self.res_amount = res_amount
        self.inputs = inputs

        self.parents = []
        self.children = []
        self.height = 0

    def add_parent(self, parent):
        self.parents.append(parent)
        parent.children.append(self)

    def is_in_parents(self, reaction):
        searched = set()
        to_search = self.parents
        while len(to_search) > 0:
            searching = to_search.pop()
            searched.add(searching)
            if searching.res_type == reaction:
                return True
            else:
                for par in searching.parents:
                    if par not in searched:
                        to_search.append(par)
        return False

    def determine_height(self):
        this_layer = self.children.copy()
        depth = 0
        while len(this_layer) > 0:
            next_layer = []
            for item in this_layer:
                next_layer.extend(item.children)
            depth += 1
            this_layer = next_layer
        self.height = depth


class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().splitlines()
        self.reactions = {'ORE': ReactionTree(0, 'ORE', [])}
        for line in self.input:
            goes_in, comes_out = line.split('=>')
            out_amount, out_prod = comes_out.split()
            out_amount = int(out_amount)
            in_prods = goes_in.split(',')
            ins = []
            for i in in_prods:
                in_amount, in_prod = i.split()
                in_amount = int(in_amount)
                ins.append((in_prod, in_amount))
            self.reactions[out_prod] = ReactionTree(out_amount, out_prod, ins)
        for r in self.reactions:
            if r != 'ORE':
                for inp in self.reactions[r].inputs:
                    self.reactions[inp[0]].add_parent(self.reactions[r])
        for r in self.reactions:
            self.reactions[r].determine_height()

    def part1(self):
        ore = 0
        mats = {'FUEL': 1}
        while len(mats) > 0:
            searching = None
            max_height = 0
            for key in mats:
                react = self.reactions[key]
                good = True
                for key2 in mats:
                    if react.is_in_parents(key2):
                        good = False
                if not good:
                    continue
                if good and react.height > max_height:
                    max_height = react.height
                    searching = key
            amount_needed = mats[searching]
            del mats[searching]
            react = self.reactions[searching]
            mult = 1
            while mult * react.res_amount < amount_needed:
                mult += 1
            for reagent in react.inputs:
                if reagent[0] == 'ORE':
                    ore += mult * reagent[1]
                else:
                    if reagent[0] not in mats:
                        mats[reagent[0]] = mult * reagent[1]
                    else:
                        mats[reagent[0]] = mats[reagent[0]] + mult * reagent[1]
        return ore

    def part2(self):
        max_ore_per_fuel = 136771
        max_ore = 1000000000000
        min_fuel_gain = int(1000000000000 / max_ore_per_fuel)

        fuel_try = min_fuel_gain
        while True:
            ore = 0
            mats = {'FUEL': fuel_try}
            while len(mats) > 0:
                searching = None
                max_height = 0
                for key in mats:
                    react = self.reactions[key]
                    if react.height > max_height:
                        max_height = react.height
                        searching = key
                amount_needed = mats[searching]
                del mats[searching]
                react = self.reactions[searching]
                mult = np.ceil(amount_needed / react.res_amount)
                for reagent in react.inputs:
                    if reagent[0] == 'ORE':
                        ore += mult * reagent[1]
                    else:
                        if reagent[0] not in mats:
                            mats[reagent[0]] = mult * reagent[1]
                        else:
                            mats[reagent[0]] = mats[reagent[0]] + mult * reagent[1]
            if ore > max_ore:
                return fuel_try - 1
            else:
                fuel_try += 1
