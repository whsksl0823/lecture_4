def add(x, y):
    return x+y

add_other = lambda x, y : x + y


# print(add(10,50))
print(add_other(11,50))


def add_plus(x, y, z):
    result_1 = x + y  
    result_2 = lambda z : z**3
    
    return result_1 , result_2

print(add_plus(10, 30, 20))