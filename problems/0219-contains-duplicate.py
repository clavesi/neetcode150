from typing import List
import unittest


class Solution:
    """Given an integer array nums, return true if any value appears at least twice in the array,
    and return false if every element is distinct.

    Examples:
    Input: nums = [1,2,3,1]
    Output: true

    Input: nums = [1,2,3,4]
    Output: false

    Input: nums = [1,1,1,3,3,4,3,2,4,2]
    Output: true
    """

    def containsDuplicate(self, nums: List[int]) -> bool:
        """| O(n)
        | -----
        | O(n) to loop through list and add to a set
        | Then just O(1) to check if List length is equal to Set length
        """
        numsSet = set(nums)  # O(n)
        return len(nums) != len(numsSet)

    def containsDuplicateSort(self, nums: List[int]) -> bool:
        """| O(nlogn)
        | -----
        | O(nlogn) to sort
        | O(n) to loop through
        | Because they're independent, they're added
        | So, O(nlogn) + O(n) = O(nlogn)
        """
        nums.sort()  # O(nlogn)
        for i in range(len(nums)-1):  # O(n)
            if nums[i] == nums[i+1]:
                return True
        return False

    def containsDuplicateBruteForce(self, nums: List[int]) -> bool:
        """| O(n^2)
        | -----
        | O(n) Outer loop
        | O(n) inner loop
        | Because the inner loop is inside the outer loop, they're multiplied.
        | So, O(n)*O(n)=O(n^2)
        """
        for i in range(len(nums)-1):  # O(n)
            for j in range(i+1, len(nums)):  # O(n)
                if nums[i] == nums[j]:
                    return True
        return False


class Test(unittest.TestCase):
    """Test Cases"""

    def setUp(self):
        self.solution = Solution()

    def test_containsDuplicate_true(self):
        # Test case where the result should be True
        nums = [1, 2, 3, 1]
        self.assertTrue(self.solution.containsDuplicate(nums))

    def test_contains_duplicate_false(self):
        # Test case where the result should be False
        nums = [1, 2, 3, 4]
        self.assertFalse(self.solution.containsDuplicate(nums))

    def test_containsDuplicate_mixed(self):
        # Test case with mixed duplicates
        nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
        self.assertTrue(self.solution.containsDuplicate(nums))


if __name__ == "__main__":
    unittest.main()
