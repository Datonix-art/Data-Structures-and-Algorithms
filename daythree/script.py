# It calculates the final value of a quantity after a certain time has passed, given its initial value and a rate of decay
# (1-fraction_lost_daily) calculates procent left after decay
def decayed_followers(intl_followers, fraction_lost_daily, days):
    res = intl_followers * (1 - fraction_lost_daily) ** days
    return res

print(decayed_followers(100, .5, 3))


# logarithmic scale
import math

def log_scale(data, base):
    data_base = []
    for number in data:
        logarithm = math.log(number, base)
        data_base.append(int(logarithm)) 
    return data_base

res = log_scale([1, 10, 100, 1000], 10)
print(res)

#* https://storage.googleapis.com/qvault-webapp-dynamic-assets/lesson_videos/big-o-notation-v1-23-00-x264.mp4

def get_full_names(first_names, last_names):
    full_names = []
    for firstname in first_names:
        for lastname in last_names:
            full_names.append(f'firstname: {firstname}, lastname: {lastname}') 
    return full_names

res = get_full_names(['nato', 'dato', 'levan'], ['lezhava', 'pochkhua'])
print(res)

# order n
def find_max(nums):
    if len(nums) == 0:
        return None
    maximum = float('-inf')
    for num in nums:
        if maximum < num:
            maximum = num
    return maximum

print(find_max([1,2,541,41,41,1,411,6141,41]))

# order n squared. n^2 algorithm that is very slow to iterate over every list and find common in full_name 

def does_name_exist(first_names, last_names, full_name):
    for firstname in first_names:
        for lastname in last_names:
            if firstname + " " + lastname == full_name:
                return True
    return False

first_names = [
    "Alice", "Bob", "Charlie", "David", "Emma", "Fiona", "George", "Hannah",
    "Ian", "Julia", "Kevin", "Laura", "Michael", "Nina", "Oscar", "Paula",
    "Quentin", "Rachel", "Steve", "Tina", "Uma", "Victor", "Wendy", "Xavier",
    "Yara", "Zach"
]
last_names =  [
    "Anderson", "Brown", "Clark", "Davis", "Evans", "Foster", "Garcia", "Hall",
    "Ingram", "Johnson", "King", "Lewis", "Martinez", "Nelson", "Owens", "Perez",
    "Quinn", "Robinson", "Smith", "Taylor", "Underwood", "Vasquez", "White", "Xu",
    "Young", "Zimmerman"
]
full_name ='Alice Anderson'
print(does_name_exist(first_names, last_names, full_name))

# O(n) algorithm
def print_name(first_names):
    for first_name in first_names:
        print(first_name)

# O(n^2) algorithm
def print_full_name(first_names, last_names):
    for firstname in first_names:
        for lastname in last_names:
            print(firstname, lastname)

# O(n^3) algorithm
def print_full_name_and_age(first_names, last_names, ages):
    for firstname in first_names:
        for lastname in last_names:
            for age in ages:
                print(firstname, lastname, age)

# O(nm) algorithm  
# https://www.boot.dev/lessons/7d38f457-fbd2-42ae-adc2-b2ca6f8bfaee
def get_avg_brand_followers(all_handles, brand_name):
    pass