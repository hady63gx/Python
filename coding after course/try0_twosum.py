class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


nums = [1, 2, 3, 4, 5]
target = 3
s = Solution()
ans = s.twoSum(nums, target)
print(ans)
