# fibonnaci sequence

#* exponential fibonacci algorithm
def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)


#* polynomal finonacci algorithm
def fibonnaci(n):
    if n == 0 or n == 1:
        return n
    
    gradparent = 0
    parent = 1
    current = None
    
    for _ in range(n - 1):
        current = parent + gradparent # f(x) = f(x-1) + f(x-2)
        gradparent = parent #f(x-2) = f(x-1)
        parent = current # f(x-2) = f(x)

    return current
                
print(fibonnaci(5))



# power set algorithm with complexity of O(2^n)

def power_set(input_set):
    if len(input_set) == 0:
        return [[]]
    subsets = [[]]
    for el in input_set:
        new_subsets = []
        for subset in subsets:
            new_subset = [el] + subset
            new_subsets.append(new_subset)
        subsets.extend(new_subsets)
    return subsets
        

print(power_set([5,6,8]))


# O(n) T(n) = O(n + n/2 + n/4 ..)

def halved_section(n):
    rows = []
    i = n
    while i > 0:
        col = []
        for j in range(i+1):
            col.append(j)
        rows.append(col)
        i //= 2
    return rows

print(halved_section(12))


# [10, 20, 40, 80, 160]

def exponential_growth(n, factor, days):
    growth_sequence = [n]
    growth = n
    for _ in range(days):
        growth *= factor
        growth_sequence.append(growth)
    return growth_sequence

print(exponential_growth(10, 2, 4))


#

def count_marketers(job_titles):
    return sum(1 for title in job_titles if title.lower() == 'marketer')

count = count_marketers(['programmer', 'marketer', 'doctor', 'marketer'])
      
print(count)

# big O complexity for this function is O(1)

def last_work_experience(work_experiences):
    if not work_experiences:
        return None
        
    ordered_list = sorted(work_experiences, reverse=True) 
    return ordered_list[0]

def last_work_experience(work_experiences):
    if len(work_experiences) > 0:
        return work_experiences[len(work_experiences) - 1]
    return None

print(last_work_experience(["Intern", "Engineer", "Team Lead"])  )

