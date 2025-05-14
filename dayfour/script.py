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