class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        total_nums=len(nums)
        j = total_nums - 1
        first_num = 0
        second_num = 0

        while i < total_nums:
            first_num = nums[i]
            j = total_nums - 1 
            while j < total_nums and j >= 0:
                if i == j:
                    j -= 1
                    continue
                second_num = nums[j]
                sum = first_num + second_num
                
                if sum == target:
                    return [i, j]
                
                
                j -= 1
            i += 1
            j = 0

