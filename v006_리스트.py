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