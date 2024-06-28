# class
# 변수와 class명 함수명은 짓는 방식 존재
# 파이썬은 함수/함수명에 snake_case 사용
# 파이썬 class 은 camelCase 사용

# self 는 생성된 인스턴스 자기 자신

class SoccerPlayer(object):
    def __init__(self, name: str, position: str, back_number: int):
        self.name = name
        self.position = position
        self.back_number = back_number

    def __str__(self):
        return "hello, %s. %d" % (self.name, self.back_number)


park = SoccerPlayer("park", "wf", 13)
print(park)
