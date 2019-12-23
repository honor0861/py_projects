import test6

# 예외처리
# 코드는 잠재적으로 오류를 가질 수 있음
# 이 때, s/w가 다운되지 않게 하고 정보를 수집하고
# 문제없이 다음 단계로 진행시키게 하는 방법

# case1 예외 발생 시 코드 진행 확인
print(0)
try: # 예외가 발생할 만한 코드를 감싼다
    print(1)
    print(1/0)
    print(2)
except Exception as e: # 예외가 발생하면 호출
    print(3,e)
else: # 예외없이 정상적으로 코드 진행되면 호출
    print(4)
finally: # 무조건 수행
    print(5)
print(6)


# case2 정상 시 코드 진행 확인
print(0)
try: # 예외가 발생할 만한 코드를 감싼다
    print(1)
    # print(1/0)
    print(2)
except Exception as e: # 예외가 발생하면 호출
    print(3,e)
else: # 예외없이 정상적으로 코드 진행되면 호출
    print(4)
finally: # 무조건 수행
    print(5)
print(6)