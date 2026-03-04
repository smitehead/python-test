# Set
# 중복값을 저장하지 않는 객체, 순서가 없음
# 생성 => {값,값,...} / set()
# 빈 Set을 생성 -> a={} x / set()

set_data={1,2,3,4}
print(set_data,type(set_data))
set_data={1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4}
print(set_data)

# 다수 자료형을 저장하기
# List자료형은 저장이 불가능함.
# set데이터 튜플 데이터만 저장이 가능함.
set_other={1,2,'가','나',180.5,True,(1,2,3),(1,2,3)}
print(set_other)

# set 데이터 조작하기
# 메소드 이용
set_data.add(10)
set_data.add(20)
print(set_data)
# 다수 요소를 추가하기
# update()
set_data.update(range(10,20))
print(set_data)
# 요소 삭제하기
# remove()
try : 
    set_data.remove(100)
except : 
    print("지정된 요소가 없습니다")

print(set_data)

# discard() 요소삭제-> 요소가 없어도 에러가 발생하지 않음
set_data.discard(11)
print(set_data)

set_data.discard(100)
print(set_data)

#pop : 임의값의 잘래내기함
print(set_data.pop())
print(set_data.pop())
print(set_data.pop())
print(set_data.pop())
print(set_data.pop())
print(set_data.pop())
print(set_data)

#전체 삭제하기
set_data.clear()
print(set_data)
set_data=None

#다른 데이터 타입과 호환성
test_list=[1,1,1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,4,4,4,5,5,5,6,6,7]
print(test_list)
set_data = set(test_list)
print(set_data)
test_list = list(set_data)
print(test_list)
# 문자열에서 중복값 제거하기
str_data=f"{'김'*10}{'밥'*10}{'천국'*5}"
print(str_data)
result=set(str_data)
print(result)
str_data=''.join(result)
print(str_data)

# set(집합)
# 집합연산자 활용하기
# 합집합 연산
# set|set
set_data={1,2,3,4,5,6,7}
set_data2={5,6,7,8,9,10}
set_result=set_data | set_data2
print(set_result)
set_str={'가','나','다','라'}
set_result=set_data|set_str
print(set_result)

# 메소드 : union() -> 다른 타입도 가능
set_result=set_data.union(set_data2)
print(set_result)
set_result=set_data.union(['하','호','하','가'])
print(set_result)
set_result=set_data.union("하하하하하 호호호호호 후후후후후 히히히히")
print(set_result)
temp="".join([x for x in "하하하하하 호호호호호 후후후후후 히히히히" if x!=" "])
print(temp)

#교집합 연산
set_result = set_data&set_data2
print(set_result)

#차집합 연산
set_result = set_data-set_data2
print(set_result)

# difference()
set_result=set_data.difference((1,2,3,4))
print(set_result)

# 대칭 차집합
set_result = set_data ^ set_data2
print(set_result)

#symmertic_differnce()함수를 이용
set_result=set_data.symmetric_difference(["가","나",1,2,3])
print(set_result)


#d인플레이스 연산자
# != 합집합
set_data={1,2,3,4,5}
set_data2={1,2,3,4,5,6,7,8}
result = set_data|set_data2
set_data |= set_data2
print(set_data)
#교집합
set_data &= {1,2,3,4,5,6}
print(set_data)
#차집합 :-= ,^=대칭차집합

#set데이터간 포함관계를 확인하기->대소비교를 통해 확인
set_data={1,2,3,4,5}
set_data2={2,3,4}
set_data3={2,3,6}

print(f"set_data >= set_data2 : {set_data>=set_data2}")
print(f"set_data >= set_data2 : {set_data>=set_data3}")

#서로소를 확인하는 메소드->두 집합간 같은 값이 없으면 True, 아니면 false
#isdisjoint()함수
print(f"중복값 20,30 : {set_data.isdisjoint({20,30})}")

#수정이 불가능한 set만들기
#Frozenset()함수를 이용
fset_data = frozenset({10,20,30})
fset_data2 = frozenset({10,20,30,40,50})
print(fset_data)
#set_data.add(200) 이런건 안됨
#튜플 대신 사용하는 이유는 set으로 만들면 집합연산이 가능하기 때문
print(fset_data | fset_data2)

#리스트에서 중복값을 제거
names=["바나나","나나바","바바바","나나나","바나나","바나바","나바나","바나나"]
#중복값 제거 후 리스트로 출력하기 반복문으로 출력
result = list(set(names))
for name in result :
    print(name)

#데이터를 in 연산자를이용해서 조회할때 list보다 set이 속도가 빠르다
data=list(range(10000000))
setstart =set(data)
import time
start =time.time()
# if 300 in data :
#     print("찾았다!")
#     print(f"리스트로 찾기 : {time.time()-start}")

# start=time.time()

# if 300 in setstart :
#     print("찾았다!")
#     print(f"set으로 찾기 : {time.time()-start}")

#장바구니 목록에서 구매하지 않은 물품찾기
cart_pro ={"컴퓨터","키보드","마우스"}
buy_pro={"키보드","마우스"}

print(cart_pro-buy_pro)

#컴프리핸션이용하기
str="이것을 반복해서 만들어보자고요! 집중해서"
set_str={s for s in str}
print(set_str)
#1~100사이의 값 중 3의 배수, 8의 배수를 set으로 만들기
set_num = {n for n in range(1,100) if n%3==0 or n%8==0}
print(set_num)