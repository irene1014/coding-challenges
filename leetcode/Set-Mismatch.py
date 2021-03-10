# 645. Set Mismatch: https://leetcode.com/problems/set-mismatch/
def findErrorNums(nums):
    s = list(set(nums))
    for i in range(1, len(nums) + 1):
        if i in s:
            s.pop(s.index(i))
            nums.pop(nums.index(i))
        else:
            mv = i
    dv = nums[0]
    return [dv, mv]


print(findErrorNums([1, 2, 2, 4]))
