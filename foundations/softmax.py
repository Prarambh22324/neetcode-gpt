import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        x = z - np.max(z)
        expo = np.exp(x)
        return np.round(expo / np.sum(expo), 4)
