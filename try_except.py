# 예외처리 (오류발생 시)
try:
    a,b = input('두 수를 넣으세요').split()
    result = (int(a)/int(b))
    print(result)
except:
    print('대입한 수가 정확한 지 확인하세요')

print('test')