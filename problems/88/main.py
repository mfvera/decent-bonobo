from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        idx_1 = 0
        idx_2 = 0

        # Renaming and trimming for the sake of my sanity.
        # My plan is to assemble nums1 once rather than prepending elements
        numbers_1 = nums1[:m]
        numbers_2 = nums2

        while idx_1 < m or idx_2 < n:
            """
            I made the mistake of using `and` above, which cuts the output short once one list finishes.
            Changing this to `or` required additional out of bounds checking that I'm not really a fan of.
            """
            if idx_1 == m:
                nums1[idx_1 + idx_2] = numbers_2[idx_2]
                idx_2 += 1
                continue

            if idx_2 == n:
                nums1[idx_1 + idx_2] = numbers_1[idx_1]
                idx_1 += 1
                continue

            num_1 = numbers_1[idx_1]
            num_2 = numbers_2[idx_2]

            if num_1 < num_2:
                nums1[idx_1 + idx_2] = num_1
                idx_1 += 1
            else:
                nums1[idx_1 + idx_2] = num_2
                idx_2 += 1

