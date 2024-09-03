def two_sums(nums: int, target: int) -> list:

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return([i,j])
            
print(two_sums([2,7,11,15], 9))



