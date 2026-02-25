#맴버쉽 연산자
# SequenceType, MappingType에 특정한 값이 있는지 확인해주는 연산자
#in , not in
str_temp="apple"
print(f"str_temp에 p가 있나? : {'p' in str_temp}")
print(f"str_temp에 p가 있나? : {'p' not in str_temp}")

list_temp=["홍길동","이순신","고길동","세종대왕"]
print(f"list_temp에 banana가 있나? : {'banana' in list_temp}")

tuple_temp=(1,2,3,4,5)
print(f"tuple_temp에 3이 있나? : {3 in tuple_temp}")
print(f"tuple_temp에 3이 있나? : {"3" in tuple_temp}")

dict_temp={"gender" : "남","email":"test@test.com"}
#key를 기준으로 찾기때문에 밑에껀 나옴
print(f"dict_temp에 gender가 있나? : {'gender' in dict_temp}")
#엔 벨류값이라 안나옴
print(f"dict_temp에 gender가 있나? : {'남' in dict_temp}")

#value값을 기준으로 검색하는 방법은?
#values()를 사용함
print(f"dict_temp에 남이 있나? : {'남' in dict_temp.values()}")

#아텐티티 연산자
#값이 아닌 주소로 비교연산을 하는것
# == 동등성 비교 -> 값을 비교함 / 근데 is 는 동일성 비교를함 -> 주소를 비교
print(str_temp == "apple")
#apple을 치면 주소가 달라서 false가 됨
# input_data=input()
# print(str_temp is input_data)

def test_su():
    return int('10')
su =test_su()
sy1=test_su()
print(su == sy1)
print(su is sy1)

#None값을 비교할때 사용함 ->안정적으로 사용
test_temp=None
print(test_temp == None)
print(test_temp is None)

#삼항연산자 
age = 20
result = "성인" if age>19 else "미성년자"
print(result)

#비트연산
bnum = 0b1010
bnum2 = 0b1100
print(f"{bnum:032b} 일반출력")
print(f"{bnum>>1:032b} >>1 쉬프트 연산(오른쪽으로 이동 / 2)")
print(f"{bnum<<1:032b} <<1 쉬프트 연산(왼쪽으로 이동 * 2)")
print(f"{bnum:032b} 일반출력")
print(f"{bnum2:032b} 일반출력")
print(f"{bnum^bnum2:032b}")
print(f"{bnum|bnum2:032b}")

#비트 마스킹
#특정값에서 지정한 자리수에 값이 있는지 확인

#권환확인이나 이런 로직을 만들수 있음
bit=0b1010
bit2=0b0011
mask =0b1000
#첫번째자리에 0이있나를 찾는것 이게 평범한거보다 훨씬빠르기때문에 사용함
print(f"{bit:032b} {bit&mask > 0}")