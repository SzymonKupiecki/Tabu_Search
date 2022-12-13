import numpy as np
from quality import quality
from dtypes import ProblemInfo


class Solution:
    def __init__(self, matrix: np.ndarray, info: ProblemInfo):
        self.matrix_ = matrix
        self.quality_ = quality(info, matrix)

    def __eq__(self, other):
        if isinstance(other, Solution):
            if self.quality_ != other.quality_:
                return False
            else:
                return np.all(self.matrix_ == other.matrix_)
        elif isinstance(other, np.ndarray):
            return np.all(self.matrix_ == other)

    def __str__(self):
        obj_str = ""
        for row in self.matrix_:
            for col in row:
                obj_str += np.array2string(col) + " "
            obj_str += '\n'
        obj_str += f"Quality = {self.quality_}"
        return obj_str
