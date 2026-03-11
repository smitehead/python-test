# 클래스 속성 이용하기
# 인스턴스 속성 및 클래스 속성
# 인스턴스 : 클래스를 객체화 하고 나서 이용할 수 있는 속성 -> 생성 후 
# self예약어를 이용해서 생성자나 인스턴스 메소드, 생성된 객체에 접근해서 설정할 수 있음
# 프로그램의 복잡도를 낮추기 위해 일반적으로 인스턴스 속성은 생성자에서만 선언하는 것을 권장

# 클래스 속성 : 공통속성, 클래스를 객체화 하지 않고 사용이 가능
#  클래스내부에서 선언한 속성이나 생성자에서 클래스명.속성명으로 선언함
# 생성된 객체수를 확인, 생성된 객체에 일련번호를 부여할때 

from typing import Any


class Attribute_test:
    def __init__(self) : 
        # 속성설정
        self.name="아무개" # 인스턴스 속성
        self.items=[]
        # 클래스 속성설정
        Attribute_test.count=0

    def add_attrubute(self,value) : 
        # 인스턴스 속성을 추가
        self.address=value
        # 클래스속성 추가
        Attribute_test.id="1234"
    
attr_obj=Attribute_test()
print(f"이름 : {attr_obj.name} 아이템 : {attr_obj.items}")
# print(f"주소 : {attr_obj.address}")

# 클래스 속성에 접근하기
print(Attribute_test.count)

# 메소드로 추가한 속성에 접근하기 -> 메소드가 실행된 후 생성
attr_obj.add_attrubute("마산합포구")
print(f"주소 : {attr_obj.address}")
print(f"{Attribute_test.id}")

attr_obj2=Attribute_test()
# print(f"{attr_obj2.id}")
print(f"{attr_obj2.name} {attr_obj2.items}")

# print(attr_obj2.address)

# 생성된 객체에서 속성을 추가하기->하지마
# attr_obj.gender='남'
# print(attr_obj.gender)


# 속성관리하기
# 외부에서 속성을 추가하는 것을 막기
# __slots__예약어를 이용해서 속성 수정불가로 만들기
class AttrituteTest2 : 
    __slots__=["name","age","gender"]
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    # def add_attr(self, value) : 
    #     self.height=value

attr_obj3=AttrituteTest2("유병승",19,"남")
print(f"{attr_obj3.name} {attr_obj3.age}")
# attr_obj3.address="경기도 시흥시"
# attr_obj3.add_attr(180.5)

# print(attr_obj.__dict__)

#slots : DTO, VO클래스에 설정하는것이 좋다

#외부에서 접근이 불가능한 속성 만들기 ->캡슐화
#속성명에 __을 붙여서 처리
class CasulationTest :
    def __init__(self) :
        self.name="바나나"
        self.__age=22
    def set_age(self,value) :
        self.__age = value

    def get_age(self):
        return self.__age
obj_test = CasulationTest()
print(obj_test.name)
print(obj_test.get_age())

#get, set함수를 호출 -> 자바스러워서 불편함 ->데코레이터를 이용해서 속성에 접근
class Person :
    def __init__(self) :
        self.__name=""
    @property
    def name(self) :
        print("getter")
        return self.__name
    @name.setter
    def name(self,name) :
        print("setter")
        self.__name=name

p = Person()
print(p.name)
p.name = "바나나"
print(p.name)
