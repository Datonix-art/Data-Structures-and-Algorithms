def insertion_sort(nums):
    if len(nums) < 2:
        return nums
    
    for i in range(1, len(nums)):
        j = i
        while nums[j] > 0 and nums[j-1] > nums[j]:
            nums[j], nums[j-1] = nums[j-1], nums[j]
            j -= 1

    return nums
    
print(insertion_sort([1,2,541,41,4,514,1,41]))


#
# quick sort https://storage.googleapis.com/qvault-webapp-dynamic-assets/lesson_videos/quick-sort.mp4

def quick_sort(nums, low, high):
    if low < high:
        p = partition(nums, low, high)
        quick_sort(nums, low, p - 1)
        quick_sort(nums, p + 1, high)


def partition(nums, low, high):
    pivot = nums[high]
    i = low
    for j in range(low, high):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[high] = nums[high], nums[i]
    return i

lst = [1,54,15,1,144,141]

quick_sort(lst, 0, len(lst) - 1)

print(lst)


import random


data = [1,23,531,313,13]

median = data[len(data) // 2]
print(median)

random.shuffle(data)
print(data)


#

def selection_sort(nums):
    n = len(nums)

    if n < 2:
        return nums
    # i current index, j inner index
    for i in range(n):
        smallest_idx = i # 0,1,2,3
        for j in range(i + 1, n): # starts from 1, 3
            print(j) # 1 2 3 2 3 3 
            """ 
            1,2,3
            2,3
            3
            """
            if nums[j] < nums[smallest_idx]:
                smallest_idx = j
        nums[i], nums[smallest_idx] = nums[smallest_idx], nums[i]
    return nums

print(selection_sort([21,3541,41,41]))
