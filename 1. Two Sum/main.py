from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to map number values to their indices
        value_to_index = {value: index for index, value in enumerate(nums)}

        # Iterate through nums to find a pair such that their sum equals target
        for index, num in enumerate(nums):
            complement = target - num
            if complement in value_to_index and value_to_index[complement] != index:
                # Return the indices of the two numbers
                return [index, value_to_index[complement]]