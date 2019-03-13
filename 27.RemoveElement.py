class Solution:
    def removeElement(self, nums, val) :
        i,last = 0,len(nums)-1
        while i <= last:
            if nums[i] == val:
                nums[i],nums[last] = nums[last],nums[i]
                last -= 1
            else:
                i += 1
        return last+1

if __name__ == "__main__":
    s = Solution()
    L = s.removeElement([3,2,2,3],3)
    print(L)
