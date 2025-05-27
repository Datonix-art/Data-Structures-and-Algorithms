lst = list((1,223,551,3131,11313,3,1,7,5,3,1))

j = 2

lst[j], lst[j-1] = lst[j-1], lst[j]

print(lst)