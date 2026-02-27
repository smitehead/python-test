str_data="안녕하세요 저는 바나나인간입니다."

# 각 값을 인덱스로 접근할 수 있음
# "test".charAt(index번호)
# []
str_result=str_data[1]
print(str_result)
str_result=str_data[-1]
print(str_result)

# 슬라이싱으로 접근하기 -> substring()
str_result=str_data[3:5]
print(str_result)
str_result=str_data[-6:-3]
print(str_result)

# 반복문이용하기
for s in str_data : 
    print(s,end=" ")

# 문자열 데이터를 다루는 메소드
# 공백을 제거하는 메소드 -> strip()
str_data="       공백이 있는 문자열       "
str_result=str_data.strip()
print(str_result)

#특정 문자를 제거하기
str_data= "aaaa특정문구aaaaa"
str_data= str_data.strip("a")
print(str_data)

str_data="faweljlsdafjl여러문구지우기asfkljawjel"
str_data= str_data.strip("abcdefjhikmnop")
print(str_data)

#대소문자 변경 매소드 upper(), lower()
str_data="Hello Python How Are You"
str_result=str_data.upper()
print(str_result)
str_result=str_data.lower()
print(str_result)

# 문자열을 리스트로 변경하기
# 특정문자를 기준으로 변경 -> split()
str_list=str_data.split() # 기본 띄어쓰기를 기준으로 분할함.
# str_list=str_data.split("")
print(str_list)

str_csv="자바,오라클,html/css,javascript,servlet/jsp,spring,sprinboot,springsecurity,react.js"
str_result=str_csv.split(",")
print(str_result)

# 리스트를 문자열로 변경 -> join()
temp_list=["일","이","삼","사"]
str_result="".join(temp_list)
print(str_result)
str_result="->".join(temp_list)
print(str_result)

#문자열에서 특정 문자찾기 -> find() ->인덱스 번호를 반환함
result= str_data.find("Python")
print(result)

#앞 뒤 문자열찾기
# startWith(),endWith()
str_data="http://google.com"
result = str_data.startswith("http")
print(result)
result = str_data.endswith("com")
print(result)

#숫자로 변환이 가능한지,알파벳인지 도 확인이 가능함
#대문자만 문자열로 저장
str_data="AajseklEfFGELWKJfekwaklfFekjk"
str_result= [x for x in str_data if 'A'<=x<='Z']
print(str_result)

#컴프리헨즈
str_data="qruweioajsfkl12345asdlwqreoiup"
str_result= [x for x in str_data if '1'<=x<='9'] #isdigit()써도 가능
print(str_result)
