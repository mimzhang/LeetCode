class Solution:
    def twoSum(self, nums, target):
        start = 0
        end = len(nums)-1
        suum = 0

        while start != end:
            suum = nums[start] + nums[end]  #为何放在循环里面
            if suum > target:
                end = end - 1
            elif suum < target:
                start = start + 1
            else:
                return [start+1,end+1]
s = Solution()
result_list = s.twoSum([2, 7, 11, 15], target = 9)
print(result_list)            
#print(Solution().twoSum(nums=[2, 7, 11, 15], target = 9))