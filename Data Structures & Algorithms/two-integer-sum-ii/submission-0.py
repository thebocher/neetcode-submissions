class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1

        while l < r:
            guess = numbers[l] + numbers[r]
            
            if guess == target:
                return [l+1, r+1]

            if guess > target:
                # move right pointer
                r -= 1
            else:
                # move left pointer
                l += 1
            
        