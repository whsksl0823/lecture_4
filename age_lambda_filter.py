# lambda 메소드를 이용한 필터
ages = [34, 25, 17, 13, 54]
print('성년리스트')

for a in filter(lambda  x: x >= 19, ages) :
    print(a)
