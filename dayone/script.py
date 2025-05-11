# find maximum number in the list 

def maximum_number(nums):
    maximum = float('-inf')
    if len(nums) == 0:
        return None
    for num in nums:
        if num > maximum:
            maximum = num
    return maximum

nums = [7,5,14,124,643,3,2,3131]

max_number = maximum_number(nums=nums)

print(max_number)

# find the sum of all numbers in list

def sum(nums):
    if len(nums) == 0:
        return None
    sum = 0
    for num in nums:
        sum += num
    return sum

nums = [7,5,14,124,643,3,2,3131]

print(sum(nums))

# find the average of numbers in the list

def average_followers(nums):
    if len(nums) == 0:
        return None
    average_followers = 0
    followers_count = len(nums)
    for num in nums:
        average_followers += num / followers_count
    return int(average_followers)

print(average_followers([5,100,12,15,1,1])) 
