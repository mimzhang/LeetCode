class Solution:
    def threeSum(self, nums):
        RL = [] #存储结果
        
        nums.sort()
        print(nums)
        for i in range(len(nums)):  #记得加range()
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:    #[0,0,0]会出问题
                continue
            
            j = i + 1
            k = len(nums)-1
            target = -nums[i]

            while j < k:
                suum = nums[j] + nums[k]
                print(suum,target)

                # if nums[j] == nums[j-1]:
                #     j = j + 1
                #     continue
                # if nums[k] == nums[k+1]:
                #     k = k - 1
                #     continue
                # if suum > target:
                #     k = k-1
                # elif suum < target:
                #     j = j+1
                # else:
                #     RL.append([nums[i],nums[j],nums[k]])
                if suum == target:
                    RL.append([nums[i],nums[j],nums[k]])
                    k = k-1
                    j = j+1
                elif suum > target:
                    k = k-1
                else:
                    j = j+1   
            s = set()
            if RL:
                for i in RL:
                    s.add((i[0],i[1],i[2]))  
 
        return list(s)

if __name__ == '__main__':
    s = Solution()
    RL = s.threeSum([])
    print(RL)

# class Solution(object):
#     def threesuum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         # 存储结果列表
#         res_list = []
#         # 对nums列表进行排序，无返回值，排序直接改变nums顺序
#         nums.sort()
#         for i in range(len(nums)):
#             # 如果排序后第一个数都大于0，则跳出循环，不可能有为0的三数之和
#             if nums[i] > 0:
#                 break
#             # 排序后相邻两数如果相等，则跳出当前循环继续下一次循环，相同的数只需要计算一次
#             if nums[i] == nums[i-1]:
#                 continue
#             # 记录i的下一个位置
#             j = i + 1
#             # 最后一个元素的位置
#             k = len(nums) - 1
#             while j < k:
#                 # 判断三数之和是否为0
#                 if nums[j] + nums[k] == -nums[i]:
#                     # 把结果加入数组中
#                     res_list.append([nums[i], nums[j], nums[k]])
#                     # 判断j相邻元素是否相等，有的话跳过这个
#                     while j < k and nums[j] == nums[j+1]: j += 1
#                     # 判断后面k的相邻元素是否相等，是的话跳过
#                     while j < k and nums[k] == nums[k-1]: k -= 1
#                     # 没有相等则j+1，k-1，缩小范围
#                     j += 1
#                     k -= 1
#                 # 小于-nums[i]的话还能往后取
#                 elif nums[j] + nums[k] < -nums[i]:
#                     j += 1
#                 else:
#                     k -= 1
#         return res_list

# if __name__ == '__main__':
#     s = Solution()
#     result_list = s.threesuum([0,0,0])
#     print(result_list)

# class Solution(object):
#     def threeSum(self, nums):
#         nums.sort()
#         RL =[]
#         for i in range(len(nums)):
#             if i == 0 or nums[i]>nums[i-1]:
#                 k = i+1
#                 r = len(nums)-1
#                 while k < r:
#                     s = nums[i] + nums[k] +nums[r]
#                     if s ==0:
#                         RL.append([nums[i],nums[k],nums[r]])
#                         k +=1
#                         r -=1
#                         while k < r and nums[k] == nums[k-1]:
#                             k += 1
#                         while r > k and nums[r] == nums[r+1]:
#                             r -= 1
#                     elif s>0:
#                         r -=1
#                     else :
#                         k +=1
#         return RL
# if __name__ == '__main__':
#     s = Solution()
#     result_list = s.threeSum([0,0,0,0])
#     print(result_list)