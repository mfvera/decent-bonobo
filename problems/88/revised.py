from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # the numbers are now largest first, but since I'll treat the lists as stacks this is perfect
        numbers_1 = list(reversed(nums1[:m]))
        numbers_2 = list(reversed(nums2))

        i = 0 # our 'output' index.
        while len(numbers_1) and len(numbers_2):
            number_1 = numbers_1[-1] # no peeking D:
            number_2 = numbers_2[-1]

            if number_1 < number_2:
                nums1[i] = numbers_1.pop()
            else:
                nums1[i] = numbers_2.pop()
            i += 1

        # only one will have values at most, so this is really just being concise
        remnants = reversed([*numbers_1, *numbers_2])
        for remnant in remnants:
            nums1[i] = remnant
            i += 1

        assert(i == n+m)
