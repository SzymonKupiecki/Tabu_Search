import numpy as np
from solution import Solution


class TabuList:
    def __init__(self, size):
        self.size = size
        self.tab = []

    def __contains__(self, item):
        return item in self.tab

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
        if isinstance(elem, Solution):
            if isinstance(self.tab, list):
                self.tab.append(elem)
                if len(self.tab) == self.size:
                    self.tab = np.array(self.tab)
            else:
                self.tab[0] = elem
                self.tab = np.roll(self.tab, -1)
