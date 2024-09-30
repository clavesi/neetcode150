from typing import List
import unittest


class Solution:
    """Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.

    | Example 1:
    | Input: nums = [2,7,11,15], target = 9
    | Output: [0,1]
    | Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

    | Example 2:
    | Input: nums = [3,2,4], target = 6
    | Output: [1,2]

    | Example 3:
    | Input: nums = [3,3], target = 6
    | Output: [0,1]
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # TODO: more efficient Two Sum
        return []

    def twoSumBruteForce(self, nums: List[int], target: int) -> List[int]:
        """| O(n^2)
        | -----
        | O(n) Outer loop
        | O(n) inner loop
        | Because the inner loop is inside the outer loop, they're multiplied.
        | So, O(n)*O(n)=O(n^2)
        """
        for i in range(len(nums)-1):  # O(n)
            for j in range(i+1, len(nums)):  # O(n)
                if nums[i] + nums[j] == target:
                    return [i, j]

        # Problem guaranteed a solution, but just in case
        return []


class Test(unittest.TestCase):
    """Test Cases"""

    def setUp(self):
        self.solution = Solution()

    def testOne(self):
        nums = [2, 7, 11, 15]
        target = 9
        self.assertEqual(self.solution.twoSum(nums, target), [0, 1])

    def test_contains_duplicate_false(self):
        nums = [3, 2, 4]
        target = 6
        self.assertEqual(self.solution.twoSum(nums, target), [1, 2])

    def test_containsDuplicate_mixed(self):
        nums = [3, 3]
        target = 6
        self.assertEqual(self.solution.twoSum(nums, target), [0, 1])


if __name__ == "__main__":
    unittest.main()
