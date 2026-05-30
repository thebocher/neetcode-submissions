class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m

            if nums[m] >= nums[0]:
                if target > nums[m]:
                    l = m+1
                else:
                    if target >= nums[0]:
                        r = m-1
                    else:
                        l = m+1
            else:
                if target < nums[m]:
                    r = m-1
                else:
                    if target <= nums[-1]:
                        l = m+1
                    else:
                        r = m-1

            # if l == r:
            #     break
            
            # if nums[m] <= nums[-1]:
            #     if nums[m] > target:
            #         if target > nums[-1]:
            #             r = m-1
            #         else:
            #             l = m+1
            #     else:
            #         r = m-1
            # else:
            #     if nums[m] < target:
            #         l = m+1
            #     else:
            #         if target < nums[0]:
            #             l = m+1
            #         else:
            #             r = m-1
            
        return -1