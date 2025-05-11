# get estimated spread of shares in social media

def get_estimated_spread(audiences_followers):
    if len(audiences_followers) == 0:
        return 0
    average = sum(audiences_followers) / len(audiences_followers)
    estimated_spread = average * (len(audiences_followers) ** 1.2)
    return estimated_spread

print(get_estimated_spread([1,51,150,1231,651,21]))


# tool that predicts an influencer's follower growth over time using geometric sequence formula, for good understanding this function refers to : (If this influencer keeps growing at the current rate, how many followers will they have after num_months months from now?)
# https://storage.googleapis.com/qvault-webapp-dynamic-assets/lesson_videos/Geometric-Sequences-v1.mp4
def get_follower_prediction(follower_count, influencer_type, num_months):
    if influencer_type == 'fitness':
       return follower_count * ( 4 ** num_months)
    elif influencer_type == 'cosmetic':
        return follower_count * (3 ** num_months)
    else:
        return follower_count * (2 ** num_months)

print(get_follower_prediction(10, 'fitness', 3))
print(get_follower_prediction(25, 'cosmetic', 12))
print(get_follower_prediction(50, 'others', 5))

#
import math

print(int(math.log(16,4))) # output 2
print(int(math.log10(100))) # output 2

# algorithm: Complete the get_influencer_score function. An influencer score is their average engagement percentage multiplied by log base 2 of their follower count.

def get_influencer_score(num_followers, average_engagement_percentage):
    return average_engagement_percentage * math.log2(num_followers)

print(get_influencer_score(100000, 0.6))


# Complete the num_possible_orders function. It takes the number of posts an influencer has in their backlog as input and returns the total number of possible orders in which we could publish the posts.
 
def num_possible_order(num_posts):
    return math.factorial(num_posts)

print(num_possible_order(20))

# 
