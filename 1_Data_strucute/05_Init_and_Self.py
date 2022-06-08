# 생성자
# 인스턴스의 생성과 초기값 저장을 한번에 할 수 있음

# 1. 객체를 생성 후 객체 속성 채우기
class Dog:
    def bark(self):
        print('멍')

myDog = Dog()
myDog.name = '멍구'
myDog.color = 'brown'
myDog.size = 'big'

# print(myDog.name)
# print(myDog.color)
# print(myDog.size)

# ==============================================#
# 2. 생성자 __init__ 을 사용하여 속성 설정
# 내가 원하는 속성을 설정하여, 여러 인스턴스를 편하게 만들 수 있다.
class Cat:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size

    def bark(self):
        print('야옹')

myCat = Cat('야옹옹', 'white', 'small')
# print(myCat.name)
# print(myCat.color)
# print(myCat.size)

# ==============================================#

# 3. self

# 아래와 같이 작성 했을 때,
# 내부적으로 파이썬은 Cat.bark(myCat) 로 작동 됩니다.
# 클래스 메서드를 호출 할 때, 첫 인자로 인스턴스가 전달 되는 것이다.
# 즉, self는 인스턴스(주소)를 자동으로 전달하는 것이다.
myCat.bark()

# 이렇게 작성해도 작성 된다
Cat.bark(myCat)


# ==============================================#

# 4. self 인스턴스 주소확인

class Foo:
    def fun1():
        print("function 1")

    def fun2(self):
        print(id(self)) # 메모리에 할당된 주소
        # print("function 2")

f = Foo()

# 정상
f.fun2()

# 오류
# func1() takes 0 positional arguments but 1 was given
# 인자가 없지만 하나를 받았다.
# f.fun1()

# 클래스 내에 정의된 self는 클래스 인스턴스 이다.
print(id(f))