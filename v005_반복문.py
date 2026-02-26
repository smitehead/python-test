#python에서 반복문은 간단하고 유연하게 사용이 가능함
#for문 -> 자바의 foreach문과 유사하다

#for 변수 in range(값[,끝,간격])

#0~9까지 출력하기
for i in range(10) :
    print(i,end=" ")
#1~10까지 출력하기
for i in range(1,11) :
    print(i,end=" ")
for i in range(1,11,2) :
    print(i,end=" ")

#구구단 구현
# dan =int(input())
# for i in range(1,10) :
#     print(f"{dan} x {i} = {dan*i}")

#for문은 리스트와튜플을 이용할 수도 있다
for s in ["가","나","다"] :
    print(s)

#while 의도적인 무한루프 조건에 맞는 루프를 처리할때 
# while True :
#     print("무한루프")

#끝을 입력할때까지 입력값을 저장호고 모든 입력을 출력하기
sum=[]
while True :
    a = input("입력 :")
    sum+=a
    if(a=="끝") :
        break
print(sum)