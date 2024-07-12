from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 0th element is guaranteed to be the first of it's kind.
        write_idx = 1

        # Same iteration practice as ../27
        for value in nums:
            if value == nums[write_idx - 1]:
                continue

            nums[write_idx] = value
            write_idx += 1

        return write_idx