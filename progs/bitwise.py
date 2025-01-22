""" You are given two 0-indexed arrays, nums1 and nums2, consisting of non-negative integers. There exists another array, nums3, which contains the bitwise XOR of all pairings of integers between nums1 and nums2 (every integer in nums1 is paired with every integer in nums2 exactly once).

Return the bitwise XOR of all integers in nums3.



Example 1:

Input: nums1 = [2,1,3], nums2 = [10,2,5,0]
Output: 13
Explanation:
A possible nums3 array is [8,0,7,2,11,3,4,1,9,1,6,3].
The bitwise XOR of all these numbers is 13, so we return 13.
"""
# from rpds import List
#
#
from typing import List


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        xor = []
        for i in range(len(nums1)):
            print(i)
            for j in range(len(nums2)):
                print(j)
                xor.append(nums1[i] ^ nums2[j])
        print(xor)
        x = 0
        for i in xor:
            x ^= i
        return x

nums1 = [2,1,3]
nums2 = [10,2,5,0]
xor = []
for i in range(len(nums1)):
    print(i)
    for j in range(len(nums2)):
        print(j)
        xor.append(nums1[i]^nums2[j])
print(xor)
x = 0
for i in xor:
    x ^= i
print(x)


