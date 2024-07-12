from typing import List
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Technically just returns the most common element regardless of if it's a majority.
        return Counter(nums).most_common()[0][0]