from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # So similar to 26/27 it's scary
        write_idx = 2 # yada yada, who cares about the first two.

        for value in nums:
            # cool value chaining ftw
            if value == nums[write_idx - 1] == nums[write_idx - 2]:
                continue

            nums[write_idx] = value
            write_idx += 1

        return write_idx