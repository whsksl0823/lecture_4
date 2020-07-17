n_list = [1, 20, -3, 4, -20, 10, 100]

minus_list = list()
minus_list2 = list()

for a in filter(lambda n : n < 0, n_list) : 
    # minus_list.insert(0, a)
    minus_list2.append(a)

# print(minus_list)
print(minus_list2)