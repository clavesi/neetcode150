from typing import List
import unittest


class Solution:
    """
    | Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
    | The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
    | You must write an algorithm that runs in O(n) time and without using the division operation.

    | Example 1:
    | Input: nums = [1,2,3,4]
    | Output: [24,12,8,6]

    | Example 2:
    | Input: nums = [-1,1,0,-3,3]
    | Output: [0,0,9,0,0]



    Constraints:
    - 2 <= nums.length <= 105
    - -30 <= nums[i] <= 30
    - The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
    """

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        O(n) + O(n) = O(n)

        The idea here is to go through the list and get the number of zeroes that appear.
        - If it's greater than 1, then every `product` will be 0.
        - If appears once, then every other index equals 0 and the index that 0 occurs equals `product`
            - This works because 0 is not multiplied into `product` when looping to get the zeroes count
        - Otherwise, if there are zero 0s, get the total product and divide by the index's value to get the product of everything else.
        """
        product = 1
        zeroesCount = 0
        for num in nums:  # O(n)
            if num:
                product *= num
            else:
                zeroesCount += 1

        # Initialize new list with same length
        result = [0] * len(nums)

        if zeroesCount > 1:
            return result

        for i, c in enumerate(nums):  # O(n)
            if zeroesCount:
                result[i] = 0 if c else product
            else:
                result[i] = product // c

        return result

    def productExceptSelfBruteForce(self, nums: List[int]) -> List[int]:
        """
        This solution works, but it's too slow for Leetcode

        This is because it's O(n^2)
        """
        # Initialize new list with same length
        result = [0] * len(nums)

        for i in range(len(result)):  # O(n)
            product = 1
            for j in range(len(nums)):  # O(n)
                if i == j:
                    continue

                product *= nums[j]
            result[i] = product
        return result


class Test(unittest.TestCase):
    """Test Cases"""

    def setUp(self):
        self.solution = Solution()

    def testOne(self):
        nums = [1, 2, 3, 4]
        expected = [24, 12, 8, 6]
        self.assertEqual(self.solution.productExceptSelf(nums), expected)

    def testTwo(self):
        nums = [-1, 1, 0, -3, 3]
        expected = [0, 0, 9, 0, 0]
        self.assertEqual(self.solution.productExceptSelf(nums), expected)


if __name__ == "__main__":
    unittest.main()
