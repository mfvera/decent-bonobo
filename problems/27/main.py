from typing import List

class Solution:
    def removeElement(self, nums: List[int], value_to_delete: int) -> int:
        # I *really* want to just make an output list and then just reassign the values into nums
        # but that feels against the spirit of the problem.
        write_idx = 0

        # iteration is safe since we're only changing indices we've already seen.
        for value in nums:
            if value == value_to_delete:
                continue

            nums[write_idx] = value
            write_idx += 1

        return write_idx