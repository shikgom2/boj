def solve(nums):
    min_sum = 999999999999
    result = []

    for i in range(len(nums)-2):
        #set left & right
        left = i+1
        right = len(nums) - 1

        while left < right:
            sum = nums[i] + nums[left] + nums[right]
    
            if abs(sum) < abs(min_sum):
                min_sum = sum
                result = [nums[i], nums[left], nums[right]] #Already sort
            #Go left or right
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            elif sum == 0:
                return result
    return result

#Input
N = int(input())
nums = list(map(int, input().split()))
nums.sort() #1
result = solve(nums)
#Output
for res in result:
    print(res, end=" ")


    