class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        for i in range(length):
            for j in range(i + 1,length):
                if target == nums[i] + nums[j]:
                    return [i,j]

if __name__ == '__main__':
    Solution().twoSum(nums = [2, 7, 11, 15], target = 9)