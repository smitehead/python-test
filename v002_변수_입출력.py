#변수 활용하기
#파이썬에서 변수는 자료형이 없이 선언함
#동적 자료형으로 데이터는 object로 처리(변수 주소저장)
# 변수 선언 및 대입
bool_var = True
int_var=19
float_var=180.5
str_var="bananan"
list_var=[1,2,3,4,5]
tuple_var=("가","나","다","라")
set_var={'a','b','c','d','e'}
dict_var={"name":"banana","age":22}

#한번에 다수의 변수를 선언하고 저장
test1,test2,test3="인간시대의 끝이 도래했다", 30,["리","스","트"]

# print 함수 활용하기
#기본 리터럴 출력
print("test")
print(1234)
print(True)

#한번에 여러값 출력하기
print("test",19,180.5)

#print 함수 옵션 이용하기
#sep옵션 -> 기본값 ''
print(2026,"02",25,sep="-")

#end옵션 ->기본값 \n
print("test",end="\t")
print("test2")

#print()함수에서 변수출력하기
print(bool_var)
print(int_var)
print(float_var)
print(str_var)
print(list_var)
print(tuple_var)
print(set_var)
print(dict_var)

#문자열 패턴을 출력하기
# f-string 이용하기
name="바나나"
age=22
print(f"이름 : {name}, 나이 : {age}")

#문자열 정렬하기
#{변수명:<숫자} 왼쪽정렬
#{변수명:>숫자} 오른쪽정렬
#{변수명:^숫자} 가운데정렬
#{변수명:<0n} : 공백을 0으로 표시
print(f"내 이름은 {name:<10} 나이는 {age:>3}입니다")
print(f"내 이름은 {name:<10} 나이는 {age:<3}입니다")
print(f"내 이름은 {name:^10} 나이는 {age:>03}입니다")
print(f"내 이름은 {name} 나이는 {age}키는 {174.32823:.2f}")
#format함수 이용하기
print("내이름은 {0} 나이는 {1}입니다".format(name, age))

# %패턴
print("내 이름은 %s 나이는 %d입니다" %(name,age))

#변수의 타입을 확인하기
# type()함수를 이용하기
print(type(str_var))
print(type(int_var))
print(type(float_var))
print(type(bool_var)) 
print(type(list_var))
print(type(tuple_var))
print(type(set_var))
print(type(dict_var))


type_test=type(str_var)
print(dir(type_test))
print(type_test.__name__)

#모든 값은 객체로 처리
print(int_var)
#주소값
print(id(int_var))

#호이스팅이 가능한가?
#안됨
# print(a)
# a="banana"

#문자열 합치기 => +연산자
#안됨
# temp = "안녕"+19+"살"

#출력을 다른곳으로 하는법
#print() ->콘솔로 출력
#파일 만들어서 print한걸 쓰기
with open('output.txt','w',encoding='utf-8') as f :
    print(f"내 이름은 {name} 나이는 {age}입니다",file=f)

#형변환 하기

#문자열을 정수형으로 변경하기
# int()함수 이용해서 변경
str_var="10" #문자열
test=int(str_var)
print(f"값 : {test} / 타입 : {type(test)}")

# test=int(float_var)
print(f"값 : {test} / 타입 : {type(test)}")

#실수형을 문자열로 변경
#str()함수 이용해서 변경
test=str(float_var)
print(f"{test} / {type(test)}")

#문자열을 실수형으로 변경하기
#float()함수를 이용해서변경
str_var="3.14"
test=float(str_var)
print(f"{test} / {type(test)}")

#리스트 타입을 문자열로 변경하기
#str()함수를 이용
test=str(list_var)
print(f"{test} / {type(test)}")

#튜플타입을 문자열로 변경하기
test=str(tuple_var)
print(f"{test} / {type(test)}")

#딕셔너리 문자열로 변경
test=str(dict_var)
print(f"{test} / {type(test)}")

#진위형으로 변경
#bool()함수를 이용

#숫자 데이터를 진위형으로 변경
num_test=1
bool_var=bool(num_test)
print(f"{bool_var} / {type(bool_var)}")
#반대도 가능함
num_test=int(bool_var)
print(f"{num_test} / {type(num_test)}")

#실수도 가능함
bool_var=bool(float_var)
print(f"{bool_var} / {type(bool_var)}")

bool_var = bool(0.0) #0.0일때만 false반환
print(f"{bool_var} / {type(bool_var)}")

#문자열 진위형 값이 있으면 true 반환 ,
bool_var=bool(str_var)
print(f"{bool_var} / {type(bool_var)}")
#공란일때 "" 면 false
bool_var=bool("")
print(f"{bool_var} / {type(bool_var)}")

#자주쓰는 자료형 -> 시퀸스, set,dict
#애도 bool로 변환도 가능함 : 값이 있으면 True 없으면 False반환
print(bool(list_var))
print(bool([]))
print(bool(tuple_var))
print(bool(()))
print(bool(set_var))
print(bool({}))
print(bool(dict_var))
print(bool({}))

#사용자가 입력하는 값 가져오기
#input()사용
print("문자열 입력 :",end="")
# str_var=input()
# print(str_var,type(str_var))

print("나이를 입력 : ",end=" ")
# var_num=int(input())
# print(int_var,type(var_num))

bool_var=True
while(bool_var) :
    try:
        print("정수입력 :",end=" ")
        input_data = int(input())
        bool_var=False
        print(f"input_data : {input_data}")
    except ValueError :
        print("자료형 잘못입력!!")

