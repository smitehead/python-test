#파이선에서 조건문을 사용할땐 {}사용하지 않는다
# : 과 들여쓰기를 기준으로 조건문의 영역을 구분

#if 조건문 : 실행할 구문 작성

# print("수입력 :" ,end="")
# su = int(input())
# if(su>10) :
#     print(f"{su}는 10보다 크다")
# else :
#     print(f"{su}는 10보다 작다")

#조건에 따라 할인율 적용하기
coopon="W1234"
product_price=100000

# if(coopon=="w1234") :
#     discount=0.2
# print(f"쿠폰을 사용한 가격은 {product_price * (1-discount)}원 입니다")


#문자열에 특정 문자가 있는지 확인하기
# str_name="banana"
# if (t:=input()) in str_name :
#     print(f"{t}는 str_name에 포함되어 있습니다.")

# if(t:=int(input())) % 2 == 0 :
#     print(f"{t}는 짝수입니다")
# else :
#     print(f"{t}는 홀수입니다")

# if ~elif ~else 구문 이용하기
print("점수 입력 : ", end="")
# score = int(input())

# if score >= 90:
#     grade = "A"
# elif score >= 80:
#     grade = "B"
# elif score >= 70:
#     grade = "C"
# elif score >= 60:
#     grade = "D"
# else:
#     grade = "F"

# print(f"당신의 점수는 {score}점이고, 학점은 {grade}입니다.")

# if문 내부에 다른 if문 사용하기
# if(coopon:=input("쿠폰번호 : ")) == "W1234" :
#     if(age :=int(input("나이 :"))) >19 :
#         print("nice day!")
#     else : 
#         print("성인만 가능")
# else :
#     print("잘못된 쿠폰번호")

#404,403,400,200,500이런 에러코드같은거도 이렇게 가능함

# match ~ case 구문이용하기
print("====정수형을 match문에 넣기====")
print("1.회원등록")
print("2.회원수정")
print("3.회원삭제")
print("4.회원조회")
print("메뉴 선택 : ", end="")
# choice = (int)(input())
# match choice :
#     case 1 : print("등록기능 개발중....")
#     case 2 : print("수정기능 개발중....")
#     case 3 : print("삭제기능 개발중....")
#     case 4 : print("조회기능 개발중....")
#     case _ : print("업는 기능입니다")
    
# print("==== 조건문 match문에 넣기 ====")
# match choice <4 :
#     case True : print("메뉴에 있는 번호입니다")
#     case False : print("메뉴에 없는 번호입니다")

# 데이터구조를 확인하는 조건문에 사용가능
#리스트 매칭하기
list_sample=[10,2,3,4,]

match list_sample :
    case [1,2,3,4] : print("[1,2,3,4]인값")
    #0인 인덱스가 10이고 길이가 4인 리스트
    case [10,x,y,z] : print(f"[10,{x},{y},{z}]인값")
    # 0번이 100이고 임이의값 2개 , 최소길이가 3개인 리스트
    case [100,x,y,*other] : print(f"[100,{x},{y},{other}]인값")
    #임의의값 3개를 가지는 리스트
    case [x,y,z] : print(f"[{x,{y},{z}}]")
    case [str() as a,int() as b, float() as c] : print("타입을 확인하는 패턴")
    case _ : print("매칭되는 패턴이 없습니다")
    

# move_tuple=("",x,y)
# match move_tuple : 
#     case ("FORWARD",x,y) : print(f"앞으로 ({x},{y})")
#     case ("BACKWARD",x,y) : print(f"뒤로 ({x},{y})")
#     case ("STOP") : print("이동 중지")
#     case _ : print("없는 명령입니다.")


# 딕셔너리 -> key,value
dict_sample={"code":404,"status":"error"}

match dict_sample : 
    case {"code":404,"status":x} : print(f"{dict_sample['code']}")
    case {"code":500,"status":"fail"} : print(f"{dict_sample['code']} 서버에서 에러가발생함")
    case {"code":200,**other} : print(f"{dict_sample['code']} {other}")
    case _ : print("일치하는게 없음")

# 가드이용하기
data=[2,3,6]
data=[10,2]
match data : 
    case list() as lst if len(lst) >=3 and all(x%2==0 for x in lst) : print("짝수만 있는 3개 이상의 리스트")


    case [a,b] if a+b >10 : print(f" 두요소의 합이 10초과 : {a}+{b} = {a+b}")

#튜플
# 최소 두개 이상 요소, 첫 요소는 음수 나머지 합(sum)은 양수인 데이터 패턴 찾기
# 길이가 3이고 모든 요소가 4와 같은 값인 패턴찾기
#단일요소 튜풀찾기

data=[4]
match data : 
    case list() as lst if len(lst) >=2 and sum(lst) > 0 and lst[0] < 0 :
        print("최소 두개 이상 요소, 첫 요소는 음수 나머지 합(sum)은 양수인 데이터 패턴 찾기")
    case (x,y,z)if x==y==z==4: print("길이가 3이고 모든 요소가 같은 값")
    case (x,) : print("단일요소 튜플")

#