# 예외처리 (오류발생 시)
try:
    a,b = input('두 수를 넣으세요').split()
    result = (int(a)/int(b))
    print(result)
except ZeroDivisionError:
    print('0으로는 나눌 수 없습니다.')
except TypeError:
    print('지원되지 않는 연산자를 사용한 오류')
except Exception as e:
    print("오류 종류 : ", e)
    
print('test')