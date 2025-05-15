class Influencer:
    def __init__(self, num_selfies, num_bio_links):
        self.num_selfies = num_selfies
        self.num_bio_links = num_bio_links
    
    def __repr__(self):
        return f'({self.num_selfies}, {self.num_bio_links})'
      

def vanity(influencer):
    return ( influencer.num_bio_links * 5 ) + influencer.num_selfies


def vanity_sort(influencers):
    return sorted(influencers, key=vanity)

influencers = [
   Influencer(10, 1),
   Influencer(2, 4),
   Influencer(15, 0),
   Influencer(1, 3)
]

print(vanity_sort(influencers=influencers))


# https://storage.googleapis.com/qvault-webapp-dynamic-assets/lesson_videos/bubble-sort.mp4

def bubble_sort_example(nums):
    swapping = True
    end = len(nums)
    while swapping == True:
        swapping = False
        for i in range(1, end):
            if nums[i-1] > nums[i]:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
                swapping = True
        end -= 1
    return nums

print(bubble_sort_example([1,5,3,131,1,6,5]))

#
def bubble_sort(followers):
    swapping = True
    end = len(followers)
    while swapping == True:
        swapping = False
        for i in range(1, end):
            if followers[i-1] > followers[i]:
                followers[i-1], followers[i] = followers[i], followers[i-1]
                swapping = True
        end -= 1
    return followers

print(bubble_sort([55,11,77,111,777]))


# 

