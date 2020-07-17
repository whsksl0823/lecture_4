n_lists = list(range(1,101))

# for 문 축약

# 짝수만 제곱하여 배열 만들기
square_arr = [x**2 for x in n_lists if x%2 == 0 and x%3 == 0]
print(square_arr)