#튜플 이용하기
#순서가 있는 불변의 자료형 ->고정값을 가지고 데이터를 처리할때
#생성 : 리터럴 = (1,) tuple()생성
#읽기 전용으로 활용

print(f"{'='*4}생성하기{'='*4}")
tuple_int =(1,2,3,4)
tuple_str=("바나나","나나바","바바나")
tuple_other=(tuple_int,tuple_str,[1,2,3])
tuple_data = 10,20,30,40
print(f"{tuple_data} type : {type(tuple_data)}")

tuple_obj=tuple([1,2,3,4,5])
tuple_obj=tuple("문자열")
print(tuple_obj,type(tuple_obj))

# 튜플은 읽기전용 자료형으로 수정이 불가능함
# tuple_int[0]=100

# 튜플값 가져오기
# 인덱싱, 슬라이싱방식으로 처리할 수 있음
print(tuple_int[0])
print(tuple_int[1])

#음수로 접근하기
print(tuple_int[-1])

#슬라이싱
print(tuple_str[0:2])
print(tuple_str[:3])
print(tuple_str[-3:-1])

#for로 튜플데이터 순회하기
for i in range(len(tuple_str)) :
    print(tuple_str[i])

for n in tuple_str : 
    print(n)

for i,v in enumerate(tuple_str) : 
    print(f"{i} {v}")

# +, * 연산자 이용하기 -> 리스트와 동일 
print(tuple_int+tuple_str)
print(tuple_int*2)

# in, not in
print(f"{'바나나' in tuple_str}")
print(f"{'나나바' not in tuple_str}")

# 내장함수 이용가능
# min, max, sum, len, sorted, count

# 랜덤으로 문자열을 생성해서 특정문자 갯수 확인
import string, random
tuple_random_letter=tuple(''.join(random.choices(string.ascii_lowercase,k=20)))
print(tuple_random_letter)

#튜플에서 b가 몃개인지 출력하기


print(tuple_random_letter.count('b'))

#이차원 튜플이용하기
print("==-=이차원 튜플 이용하기====")
tuple_double = ((1,2,3,4),(5,6,7,8),(9,10))

#값에 접근하기
print(tuple_double[0][0])
print(tuple_double[1][1])
print(tuple_double[2])

# 슬라이싱으로 데이터 가져오기
print(tuple_double[1:3])
# 두번 슬라이싱을 해서 가져온 결과
# 0~1번 을 가져온 튜플에서 1번2번 인덱스 튜플을 가져오는 것
print(tuple_double[0:2][1:3])

print(tuple_double[0:2][1:3][0][1])

# 이차원튜플에서 반복문 이용하기
for i in range(len(tuple_double)) : 
    for j in range(len(tuple_double[i])) : 
        print(tuple_double[i][j],end=" ")
    print()

for row in tuple_double : 
    for col in row : 
        print(col, end=" ")
    print()

#튜플은리스토와 호완이 가능하다
test_list=["강원준","하승우","이경민","임민규","정수혁"]
test_tuple=tuple(test_list)
print(test_tuple)
test_list=list(test_tuple)
print(test_list)

#튜플 del()을 이용해서 특정인덱스를 삭제는 불가능
# print(test_tuple)
# del(test_tuple[0])
# print(test_tuple)

test_tuple=None

#컴프리헨션
tuple_com = tuple(x**2 for x in tuple_int if x>3)
print(tuple_com)