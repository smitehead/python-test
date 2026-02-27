list_int = [1,2,3,4,5]
list_float = [1.1,2.2,3.3,4.4,5.5]
list_str=["banana","nanaba","babana","nanana","nabana"]
list_mixed=[10,"bana",[10.1,20.2]]

list_int =list(range(1,6))
list_obj=list("하나둘셋")
print(list_int)
print(list_obj)

#생성된 리스트 인덱스로 접근하기
print(f"list_int[0] : {list_int[0]} {type(list_int[0])}")
print(f"list_float[0] : {list_float[0]} {type(list_float[0])}")

#인덱스로 값 수정하기 
list_int[0]=100
list_str[2]="바나나"
print(list_int)
print(list_str)

#기본 슬라이싱 이용하기
#인덱스 범위를 지정해서 값을 가져오거나 저장하는것
#리스트명[[시작인덱스] : [끝인덱스]] : 시작인덱스와 끝 인덱스는 생략이 가능하다
#출력시 시작인덱스는 포함, 끝인덱스는 불포함한다
print(list_int[2:4]) #2~3번 인덱스를 가져온다
print(list_int[3:]) #3번 인덱스부터
print(list_int[:2]) #0~1번까지 인덱스 값
print(list_int[:]) #전체

#인덱스 번호에 음수를 넣으면 뒤에서부터 조회한다
print(list_int[-1]) #마지막 인덱스
print(list_int[-1*(len(list_int))])

#슬라이싱으로 음수 이용하기
print(list_int[-3:-1])

print(list_str)
list_str[1:3]=["바나나","나나바"]
print(list_str)

list_str[4:]=['a','b','c']
print(list_str)
list_temp=[]
list_temp[4:]=['a','b','c']
print(list_temp)
list_temp[len(list_temp):]=range(1,11)
print(list_temp)

#문자열을 대입하기
list_temp[len(list_temp):] = "안녕하세연"
print(list_temp)

# 슬라이싱을 이용해서 값 대입하기
print(list_str)
list_str[1:3]=['이경민','박종권','김태우','김민규']
print(list_str)
list_str[4:]=['a','b','c']
print(list_str)
list_temp=[]
list_temp[4:]=['a','b','c']
print(list_temp)
list_temp[len(list_temp):]=range(1,11)
print(list_temp)
# 문자열 대입하기
list_temp[len(list_temp)-1]="안녕하세요"
print(list_temp)

# 특정 범위를 삭제하기
print(f"이전값 {list_temp}")
list_temp[0:4]=[]
print(f"이후값 {list_temp}")

# 시작, 끝이 동일하면 삽입으로 처리
print(f"전체값 list_int {list_int}")
list_int[2:2]=range(5)
print(f"전체값 list_int {list_int}")

# 범위를 벗어나서 지정 -> 자동으로 추가
list_empty=[]
print(f"list_empty : {list_empty}")
list_empty[0:2]=[1,2,3,4]
print(f"list_empty : {list_empty}")
print(list_empty[2])

#반복문을 이용해서 데이터 순회
# 방법 : for 변수명 in sequnceType : 로직
for a in list_int :
    print(f"a = {a}")

#인덱싱을 이용하기
for i in range(len(list_int)) :
    print(f"{i} : {list_int[i]}")

#인덱스 ,값을 한번에 반복문에서 활용하기
for i,v in enumerate(list_int) :
    print(f"{i} : {v}")

#옵션 : start = 시작 인덱스 지정
print("=====start 인덱스 =====")
for i,v in enumerate(list_int,start=5) :
    print(f"{i} : {v}")

#리스트의 길이 확인
print(len(list_int))

#리스트 연산하기 ->연산자 제공
print("====연산자====")
list_op_a=[1,2,3,4]
list_op_b=["바나나","나나바","바바나"]
list_op_result=list_op_a+ list_op_b #원본값은 안바뀜
print(list_op_result)

#곱하기 연산
list_op_result=list_op_a*3
print(f"list_op_a*3 = {list_op_result}")

#리스트의 대소비교
print("====리스트 대소 비교하기====")
list_str_com=["a","b","c"]
list_str_com2=["z","a","b"]
print(f"list_str_com < list_str_com2 : {list_str_com < list_str_com2}")

list_tuple_com=[(1,2,3),(4,5,6)]
list_tuple_com2=[(4,3,2),(1,2,3)]
print(f"list_tuple_com < list_tuple_com2 : {list_tuple_com < list_tuple_com2}")

# list에 저장된 값 확인하기
# in, not in 
result=200 in list_op_a
print(f"result : {result}")

if 200 in list_op_a : 
    print("3이 있다")

# list_op_b에 김영호가 없으면 추가하기
if "김영호" not in list_op_b : 
    list_op_b[len(list_op_b):]=["김영호"]
print(list_op_b)

# 내장함수 이용하기 -> built-in함수
# sorted함수
# 데이터를 정렬하는 함수
# 매개변수 iterable, key, reverse이용
print("==== sorted함수 이용하기 ====")
list_order=sorted(list_int)
print(f"list_order : {list_order}")

#내림차순 정렬
list_order=sorted(list_int,reverse=True)
print(f"list_order : {list_order}")

#key파라미터 : 정렬기준
list_str=["하나","코리아","대한민국","김수한무거북이와","바나나나주바바바나가바바가"]
list_str=sorted(list_str,key=len,reverse=True)
print(list_str)


#max/min함수
print("===숫자형 list====")
print(f"max(list_int) : {max(list_int)}")
print(f"min(list_int) : {min(list_int)}")

print("===문자형 list====")
print(f"max(list_str) : {max(list_str)}")
print(f"min(list_str) : {min(list_str)}")

#합계 (sum 함수)
print(f"list_int 합계 : {sum(list_int)}")

#메소드 이용하기
#append함수 사용하기
list_test=[]
list_test.append("바나나")
list_test.append("나나나")
print(list_test)

#랜덤데이터 출력하기
import random
list_test=[]
for i in range(1,20,1) :
    list_test.append(random.randint(1,10))
    print(list_test)

#pop()
result = list_test.pop()
print(f"삭제값 : {result} / 원본 : {list_test}")

#매개변수 index번호 ->해당인덱스의 값을 짤라냄
result =list_test.pop(3)
print(f"삭제값 : {result} / 원본 : {list_test}")

#sort()/reverse()
list_test.sort()
print(f"정렬 : {list_test}")
list_test.reverse()
print(f"역순 : {list_test}")

# 값의 인덱스 번호 가져오기
#java->indexof() 여기는 -> index()
search_index=list_test.index(5)
print(f"5의 인덱스 : {search_index}")
# search_index=list_test.index(20)
# print(f"20의 인덱스 : {search_index}")

# insert(index,value) 중간에 값을 삽입하는 함수
list_test.insert(3,100)
print(list_test)

# remove() 삭제하는 함수
list_test.remove(5)
print(list_test)

#count() 값을 갯수를 찾기
result = list_test.count(2)
print(f"중복의 갯수 : {result}")

#copy() : 복사만들기
copy_list=list_test.copy()
print(f"copy_list : {copy_list}")

#clear 전체삭제
copy_list.clear()
print(f"copy_list : {copy_list}")

 #리스트 삭제 :
# copy_list=None
# print(copy_list[0])

#원하는 위치의 값을 삭제하는 방법
#del(list[인덱스 번호])
print(list_test)
del(list_test[0])
print(list_test)

#리스트 언패킹
#리스트에 있는 요소를 각 변수에 저장해주는 기능
#조건 : 리스트에 저장된 요소수와 변수의 수가 동일해야함
# *변수명 : 그 외 요소를 리스트로 받음

list_unpacking=[1,2,3,4,5]
a,b,c,d,e=list_unpacking
print(f"{a}, {b}, {c}, {d}, {e}")

#숫자를 안맞추면 에러남
# a,b,c,d=list_unpacking
# print(f"{a}, {b}, {c}, {d}")

a,b,c,*d=list_unpacking
print(f"{a}, {b}, {c}, {d}")

#for 문에서 언패킹 이용하기 ->2차원 방식의 데이터를 활용할때
list_unpacking=[[1,2],[3,4],[5,6]]
for col1,col2 in list_unpacking :
    print(f"col1: {col1}, col2: {col2}")
#이차원 리스트 이용하기
list_metrix=[[1,2,3,4],["바나나","나나바","바나바","나바나"],[1.1,2.2,3.3,4.4]]

#인덱스로 접근하기 변수명[행][열]
print(list_metrix[0])
print(list_metrix[0][1])

#슬라이싱으로 접근하기
# [:]
#특정 열을 가져오기
print(list_metrix[0][0:3])
print(list_metrix[1][:2])
#행을 가져오기
print(list_metrix[0:2])

# 인덱스로 데이터 저장하기
# list_matrix[0][1]=200
# list_matrix[1][3]="짱구"
# print(list_matrix)
# list_matrix[1]=list("abcde")
# print(list_matrix)
# 인덱스를 초과해서 저장
# list_matrix[len(list_matrix)]=list("일이삼사")
# list_matrix[len(list_matrix):len(list_matrix)]=list("일이삼사")
# print(list_matrix)

# for row in list_matrix : 
#     for col in row : 
#         print(col,end=" ")
#     print()

# 특정 지역의 좌표를 가져와 출력하기
list_coords=[[32.2,123.12],[12.3,114.3],[12,33],[123.11,23.12]]

for x,y in list_coords : 
    print(f"좌표 : {x} {y}")

#컴프리핸션
list_data=[11,23,34,45,50]

list_result = [x**2 for x in list_data]
print(list_result)

# 짝수인 값만 거듭제곱해서 새로운 리스트만들기
list_result=[x**2 for x in list_data if x%2==0]
print(list_result)
import random
# 랜덤 원하는 수만큼 배열만들기
list_result=[random.randint(1,10) for _ in range(5)]
print(list_result)
#이름만 빼서 리스트 만들기