def get_avg_brang_followers(all_handles, brand_name):
    count = 0
    for handles in all_handles:
        for handle in handles:
            if brand_name in handle:
                count += 1
    return count / len(all_handles)

all_handles = [
    ["cosmofan1010", "cosmogirl", "billjane321"],
    ["cosmokiller", "gr8", "cosmojane3"],
    ["iloveboots", "paperthin"]
]

brand_name = 'cosmo'

print(get_avg_brang_followers(all_handles, brand_name))


#   def find_last_name(names_dict, first_name):
def find_last_name(names_dict, first_name):
    try:
        return names_dict[first_name]
    except KeyError:
        return None


names_dict = {
    "firstname": 'david',
    "lastname": 'lezhava'
}

first_name = 'david'

print(find_last_name(names_dict, first_name))


#

def search(target, arr):
    try:
        if arr.index(target) != -1:
            return target
    except ValueError:
        return False

#

def binary_search(target, arr):
    low = 0
    high = len(arr) - 1
    while low <= high:
        median = (low + high) // 2
        if arr[median] == target:
            return True
        elif arr[median] < target:
            low = median + 1
        else:
            high = median - 1
    return False


arr = ['web dev', 'software engineering', 'ML engineering', 'Data Structures and Algorithms']
target = 'web dev'

arr.sort()

print(search(target, arr))
print(binary_search(target, arr))

# 

def count_names_with_binary_search(list_of_lists, target_name):
    low = 0
    high = len([all_names for all_names in list_of_lists]) - 1
    while low <= high:
        median = (low + high) // 2
        count = 0
        for all_names in list_of_lists:
            if all_names[median] == target_name:
                count += 1
            elif all_names[median] < target_name:
                low = median + 1
            else:
                high = median - 1
    return count


list_of_lists = [
    ["John", "Alice", "Bob"],
    ["Alice", "John", "Charlie"],
    ["Bob", "Eve", "Alice"],
    ["Charlie", "Eve", "John"]
]

for lst in list_of_lists:
    lst.sort()

target_name = "Alice"

print(count_names_with_binary_search(target_name=target_name, list_of_lists=list_of_lists))


#
def count_names(list_of_lists, target_name):
    count = 0
    for lst in list_of_lists:
        count += lst.count(target_name)
    return count

target_name = "Alice"

list_of_lists = [
    ["John", "Alice", "Bob"],
    ["Alice", "John", "Charlie"],
    ["Bob", "Eve", "Alice"],
    ["Charlie", "Eve", "John"]
]

print(count_names(list_of_lists, target_name))

