# %%

# 1. 1부터 100까지 합 (for문 활용)

sum = 0
for i in range(1,101):
    sum += i
print(sum)

# %%

# 2. 다음 소스코드에서 클래스를 작성하여 게임 캐릭터의 능력치와 '파이어볼'이 출력되게 만드시오.
#**주어진 소스 코드를 수정해선 안됩니다.**

# 출력 예시
# 545 210 10
# 파이어볼

class Wizard:
    def __init__(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor
        
    def attack(self):
        print("파이어볼")
    

x = Wizard(health=545, mana=210, armor=10)
print(x.health, x.mana, x.armor)
x.attack()

# %%

# self 스스로 메모리를 생성하여 전달하는 역할
class Foo01:
        def func1():
                print("function 1")
        def func2(self):
                print("function 2")

f = Foo01()

f.func2()
# 파이썬 메서드의 첫번째 인자로 항상 인스턴스가 전달 되기 때문에 발생하는 문제
# 인자가 없지만 하나를 받아서 error
# f.func1() 

# %%

# 파이썬의 클래스는 그 자체가 하나의 네임스페이스이기 때문에 인스터스 생성과 상관없이
# 클래스 내의 메소드를 직접 호출 할 수 있습니다.

class Foo02:
    def func1():
            print("function 1")

    def func2(self):
            print(id(self))
            print("function 2")

f = Foo02()

print( id(f)) 
f.func2()

# 위 코드는 func1 메서드를 호출했지만 앞서 인스턴스를 통해 메서드를 호출했던 것과는 달리 오류가 발생하지 않는 것을 확인할 수 있습니다. 
# 왜냐하면 인스턴스.메서드() 형태로 호출한 것과 달리 이번에는 클래스명.메서드() 형태로 호출했기 때문입니다.
Foo02.func1()


# %%

# 3. 우리 태양계를 이루고 있는 행성은 수성, 금성, 지구, 화성, 목성, 토성, 천왕성, 해왕성으로 총 8개 입니다. 
# 저희는 우리 태양계의 n번째 행성이 무엇인지 알고 싶습니다.
# 입력 1 // 출력 수성

def plate(n):
    plate_list = ["수성", "금성", "지구", "화성", "목성", "토성", "천왕성", "해왕성"]
    return plate_list[n-1]

result = plate(1)
print(result)

# %%

# 4. 영희는 친구와 게임을 하고 있습니다. 서로 돌아가며 랜덤으로 숫자를 하나 말하고 
# 그게 3의 배수이면 박수를 치고 아니면 그 숫자를 그대로 말하는 게임입니다.
# 입력 3 // 출력 짝짝짝
# 입력 2 // 출력 2

def game(n):
    if n%3 == 0:
        print("짝짝짝") 
    else :
        print(n)

game(1)


# %%

# 5. 신학기가 시작되고, 아이들이 돌아가면서 자기소개를 하기로 했습니다.
# 만약 입력으로 `김다정`이라는 이름이 주어지면
# 출력 = 안녕하세요. 저는 김다정입니다.

def hello(name):
    print("안녕하세요. 저는 " + name + "입니다") 

hello('김다정')


# %%
