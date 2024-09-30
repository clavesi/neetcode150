from collections import defaultdict
import unittest


class Solution:
    """
    Given two strings s and t, return true if t is an anagram of s, and false otherwise.

    | Example 1:
    | Input: s = "anagram", t = "nagaram"
    | Output: true

    | Example 2:
    | Input: s = "rat", t = "car"
    | Output: false

    | Constraints:
    - 1 <= s.length, t.length <= 5 * 104
    - s and t consist of lowercase English letters.
    """

    def isAnagram(self, s: str, t: str) -> bool:
        """| O(n) - HashMap (dictionary)
        | -----
        | O(1) length check
        | O(n) loop
        | O(1) in and update
        | O(n) equivalence check
        | Because the loop and the equivalence check are independent, they're added.
        | So, O(n)+O(n)=O(n)
        """
        # Quick length check
        if (len(s) != len(t)):
            return False

        sDictionary = {}
        tDictionary = {}
        for i in range(len(s)):
            if s[i] in sDictionary:
                sDictionary.update({s[i]: sDictionary.get(s[i])+1})
            else:
                sDictionary.update({s[i]: 1})

            if t[i] in tDictionary:
                tDictionary.update({t[i]: tDictionary.get(t[i])+1})
            else:
                tDictionary.update({t[i]: 1})

        return sDictionary == tDictionary

    def mySolutionSimplified(self, s: str, t: str) -> bool:
        """| Courtesy of NeetCode
        | This is what I wanted to do, don't know why I thought I needed the in check
        """
        # Quick length check
        if (len(s) != len(t)):
            return False

        sDictionary = {}
        tDictionary = {}
        for i in range(len(s)):
            sDictionary[s[i]] = 1 + sDictionary.get(s[i], 0)
            tDictionary[t[i]] = 1 + tDictionary.get(t[i], 0)

        return sDictionary == tDictionary

    def moreEfficientHashMap(self, s: str, t: str) -> bool:
        """
        | Courtesy of rahulvarma5297 on LeetCode
        | This is the same logic as mine, but it's 49ms vs my 70ms.
        | Why?

        My version created two different dictionaries, which requires more memory.
        I have a get and then get/update twice a loop, which is slower than this which just updates.
        My comparison also has to traverse both lists, which is slower than just doing a single traversal over count.
        """
        count = defaultdict(int)
        # Count the frequency of characters in string s
        for x in s:
            count[x] += 1

        # Decrement the frequency of characters in string t
        for x in t:
            count[x] -= 1

        # Check if any character has non-zero frequency
        for val in count.values():
            if val != 0:
                return False

        return True


class Test(unittest.TestCase):
    """Test Cases"""

    def setUp(self):
        self.solution = Solution()

    def testOne(self):
        s = "anagram"
        t = "nagaram"
        self.assertTrue(self.solution.isAnagram(s, t))

    def testTwo(self):
        s = "rat"
        t = "car"
        self.assertFalse(self.solution.isAnagram(s, t))


if __name__ == "__main__":
    unittest.main()
