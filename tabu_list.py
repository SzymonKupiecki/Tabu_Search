import numpy as np
from solution import Solution
from typing import Tuple


class TabuList:
    def __init__(self, size):
        self.size = size
        self.tab = []

    def __contains__(self, item):
        if isinstance(item, Solution):
            for change_type in item.changes_:
                # if change_type in self.tab:
                #     return True
                for elem in self.tab:
                    if change_type[0] == elem[0] and change_type[1] == elem[1] and change_type[2] == elem[2]:
                        return True
            return False
        else:
            return False

    def get_elem(self):
        if self.tab != 0:
            return self.tab[0]
        else:
            return None

    def get_by_index(self, index):
        if index < len(self.tab):
            return self.tab[index]
        else:
            return None

    def insert_elem(self, elem):
        # optional functionality - recognize if input is list or either Solution object - by te time it has to be list
        if isinstance(self.tab, list):
            full = -1  # variable that checks if tabu not reaching its length during insertion
            for i in range(len(elem)):  # insert each change one by one
                self.tab.append(elem[i])
                if len(self.tab) == self.size:  # if we reach desired length change type to np.array
                    self.tab = np.array(self.tab)
                    if i != len(elem):  # if sth to add is left remember index
                        full = i
                        break
            if full != -1:  # all left changes will be inserted by adding to array mechanism
                self.insert_elem(elem[full+1:])
        else:
            for item in elem:
                self.tab[0] = item
                self.tab = np.roll(self.tab, -1)
