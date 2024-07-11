from typing import List
from itertools import chain

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        idx_1 = 0
        idx_2 = 0

        numbers_1 = nums1[:m]
        numbers_2 = nums2

        # O((n+m)log(n+m))
        for i, val in enumerate(sorted(chain(numbers_1, numbers_2))):
            nums1[i] = val