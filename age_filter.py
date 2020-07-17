def adult_func(n):
    if n >= 19 :
        return True
    else :
        return False

# print(adult_func(18))

ages = [34, 25, 17, 13, 54]
print('성년리스트')


# filter 메소드는 iterable 인자를 받아서 참, 거짓을 return  한다.
# print(filter(adult_func, ages))
for a in filter(adult_func, ages) :
    print(a)
